import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'))

total_cals = 0
max_total = 0
for line in f:
    tokens = line.split()
    if len(tokens) != 0:
        total_cals += int(tokens[0])
    else:
        print(f"total calories = {total_cals}")
        if max_total < total_cals:
            max_total = total_cals
            print(f"max total calories = {max_total}")
        total_cals = 0

print(f"\nmax total calories = {max_total}")
