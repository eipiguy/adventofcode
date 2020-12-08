def check_slope(area: [], dx: int, dy: int) -> int:
    n, x, y = 0, 0, 0
    while y <= len(area) - 1:
        row = area[y]
        loc = row[x]
        if loc == '#':
            n += 1
        y += dy
        x = (x + dx) % len(row)
    return n

with open('input.txt', 'r') as infile:
    field = [line.strip() for line in infile]

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

product = 1
for (x, y) in slopes:
    trees = check_slope(area=field, dx=x, dy=y)
    product *= trees

print(product)