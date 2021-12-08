#!/usr/bin/env python3

CHILD = 8
BREED = 6

class Fish:
    def __init__(self, timers):
        self.fish = timers
    def tick(self):
        num_breed = self.fish.count(0)
        self.fish = [ BREED if x <= 0 else x-1 for x in self.fish ]
        self.fish.extend( [CHILD] * num_breed )

with open('input') as f:
    lines = [line.rstrip() for line in f.readlines()]

initial = Fish([ int(x) for x in lines[0].split(",") ])
print(f"initial = {initial.fish}")

days = 80
while days > 0:
    initial.tick()
    days -= 1

print(len(initial.fish))
