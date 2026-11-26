#!/usr/bin/env python3
"""Confere o layout de skills e o contrato dos perfis de trilha.

Canônico: `.agents/skills/<nome>/SKILL.md`
Compat:   `.cursor/skills` e `.claude/skills` → symlinks para `.agents/skills`

Uso (na raiz do repo):
  python3 tools/sync_skills.py          # valida; recria symlinks se faltarem
  python3 tools/sync_skills.py --check  # só verifica; sai com erro se divergir

Também confere se cada cargos/<trilha>/perfil.md tem as seções fixas (PERFIL_SECOES).
Só usa a biblioteca padrão (Windows, WSL, Linux, macOS).
"""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CANON = ROOT / ".agents" / "skills"
LINK_NAMES = (".cursor/skills", ".claude/skills")
PERFIL_SECOES = [
    "## Identificação",
    "## Mapa e tags",
    "## Discursiva",
    "## Prioridades do P3",
    "## Escopo dos itens",
    "## Especificidade técnica (anti-dedução)",
    "## Fontes técnicas primárias",
    "## Amostra de dificuldade",
    "## Acervo mais aderente",
    "## Exemplos de pedidos",
]


def skill_dirs() -> list[pathlib.Path]:
    if not CANON.is_dir():
        return []
    return sorted(p for p in CANON.iterdir() if (p / "SKILL.md").is_file())


def resolve(p: pathlib.Path) -> pathlib.Path | None:
    try:
        return p.resolve()
    except OSError:
        return None


def link_ok(rel: str) -> tuple[bool, str]:
    path = ROOT / rel
    if not path.exists() and not path.is_symlink():
        return False, "ausente"
    if not path.is_symlink():
        # Windows Git sem core.symlinks às vezes materializa cópia
        got = resolve(path)
        want = resolve(CANON)
        if got is not None and want is not None and got == want:
            return True, "cópia materializada (ok; prefira symlink)"
        return False, "não é symlink nem cópia de .agents/skills"
    target = path.readlink()
    # Aceita relativo ou absoluto que resolva para CANON
    got = resolve(path)
    want = resolve(CANON)
    if got is None or want is None or got != want:
        return False, f"symlink quebrado ou alvo errado ({target})"
    return True, str(target)


def ensure_symlink(rel: str) -> None:
    path = ROOT / rel
    if path.is_symlink() or path.exists():
        if path.is_symlink() or path.is_file():
            path.unlink()
        elif path.is_dir():
            # Não apagar árvore real por engano
            raise SystemExit(
                f"{rel} é um diretório real — remova/mova manualmente e rode de novo"
            )
    path.symlink_to(pathlib.Path("../.agents/skills"))


def perfis_incompletos() -> dict[str, list[str]]:
    faltas: dict[str, list[str]] = {}
    cargos = ROOT / "cargos"
    if not cargos.is_dir():
        return {"cargos": ["ausente"]}
    for perfil in sorted(cargos.glob("*/perfil.md")):
        txt = perfil.read_text(encoding="utf-8")
        miss = [h for h in PERFIL_SECOES if not any(l.strip() == h for l in txt.splitlines())]
        if miss:
            faltas[perfil.parent.name] = miss
    for trilha in sorted(p.name for p in cargos.iterdir() if p.is_dir()):
        if not (cargos / trilha / "perfil.md").exists():
            faltas[trilha] = ["perfil.md ausente"]
    return faltas


def main() -> None:
    check = "--check" in sys.argv
    errors: list[str] = []

    if not CANON.is_dir():
        errors.append(f"canônico ausente: {CANON.relative_to(ROOT)}")
    skills = skill_dirs()
    if not skills and CANON.is_dir():
        errors.append(".agents/skills/ sem nenhum SKILL.md")

    for rel in LINK_NAMES:
        ok, detail = link_ok(rel)
        if ok:
            continue
        if check:
            errors.append(f"{rel}: {detail}")
        else:
            try:
                ensure_symlink(rel)
                print(f"Recriado symlink: {rel} -> ../.agents/skills")
            except SystemExit as e:
                errors.append(str(e))
            except OSError as e:
                errors.append(f"{rel}: não foi possível criar symlink ({e})")

    faltas = perfis_incompletos()
    if faltas:
        errors.append(f"Perfis de trilha incompletos: {faltas}")

    if errors:
        for e in errors:
            print(e)
        print("Canônico: .agents/skills/  |  Compat: .cursor/skills e .claude/skills → symlink")
        print("Windows: git config core.symlinks true (e Developer Mode se necessário)")
        sys.exit(1)

    names = [p.name for p in skills]
    print(
        "OK: .agents/skills canônico; .cursor/.claude symlinks; "
        f"skills={names}; perfis completos"
    )


if __name__ == "__main__":
    main()
