import BeautifulSoup as b
import sys

fname = sys.argv[1]

soup = b.BeautifulSoup(open(fname).read().decode('utf-8'))

for table in soup.findAll('table'):
    headers = [h.string for h in table.findAll('th')]

    caption = [t for t in table.find('caption').contents]
    rows = table.findAll('tr')[1:] #ignore header
    row_cells = [row.findAll('td') for row in rows]
    field_values = [zip(headers, row) for row in row_cells]
    tmp = u"\n<li>\n<strong>{}</strong>: {}\n</li>\n"
    rendered_rows = [[tmp.format(field, " ".join(unicode(c) for c in value.contents)) for field, value in zcells] for zcells in field_values]
    print rendered_rows
    out = u"\n<br/>\n"
    captionstr = " ".join(str(t) for t in caption)
    print captionstr
    out += u"\n<p class='caption'>{}</p>".format(captionstr)
    out += u"\n<ul>\n"
    out += u"\n<li>&mdash;</li>\n".join([u"\n".join(rr) for rr in rendered_rows])
    out += u"\n</ul>\n"
    out += u"\n<br/>\n"
    table.replaceWith(out)

for bq in soup.findAll('blockquote'):
    emtag = u'<p><em>{}</em></p>'.format(bq)
    bq.replaceWith(emtag)
#    with open('bla.html', 'a') as w:
#        w.write(out.encode('utf-8'))

out = soup
with open(sys.argv[1], 'w') as w:
    w.write(str(out))
