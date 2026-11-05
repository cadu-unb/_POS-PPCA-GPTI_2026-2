#!/usr/bin/env bash
# Compila as figuras e, depois, os seis documentos da P3D (rodar de dentro de TEX/).
# Uso: bash compilar.sh            (tudo)
#      bash compilar.sh figuras    (só as figuras)
#      bash compilar.sh docs       (só os documentos; as figuras já devem estar em out/)
cd "$(dirname "$0")" || exit 1
mkdir -p out

figuras() {
  for f in figuras/*.tex; do
    echo ">> figura $f"
    pdflatex -output-directory=out -interaction=nonstopmode -halt-on-error "$f" > /dev/null || { echo "ERRO em $f (veja out/$(basename "${f%.tex}").log)"; exit 1; }
  done
}

docs() {
  for d in P3D_Privacidade2_Relatorio_PT P3D_Privacidade2_Report_EN \
           P3D_Privacidade2_Poster_PT P3D_Privacidade2_Poster_EN \
           P3D_Privacidade2_Licoes_PT P3D_Privacidade2_Lessons_EN; do
    echo ">> documento $d (duas passagens)"
    for i in 1 2; do
      pdflatex -output-directory=out -interaction=nonstopmode -halt-on-error "$d.tex" > /dev/null || { echo "ERRO em $d (veja out/$d.log)"; exit 1; }
    done
  done
}

case "${1:-tudo}" in
  figuras) figuras ;;
  docs) docs ;;
  *) figuras; docs ;;
esac
echo "Pronto. PDFs em out/."
