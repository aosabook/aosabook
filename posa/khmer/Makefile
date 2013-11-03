ifeq ($(shell which convert 2>/dev/null),)
CONVERT = echo
else
CONVERT = convert
endif

FIG_PNGS = data_flow.png kmers.png layers.png
FIG_PDFS = data_flow.pdf kmers.pdf layers.pdf

all: $(FIG_PDFS)
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex
	pdflatex main.tex

pandoc: $(FIG_PNGS)
	sed -i 's|pdf|png|' khmer.markdown
	pandoc -o khmer.pdf khmer.markdown

clean:
	-rm -f *.aux *.log *.bbl *.blg *.dvi *.pdf 

%.pdf: %.eps
	$(CONVERT) $< $@

%.png: %.eps
	$(CONVERT) $< $@

# vim: set ft=make tw=79:
