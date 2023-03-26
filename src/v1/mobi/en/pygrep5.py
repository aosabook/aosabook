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
    if line.startswith('<p></p>'):
        line = '<p>&nbsp;</p>' + line[7:] 
    out_file.write(line)

out_file.close()
in_file.close()

