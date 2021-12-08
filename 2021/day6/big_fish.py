#!/usr/bin/env python3

CHILD = 8
BREED = 6

class Fish:
    def __init__(self, timers):
        self.count = [0] * (CHILD + 2)
        for x in timers:
            self.count[x] += 1
    def tick(self):
        new = self.count[0]
        end = len(self.count) - 1
        for i,x in enumerate(self.count):
            if i < end:
                self.count[i] = self.count[i+1]
        self.count[BREED] += new
        self.count[CHILD] += new

with open('input') as f:
    lines = [line.rstrip() for line in f.readlines()]

initial = Fish([ int(x) for x in lines[0].split(",") ])
print(initial.count)

days = 256
while days > 0:
    initial.tick()
    days -= 1
    print(initial.count)

print()
print(initial.count)
print(sum(initial.count))
