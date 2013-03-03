#!/bin/bash

DIR=`dirname "$1"`
FILE=`basename "$1"`

function pdf_latex() {
    pdflatex --interaction nonstopmode "$FILE.tex"
}

cd "$DIR"
rst2latex.py \
    --no-section-numbering --use-latex-footnotes --use-latex-citations \
    --use-latex-toc --language=pt_br --traceback \
    "$FILE" > "$FILE.tex"

pdf_latex
pdf_latex
rm -f "$FILE".{out,log,aux,tex,toc}

# --stylesheet-path=portugues.inc
