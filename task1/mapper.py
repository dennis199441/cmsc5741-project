import sys

for line in sys.stdin:
    line = line.strip()
    labels = line.split()
    for label in labels:
        print('%s\t%s' % (label, 1))