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
    if line.strip().startswith('<h2'):
        line = '<p></p>'+line+'<p></p>'
    if line.strip().startswith('<h1'):
        line = '<p></p>'+line
    out_file.write(line)

out_file.close()
in_file.close()

