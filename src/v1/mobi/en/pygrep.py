import sys

#==============================================================================
# hard-wired replacements
# Replace one string with another
str_rep = [\
    ['&#8942;', '|'],\
    ['&#9251;', '_'],\
    ['http://www.aosabook.org/en/', ''],\
    ]

#==============================================================================
# main
in_name = sys.argv[1]
out_name = sys.argv[2]
print 'Transforming from', in_name, 'to', out_name

in_file = file(in_name, 'r')
out_file = file(out_name, 'w')

for line in in_file:
    for one_str in str_rep:
        line = line.replace( one_str[0], one_str[1])
    out_file.write(line)

out_file.close()
in_file.close()

