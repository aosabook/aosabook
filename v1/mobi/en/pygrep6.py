import sys
import os

#==============================================================================
# main
in_name = sys.argv[1]
out_name = in_name+'x'

os.system('mv '+in_name+' '+out_name)
print 'Transforming from', in_name, 'to', out_name

in_file = file(out_name, 'r')
out_file = file(in_name, 'w')

for line in in_file:
    if line.strip().startswith('<p>Figure&nbsp'):
        line = line.strip()
        line = '<em>'+line+'</em><p>&nbsp;</p>\n'
    if line.strip().startswith('<h3>'):
        line = line.strip()
        line = '<p>&nbsp;</p>'+line+'<p>&nbsp;</p>\n'
    if line.strip().startswith('<font size=1><pre>'):
        line = '<p>&nbsp;</p>'+line
    if line.strip().startswith('</pre></font>'):
        line = line.strip()
        line = line+'<p>&nbsp;</p>\n'
    out_file.write(line)

out_file.close()
in_file.close()

