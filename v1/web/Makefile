HTML = $(wildcard en/*.html)
EXTRAS = $(wildcard en/committers/*.html)
OTHER = $(wildcard en/*.css) \
        $(wildcard images/*.*) \
        $(wildcard images/*/*.*)

DST = ../../../tmp

install :
	mkdir -p ${DST}/en
	mkdir -p ${DST}/images
	python bin/tracking.py bin/tracking.js ${DST} ${HTML}
	tar zcf - ${EXTRAS} | (cd ${DST} && tar zxf -)
	tar zcf - ${OTHER} | (cd ${DST} && tar zxf -)
	find ${DST} -type f -exec chmod 644 {} \;
	find ${DST} -type d -exec chmod 755 {} \;
