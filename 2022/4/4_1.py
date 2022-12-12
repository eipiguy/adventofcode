import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'))

contained = 0
for line in f:
    intervals = line.rstrip().split(',')
    left = intervals[0].split('-')
    right = intervals[1].split('-')

    print(f"line ={line.rstrip()}")
    print(f"left = ({left[0]},{left[1]}), right = ({right[0]},{right[1]})")
    if left[0] <= right[0] and right[1] <= left[1]:
        contained += 1
        print(f"right contained in left")
        print(f"num contained = {contained}")
    elif right[0] <= left[0] and left[1] <= right[1]:
        contained += 1
        print(f"left contained in right")
        print(f"num contained = {contained}")

print(f"num contained = {contained}")