#!/usr/bin/env bash
# Compila as figuras e, depois, os documentos da P3D (rodar de dentro de TEX/):
# os seis originais (ABNT) e as quatro alternativas "style2" (relatórios PT/EN no estilo
# do relatório da P2A; pôsteres PT/EN no estilo do pôster da P2A).
# Uso: bash compilar.sh            (tudo: figuras, docs e style2)
#      bash compilar.sh figuras    (só as figuras)
#      bash compilar.sh docs       (só os seis documentos originais; as figuras já devem estar em out/)
#      bash compilar.sh style2     (só as alternativas style2; as figuras já devem estar em out/)
#      bash compilar.sh limpar     (só apaga os auxiliares de out/; todos os modos limpam ao final)
# Os relatórios style2 são gerados dos originais por ferramentas/gerar_style2.py só se faltarem
# ou se o original for mais novo (para forçar: apague o *_style2.tex ou rode o script à mão);
# os pôsteres style2 são escritos à mão.
cd "$(dirname "$0")" || exit 1
mkdir -p out

figuras() {
  for f in figuras/*.tex; do
    echo ">> figura $f"
    pdflatex -output-directory=out -interaction=nonstopmode -halt-on-error "$f" > /dev/null || { echo "ERRO em $f (veja out/$(basename "${f%.tex}").log)"; exit 1; }
  done
}

compila() {
  for d in "$@"; do
    echo ">> documento $d (duas passagens)"
    for i in 1 2; do
      pdflatex -output-directory=out -interaction=nonstopmode -halt-on-error "$d.tex" > /dev/null || { echo "ERRO em $d (veja out/$d.log)"; exit 1; }
    done
  done
}

docs() {
  compila P3D_Privacidade2_Relatorio_PT P3D_Privacidade2_Report_EN \
          P3D_Privacidade2_Poster_PT P3D_Privacidade2_Poster_EN \
          P3D_Privacidade2_Licoes_PT P3D_Privacidade2_Lessons_EN
}

style2() {
  # Gera os relatórios style2 só se faltar algum ou se o original for mais novo que o style2
  # (assim edições à mão no style2 não são sobrescritas a cada compilação).
  precisa=0
  for base in P3D_Privacidade2_Relatorio_PT P3D_Privacidade2_Report_EN; do
    if [ ! -f "${base}_style2.tex" ] || [ "${base}.tex" -nt "${base}_style2.tex" ]; then precisa=1; fi
  done
  if [ "$precisa" = 1 ]; then
    PY="$(command -v python3 || command -v python)"
    if [ -n "$PY" ]; then
      echo ">> gerando os relatórios style2 a partir dos originais"
      "$PY" ferramentas/gerar_style2.py || { echo "ERRO em gerar_style2.py"; exit 1; }
    else
      echo "ERRO: faltam *_style2.tex (ou estão desatualizados) e python não foi encontrado"
      exit 1
    fi
  else
    echo ">> relatórios style2 já existem e estão em dia (nada a gerar)"
  fi
  compila P3D_Privacidade2_Relatorio_PT_style2 P3D_Privacidade2_Report_EN_style2 \
          P3D_Privacidade2_Poster_PT_style2 P3D_Privacidade2_Poster_EN_style2
}

# Apaga os auxiliares do LaTeX em out/ e deixa só os PDFs. Em caso de erro o script
# sai antes e NÃO limpa, para que o .log continue disponível.
limpar() {
  echo ">> limpando arquivos temporários de out/"
  find out -maxdepth 1 -type f \( -name '*.aux' -o -name '*.log' -o -name '*.out' -o -name '*.toc' \
    -o -name '*.lof' -o -name '*.lot' -o -name '*.fls' -o -name '*.fdb_latexmk' -o -name '*.synctex.gz' \
    -o -name '*.bbl' -o -name '*.blg' -o -name '*.nav' -o -name '*.snm' -o -name '*.vrb' \) -delete
}

case "${1:-tudo}" in
  figuras) figuras; limpar ;;
  docs) docs; limpar ;;
  style2) style2; limpar ;;
  limpar) limpar ;;
  *) figuras; docs; style2; limpar ;;
esac
echo "Pronto. PDFs em out/."
