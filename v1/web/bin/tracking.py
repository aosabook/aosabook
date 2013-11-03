#!/usr/bin/env python

'''Insert tracking scripts into HTML pages.
Usage: tracking.py tracking.js output_dir 1.html 2.html ... < tracking.js'''

import sys, os

def read_file(filename):
    reader = open(filename, 'r')
    data = reader.read()
    reader.close()
    return data

def write_file(filename, content):
    writer = open(filename, 'w')
    writer.write(content)
    writer.close()

assert len(sys.argv) >= 3, 'Usage: tracking.py tracking.js output_dir files...'

to_insert = read_file(sys.argv[1])

output_dir = sys.argv[2]
assert os.path.isdir(output_dir), 'Second argument not a directory'

for filename in sys.argv[3:]:
    content = read_file(filename)
    pos = content.find('</head>')
    assert pos >= 0, '%s does not contain </head>' % filename
    content = content[:pos] + '\n' + to_insert + '\n' + content[pos:]
    output_filename = os.path.join(output_dir, filename)
    write_file(output_filename, content)
