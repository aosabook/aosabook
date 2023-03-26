validate:
	@html5validator --root docs --ignore \
	'No space between attributes' \
	'The "align" attribute' \
	'The "cellpadding" attribute' \
	'The "width" attribute' \
	'An "img" element must have an "alt" attribute'
