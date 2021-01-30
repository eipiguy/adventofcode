with open('input.txt', 'r') as infile:
    field = [line.strip() for line in infile]

n_trees = 0
x, y, dx, dy = 0, 0, 3, 1

while y <= len(field) - 1:
    row = field[y]
    loc = row[x]
    if loc == '#':
        n_trees += 1
    y += dy
    x = (x + dx) % len(row)

print(n_trees)