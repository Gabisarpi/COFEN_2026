"""Regras de etiquetagem do acervo Quadrix → tags do mapa do Cargo 407 (cargos/tic/mapa-edital.md).

`tags_bloco(secao, comando, itens)` devolve as tags de um bloco. O comando ("julgue os itens…")
decide primeiro; só se ele não bastar, o texto dos itens. Bloco sem tag = assunto fora do edital
do 407 (ex.: atualidades, lei de outra profissão): fica no acervo com `tags_edital: []`.
Ajuste fino depois da extração: editar o frontmatter do bloco (a tag manual vale).
"""
from __future__ import annotations

import re

I = re.IGNORECASE

# Ordem importa só para a ordem das tags no arquivo.
REGRAS_COMP = [
    (r"5\.905|94\.406|7\.498|Resolu[çc][ãa]o COFEN|Regimento Interno do COREN|C[óo]digo de [ÉE]tica dos Profissionais de Enfermagem|Sistema COFEN", "comp.leg.enfermagem"),
    (r"8\.429|improbidade", "comp.leg.improbidade"),
    (r"9\.784|processo administrativo", "comp.leg.processo"),
    (r"13\.709|LGPD|prote[çc][ãa]o de dados", "comp.leg.lgpd"),
    (r"14\.133|licita[çc]|contrata[çc][õo]es p[úu]blicas", "comp.leg.licitacoes"),
    (r"12\.846|anticorrup", "comp.leg.anticorrupcao"),
    (r"12\.527|acesso [àa] informa[çc][ãa]o|7\.724", "esp.tic.etica"),
    (r"[ée]tica (no|do) (setor|servi[çc]o) p[úu]blico|1\.171|c[óo]digo de [ée]tica profissional do servidor", "esp.tic.etica"),
    (r"art(igo)?s?\.? ?(5|196|197|198|199|200)\b.*Constitui|Constitui[çc][ãa]o.*sa[úu]de|seguridade social|SUS\b|direitos e deveres individuais", "comp.leg.cf"),
    (r"Constitui[çc][ãa]o|CF/1988|CF/88|direitos e garantias|organiza[çc][ãa]o do Estado|Poder (Legislativo|Executivo|Judici)", "comp.const"),
    (r"Direito Administrativo|atos? administrativ|poderes administrativ|administra[çc][ãa]o (direta|indireta)|autarquia|conselhos? de fiscaliza[çc][ãa]o|servidor(es)? p[úu]blico|agentes? p[úu]blico|empregado p[úu]blico|sindic[âa]ncia|PAD\b|princ[íi]pios da administra|controle (judicial|da Administra)|responsabilidade civil do Estado|danos causados a particulares|8\.112", "comp.adm"),
]

REGRAS_ESP = [
    (r"5\.905|94\.406|Resolu[çc][ãa]o COFEN|Regimento Interno do COREN|C[óo]digo de [ÉE]tica dos Profissionais", "comp.leg.enfermagem"),
    (r"contrata[çc][ãa]o de solu[çc][õo]es de TI|termo de refer[êe]ncia|IN SGD|94/2022|fiscal(iza[çc][ãa]o)? (t[ée]cnic|administrativ|do contrato|de contrato)|gest[ãa]o (e fiscaliza[çc][ãa]o )?de contratos|14\.133|estudo t[ée]cnico preliminar|licita", "esp.tic.contratos"),
    (r"auditoria|controles? internos?|conformidade\b|compliance", "esp.tic.auditoria"),
    (r"governan[çc]a (e gest[ãa]o )?de (TI|TIC|dados)|PDTI|planejamento estrat[ée]gico de TI|indicadores|BSC|balanced scorecard|portf[óo]lio", "esp.tic.gestao"),
    (r"ITIL|COBIT|gerenciamento de servi[çc]os|gest[ãa]o de servi[çc]os|SLA|acordo de n[íi]vel|central de servi[çc]os|service desk|gest[ãa]o de riscos|gerenciamento de (incidentes|problemas|mudan)", "esp.tic.govti"),
    (r"seguran[çc]a da informa[çc][ãa]o|criptograf|certificad[oa] digital|assinatura digital|malware|v[íi]rus|ransomware|phishing|ataque|vulnerabilidad|27001|27002|backup|c[óo]pia de seguran|continuidade de neg|firewall|IDS|IPS|autentica[çc][ãa]o|controle de acesso|hash", "esp.tic.seguranca"),
    (r"redes? de computadores|\brede\b|\bredes\b|OSI|TCP|UDP|\bIP\b|IPv[46]|roteador|switch|DNS|DHCP|VPN|VLAN|protocolo|Wi-?Fi|WLAN|LAN\b|WAN\b|cabeamento|HTTP|SMTP|FTP|camada de (rede|transporte|enlace)", "esp.tic.redes"),
    (r"banco de dados|SQL|SGBD|normaliza[çc][ãa]o|modelo relacional|entidade-relacionamento|NoSQL|ETL|data ?warehouse|data ?lake|OLAP|PostgreSQL|MySQL|Oracle", "esp.tic.bd"),
    (r"engenharia de software|UML|Scrum|Kanban|[áa]gil|ciclo de vida|teste[s]? de software|requisitos|programa[çc][ãa]o|POO|orientad[ao] a objetos|Python|Java\b|JavaScript|PHP|algoritmo|estrutura de dados|Git\b|DevOps|API", "esp.tic.engsw"),
    (r"virtualiza|hipervisor|cont[êe]ineres?|Docker|Kubernetes|servidor(es)? (de|web)|Active Directory|AD DS|armazenamento|storage|RAID|SAN\b|NAS\b|monitoramento|Zabbix|gest[ãa]o de ativos|invent[áa]rio|migra[çc][ãa]o|implanta[çc][ãa]o|datacenter|data center|alta disponibilidade|cluster", "esp.tic.infra"),
    (r"sistemas? operaciona|Linux|Windows|barramento|processador|CPU|mem[óo]ria|hardware|perif[ée]ric|arquitetura de computadores|computa[çc][ãa]o em nuvem|nuvem|cloud|IaaS|PaaS|SaaS|intranet|internet|escalonamento|processos? e threads|sistema de arquivos", "esp.tic.fundamentos"),
    (r"LGPD|13\.709|prote[çc][ãa]o de dados|12\.527|acesso [àa] informa[çc][ãa]o|improbidade|8\.429|9\.784|[ée]tica no setor", "esp.tic.etica"),
    (r"atendimento|suporte (ao|a) usu[áa]rio|parecer|nota t[ée]cnica|ouvidoria|treinamento", "esp.tic.atendimento"),
]

ATUALIDADES = re.compile(r"atualidades|eventos? pol[íi]ticos|contexto (europeu|internacional|mundial)|elei[çc][õo]es|guerra|conflito|Faixa de Gaza|Ucr[âa]nia|Ir[ãa]\b|cen[áa]rio (pol[íi]tico|econ[ôo]mico|internacional)", I)


def _aplica(regras, texto: str) -> list[str]:
    out = []
    for rx, tag in regras:
        if re.search(rx, texto, I) and tag not in out:
            out.append(tag)
    return out


OUTRO_CONSELHO = re.compile(
    r"COFFITO|CREFITO|\bCREF\b|CREF-\d|CONFEF|\bCFP\b|\bCRP\b|Conselhos? (Federal|Regionais|Regional) de (Psicologia|Fisioterapia|Odontologia|"
    r"Medicina|Educa[çc][ãa]o F[íi]sica|Administra[çc][ãa]o|Contabilidade|Fonoaudiologia|Arquitetura)|\bCRO\b|\bCFO\b|CRMV|CFMV|\bCRM\b|\bCFM\b|"
    r"profiss[õo]es? de (fisioterapeuta|psic[óo]logo|m[ée]dico|cirurgi[ãa]o-dentista|profissional de educa)|9\.696/1998|6\.316/1975|5\.766/1971|5\.081/1966|5\.517/1968", I)


def frase_comando(cmd: str) -> str:
    """A frase do comando ("Em relação a …, julgue os itens"), sem o texto-base."""
    partes = re.split(r"(?<=[.!?])\s+", cmd.strip())
    for p in reversed(partes):
        if re.search(r"julgue|judge", p, I):
            i = partes.index(p)
            return " ".join(partes[max(0, i - 1):i + 1]) if len(p) < 60 else p
    return cmd[-300:]


def tags_bloco(secao: str, comando: str, itens: str) -> list[str]:
    cmd = comando or ""
    frase = frase_comando(cmd)
    if secao == "basicos":
        if ATUALIDADES.search(frase) or re.search(r"pol[íi]tica e da economia|ci[êe]ncia aberta|DSpace|epistemologia|10\.973", frase, I):
            return []
        leg = _aplica(REGRAS_COMP, frase)
        if leg and not re.search(r"texto|linha \d", frase, I):
            return leg[:2]
        if re.search(r"Text for items|julgue the|according to the text|\bthe\b.*\bthe\b", cmd + " " + itens[:400], I) and not re.search(r"\bque\b|\bnão\b", itens[:300], I):
            return ["basicos.ingles"]
        if re.search(r"Texto para os itens|no texto|do texto|ao texto|linha \d|trecho|correção gramatical|sentido original|reda[çc][ãa]o oficial|of[íi]cio|tipologia", cmd + " " + itens[:600], I):
            return ["basicos.lp"]
        if re.search(r"proposi[çc]|probabilidade|percentual|porcentagem|raz[ãa]o|propor[çc]|juros|n[úu]mero|equa[çc]|fun[çc][ãa]o|progress|conjunto|situa[çc][ãa]o hipot[ée]tica|l[óo]gica|combina|arranjo|m[ée]dia|tabela|gr[áa]fico", cmd + " " + itens[:400], I):
            return ["basicos.rlm"]
        if re.search(r"Windows|Excel|Word|navegador|correio eletr|Internet|nuvem|arquivo", cmd, I):
            return ["esp.tic.fundamentos"]  # Noções de Informática: no 407 só serve de apoio aos fundamentos
        return ["basicos.lp"]
    if ATUALIDADES.search(frase) and secao != "especificos":
        return []
    if OUTRO_CONSELHO.search(frase) and not re.search(r"COFEN|COREN|Enfermagem", frase, I):
        return []  # lei/resolução de outro conselho: não é edital do 407 (análogo à Lei 5.905, só como estilo)
    if secao == "complementares":
        return (_aplica(REGRAS_COMP, frase) or _aplica(REGRAS_COMP, itens))[:2]
    t = _aplica(REGRAS_ESP, frase) or _aplica(REGRAS_ESP, itens)
    return t[:3]
