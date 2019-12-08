import sys

current_category = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    category, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_category == category:
        current_count += count
    else:
        if current_category:
            print('%s\t%s' % (current_category, current_count))
        current_count = count
        current_categoty = category

if current_category == category:
    print('%s\t%s' % (current_category, current_count))
