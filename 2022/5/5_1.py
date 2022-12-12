import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'))


crates = []
instructions = []
at_instructions = False
num_to_move = 0
origin = 0
destination = 0

####
# Parse
####
for line in f:
    if line.rstrip()=="":
        at_instructions = True
    # Crate Data
    elif not at_instructions:
        crates.append([])
        for i in range(len(line)):
            if i%4 == 1:
                crates[-1].append(line[i])
    # Instructions
    else:
        line_split = line.rstrip().split(' from ')
        num_to_move = int(line_split[0][5:])
        locations = line_split[1].split(' to ')
        origin = int(locations[0])-1
        destination = int(locations[1])-1
        instructions.append([num_to_move, origin, destination])

####
# Organize
####
stacks = []
for i in crates[-1]:
    stacks.append([])

# Row major to column major order
for level in reversed(crates):
    for column, content in enumerate(level):
        if not content==" ":
            stacks[column].append(content)

# Strip initial number
for i,column in enumerate(stacks):
    stacks[i] = column[1:]

print(stacks)
print(instructions)

####
# Perform Instructions
####

for command in instructions:
    for crate_num in range(int(command[0])):
        stacks[command[2]].append(stacks[command[1]].pop())

print(stacks)