LATEX = pdflatex
BIBTEX = bibtex
PANDOC = pandoc -S --chapters --highlight-style=kate

CHAPTERS = \
  frontmatter \
	intro \
	chrome \
	dance \
	ethercalc \
	infinispan \
	khmer \
	memshrink \
	mobile-perf \
	ninja \
	pugixml \
	talos \
	warp \
	zotonic \
	colophon

SRC=$(foreach name,${CHAPTERS},${name}.tex)

MDCHAPTERS = \
  pugixml \
  ethercalc \
  talos \
  warp

MDSRC=$(foreach name,${MDCHAPTERS},${name}.markdown)

MDS : ${SRC} ${MDSRC}
	$(foreach name,${MDCHAPTERS},${PANDOC} -o ${name}.tex ${name}.markdown;)

all : posa.pdf MDS

posa.pdf : posa.tex posa.bib ${SRC}
	${LATEX} posa
	${BIBTEX} posa
	${LATEX} posa
	${LATEX} posa
	${LATEX} posa

forPDF : posaPDF.pdf

posaPDF.pdf : posaPDF.tex posa.bib ${SRC}
	${LATEX} posaPDF
	${BIBTEX} posa
	${LATEX} posaPDF
	${LATEX} posaPDF
	${LATEX} posaPDF

questions:
	@(for i in *.tex; do echo `fgrep aosaquestion $$i | wc -l` $$i; done) | sort -n -r

clean:
	@rm -f posa.pdf *.aux *.bak *.bbl *.blg *.log *.toc *~

cleanish:
	@rm -f *.aux *.bak *.bbl *.blg *.log *.toc *~
