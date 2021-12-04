#!/usr/bin/env python3

class Board:
    def __init__(self, rows):
        self.size = len(rows)
        self.board = []
        for row in rows:
            self.board.extend(row)
        self.called =  [False] * (self.size * self.size)

    def __call(self, n):
        for i, x in enumerate(self.board):
            if x==n:
                self.called[i] = True
        return
    
    def __check_rows(self):
        start_id = 0
        while start_id + self.size <= len(self.called):
            if False in self.called[start_id:start_id + self.size]:
                start_id += self.size
            else:
                return True
        return False
    
    def __check_cols(self):
        solved = False
        start_id = 0
        while start_id < self.size:
            i = start_id
            solved = True
            while i < len(self.called):
                if self.called[i]:
                    i += self.size
                else:
                    solved = False
                    break
            if solved:
                return True
            start_id += 1
        return False
    
    def __check_diags(self):

        return False
    
    def __checkSolved(self):
        if(     self.__check_rows() \
                or self.__check_cols() \
                or self.__check_diags() ):
            return True
        return False
    
    def uncalled(self):
        uncalled = []
        for i, x in enumerate(self.board):
            if not self.called[i]:
                uncalled.append(x)
        return uncalled

    def call_seq(self, sequence):
        for i, n in enumerate(sequence):
            self.__call(n)
            if(self.__checkSolved()):
                    return i
        return 0
    
def parse_boards(lines):
    boards = []
    cur_board = []
    for line in lines:
        if not line:
            boards.append(Board(cur_board))
            cur_board = []
            continue
        cur_board.append([ int(n) for n in line.split() ])
    return boards


with open('input') as f:
    lines = [line.rstrip() for line in f.readlines()]

sequence = [ int(x) for x in lines[0].split(',') ]
boards = parse_boards(lines[2:])

best_board = 0
fastest = len(sequence)

worst_board = 0
slowest = 0

for i,b in enumerate(boards):
    win = b.call_seq(sequence)
    if win < fastest:
        fastest = win
        best_board = i
    if win > slowest:
        slowest = win
        worst_board = i

print(f"best board id {best_board} wins on call {fastest}")
print()
print("uncalled numbers on fastest board")
print(f"{boards[best_board].uncalled()}")
uncalled_sum = sum(boards[best_board].uncalled())
product = uncalled_sum * sequence[fastest]
print()
print(f"sum of uncalled numbers = {uncalled_sum}, last call = {sequence[fastest]}")
print(f"product = {product}")
print()
print(f"slowest board id {worst_board} wins on call {slowest}")
print()
print("uncalled numbers on slowest board")
print(f"{boards[worst_board].uncalled()}")
uncalled_sum = sum(boards[worst_board].uncalled())
product = uncalled_sum * sequence[slowest]
print()
print(f"sum of uncalled numbers = {uncalled_sum}, last call = {sequence[slowest]}")
print(f"product = {product}")
