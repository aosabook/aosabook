LATEX = pdflatex
BIBTEX = bibtex

CHAPTERS = \
	frontmatter \
	intro \
	asterisk \
	audacity \
	bash \
	bdb \
	cmake \
	eclipse \
	graphite \
	hdfs \
	integration \
	jitsi \
	llvm \
	mercurial \
	nosql \
	packaging \
	riak \
	selenium \
	sendmail \
	snowflock \
	socialcalc \
	telepathy \
	thousandparsec \
	violet \
	vistrails \
	vtk \
	wesnoth \
	makingsoftware \
  colophon

SRC=$(foreach name,${CHAPTERS},${name}.tex)

all : aosa.pdf

aosa.pdf : aosa.tex aosa.bib ${SRC}
	${LATEX} aosa
	${BIBTEX} aosa
	${LATEX} aosa
	${LATEX} aosa

ascii:
	@python ../bin/ascii.py ${SRC}

questions:
	@(for i in *.tex; do echo `fgrep aosaquestion $$i | wc -l` $$i; done) | sort -n -r

clean:
	@rm -f *.aux *.bak *.bbl *.blg *.log *.toc *~
