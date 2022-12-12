import os

def topVals(value, list):
    for i, item in enumerate(list):
        if item < value:
            if i+1 < len(list):
                list[i+1] = list[i]
            list[i] = value
            return list
    return list    

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'))

total_cals = 0
top_cals = [ 0, 0, 0 ]
for line in f:
    tokens = line.split()
    if len(tokens) != 0:
        total_cals += int(tokens[0])
    else:
        print(f"total calories = {total_cals}")
        top_cals = topVals(total_cals, top_cals)
        total_cals = 0
        print(f"top total calories = {top_cals}")

print(f"sum = {sum(top_cals)}")
