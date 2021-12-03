#!/usr/bin/env python3

f = open('input', 'r')

num_increases = -3;
llast = 0
last = 0
last_total = 0
for line in f:
    num = int(line)
    total = num + last + llast
    if total > last_total:
        num_increases += 1
    last_total = total
    llast = last
    last = num

print(num_increases)

f.close()
