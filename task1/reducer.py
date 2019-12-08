import sys

current_label = None
current_count = 0
label = None

for line in sys.stdin:
    line = line.strip()
    label, count = line.split(" ", 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_label == label:
        current_count += count
    else:
        if current_label:
            print('%s\t%s' % (current_label, current_count))
        current_count = count
        current_label = label

if current_label == label:
    print('%s\t%s' % (current_label, current_count))