# goal: given a series of instructions, execute them and return a global value
#       at the moment an instruction is executed twice

with open('input.txt','r') as infile:
    instructions = [line.strip() for line in infile.readlines()]

position = 0
accumulator = 0
execution_log = []  # list of positions already executed on

while position < len(instructions):
    if position in execution_log:  # first double-execution is what we want
        print(accumulator)
        break
    execution_log.append(position)
    operation, argument = instructions[position].split(' ')
    print(position, accumulator, operation, argument)
    accumulator += int(argument) if operation == 'acc' else 0
    position += int(argument) if operation == 'jmp' else 1