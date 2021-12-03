#!/usr/bin/env python3

f = open('input', 'r')

distance = 0
depth = 0
aim = 0
for line in f:
    tokens = line.split()
    direction = tokens[0]
    value = int(tokens[1])
    if direction == "forward":
        distance += value
        depth += aim * value
    elif direction == "up":
        aim -= value
    elif direction == "down":
        aim += value

print("distance = " + str(distance))
print("depth = " + str(depth))
print("product = " + str(distance * depth))

f.close()
