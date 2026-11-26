---
id: crf_pr_2025_analista_sistemas_b16
orgao: "CRF-PR"
ano: 2025
banca: quadrix
cargo: "Analista de Sistemas"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.infra
itens: 81-85
aderencia: media
fonte:
  path: acervo/fontes/crf_pr_2025_analista_sistemas/prova.pdf
  gabarito: acervo/fontes/crf_pr_2025_analista_sistemas/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. Item 11: alterado para “C” (certo). / Itens 12, 60 e 68: anulados."
---

## Comando

Acerca da virtualização e dos contêineres, julgue os itens a seguir.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 81 | Em clusters Proxmox configurados com Ceph Storage, a perda simultânea de dois nós monitores (MON) não impacta a disponibilidade do cluster, pois o Ceph mantém quórum automaticamente, independentemente do número total de monitores configurados. | E |
| 82 | A utilização de PCI Passthrough (VFIO) em ambientes KVM permite que uma placa física seja compartilhada simultaneamente por múltas máquinas virtuais, garantindo desempenho nativo e isolamento completo entre VMs. | E |
| 83 | No Proxmox VE, a funcionalidade de Live Migration depende, obrigatoriamente, do uso de armazenamento compartilhado (como NFS, iSCSI ou Ceph) ou de discos replicados, pois o estado do disco virtual precisa estar acessível simultaneamente ao nó de origem e ao nó de destino. | C |
| 84 | O KVM utiliza virtualização total com base em extensões de hardware (Intel VT-x e AMD-V) e, diferentemente de contêineres, requer um sistema operacional convidado completo, o que implica maior sobrecarga de recursos quando comparado ao LXC. | C |
| 85 | Em ambientes Docker executados sobre hosts Proxmox, a criação de múltiplas redes bridge no Docker elimina a necessidade de configuração de VLANs no switch físico, pois o isolamento lógico fornecido pelo Docker substitui completamente a segmentação de rede em nível de infraestrutura. | E |
