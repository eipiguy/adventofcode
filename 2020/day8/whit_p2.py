# goal: in the list of instructions, find the jmp OR nop that needs to be swapped
#       such that the program will attempt to execute instruction Z + 1

with open('input.txt','r') as infile:
    instructions = [line.strip() for line in infile.readlines()]

position = 0
accumulator = 0
execution_log = []
backup = {
    'position': position,
    'accumulator': accumulator,
    'execution_log': execution_log.copy()  # here's 4 hours of your life back: lists are immutable
}
flipped_run = False
resetting = False
while position < len(instructions):
    if position in execution_log:  # first double-execution is what we want
        print('ERROR', position, flipped_run)
        if not flipped_run:
            print('FATAL ERROR', execution_log)
            break
        print('RESTORE', backup)
        position = backup['position']
        accumulator = backup['accumulator']
        execution_log = backup['execution_log']
        flipped_run = False
        resetting = True
        continue
    operation, argument = instructions[position].split(' ')
    if operation in ['jmp', 'nop'] and not flipped_run and not resetting:
        print('FLIP', position, operation)
        backup = {
            'position': position,
            'accumulator': accumulator,
            'execution_log': execution_log.copy()
        }
        operation = 'jmp' if operation == 'nop' else 'nop'
        flipped_run = True
    else:
        resetting = False
    execution_log.append(position)
    print('EXE', position, operation, argument, flipped_run, backup['position'])
    accumulator += int(argument) if operation == 'acc' else 0
    position += int(argument) if operation == 'jmp' else 1

print(accumulator)