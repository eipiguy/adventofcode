import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'))

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0
for line in f:
    shared = []
    line = line.rstrip()

    print(f"\n{line}")

    n = len(line) // 2
    if len(line) == 0:
        continue

    first = line[0:n]
    second = line[n:]
    print(f"{first} {second}")

    for i in first:
        if i in second and i not in shared:
                shared.append(i)

    if len(shared) > 0:
        for i in shared:
            priority = abc.find(i) + 1
            sum += priority
            print(f"{shared} = {priority}")
            print(f"sum = {sum}")
