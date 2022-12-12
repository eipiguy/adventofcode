import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'))

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0
parity = 0
history = []
for line in f:
    history.append(line.rstrip())
    if parity < 2:
        parity += 1
        continue 

    print(f"\n{history}")

    shared = []
    for i in history[0]:
        if i in history[1] and i in history[2] and i not in shared:
            shared.append(i)


    if len(shared) > 0:
        for i in shared:
            priority = abc.find(i) + 1
            sum += priority
            print(f"{shared} = {priority}")
            print(f"sum = {sum}")

    parity = 0
    history = []
