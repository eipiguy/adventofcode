# read in groups of letters, count how many unique letters are in each group,
# and then multiply the count of unique letters for a final sum.
groups = []
with open('input.txt', 'r') as infile:
    buffer = None
    for line in infile.readlines():
        temp = line.strip().lower()
        if len(temp) > 0:
            if not buffer:
                buffer = set()
            buffer.update(temp)
        else:
            groups.append(buffer)
            buffer = None
    buffer.update(temp)
    groups.append(buffer)

print(sum(len(g) for g in groups))
