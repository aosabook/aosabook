LATEX = pdflatex
BIBTEX = bibtex

CHAPTERS = \
  frontmatter \
  frontmatterPDF \
	intro \
	distsys \
	ffreleng \
	freertos \
	gdb \
	ghc \
	git \
	gpsd \
	ironlang \
	itk \
	mailman \
	matplotlib \
	mediawiki \
	moodle \
	nginx \
	openmpi \
	oscar \
	pjs \
	puppet \
	pypy \
	sqlalchemy \
	twisted \
	yesod \
	yocto \
	zeromq \
	colophon

SRC=$(foreach name,${CHAPTERS},${name}.tex)

all : aosa2.pdf

aosa2.pdf : aosa2.tex aosa2.bib ${SRC}
	${LATEX} aosa2
	${BIBTEX} aosa2
	${LATEX} aosa2
	${LATEX} aosa2
	${LATEX} aosa2

forPDF : aosa2PDF.pdf

aosa2PDF.pdf : aosa2PDF.tex aosa2.bib ${SRC}
	${LATEX} aosa2PDF
	${BIBTEX} aosa2
	${LATEX} aosa2PDF
	${LATEX} aosa2PDF
	${LATEX} aosa2PDF

questions:
	@(for i in *.tex; do echo `fgrep aosaquestion $$i | wc -l` $$i; done) | sort -n -r

clean:
	@rm -f aosa2.pdf *.aux *.bak *.bbl *.blg *.log *.toc *~

cleanish:
	@rm -f *.aux *.bak *.bbl *.blg *.log *.toc *~
