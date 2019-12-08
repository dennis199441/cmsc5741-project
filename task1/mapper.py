import sys

for line in sys.stdin:
	if line.startswith("#"):
		line = line.replace("#", "")
	    categories = line.split()
	    for category in categories:
	        print('%s\t%s' % (category, 1))