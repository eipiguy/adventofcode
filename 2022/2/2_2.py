import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'))

lose = 0
draw = 3
win = 6

points = [ lose, draw, win ]

score = 0

for line in f:
    print(f"\nscore = {score}")
    tokens = line.split()
    if len(tokens) < 1:
        continue

    match tokens[0]:
        case 'A':
            first = 1
        case 'B':
            first = 2
        case 'C':
            first = 3
    match tokens[1]:
        case 'X':
            second = (first-1)%3
            if second == 0:
                second = 3
        case 'Y':
            second = first
        case 'Z':
            second = (first%3)+1

    print(f"first = {first}, second = {second}")

    score += second
    if first == second:
        score += points[1]
    elif second == ((first%3)+1):
        score += points[2]
    else:
        score += points[0]

print(f"\nscore = {score}")