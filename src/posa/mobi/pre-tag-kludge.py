from IPython import get_ipython
import sys
import BeautifulSoup as b
with open(sys.argv[1]) as f:
    soup = b.BeautifulSoup(f.read())

for pre in soup.findAll('pre'):
    open('bla.txt', 'w').write(str(pre))
    nf = get_ipython().getoutput(u'pandoc bla.txt -f html -t markdown | head -n -1 | tail -n +2')
    new = "\n\n".join(u'<p><code>{}</code></p>'.format(f.replace('>', '&gt;').replace('<', '&lt;')) for f in nf)
    pre.replaceWith(new)
#    open('bla2.txt', 'w').write(new)
#    nf = get_ipython().getoutput(u'pandoc -f markdown -t html bla2.txt')
#    print "\n".join(nf)
#    pre.replaceWith("\n".join(l for l in nf))

with open(sys.argv[1], 'w') as f:
    f.write(str(soup))
