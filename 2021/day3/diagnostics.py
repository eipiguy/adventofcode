#!/usr/bin/env python3



def ox_filter(lines, bit):
    keep = []
    num_zeros = 0
    most = 1
    
    for line in lines:
        if line[bit] == "0":
            num_zeros += 1

    if num_zeros > (len(lines) // 2):
        most = 0

    for i, line in enumerate(lines):
        if int(line[bit]) == most:
            keep.append(i)

    return keep

def ox(lines):
    bit = 0
    keep = list(range(len(lines)))

    while len(lines) > 1:
        keep = ox_filter(lines, bit)
        lines = [ lines[i] for i in keep ]
        bit += 1

    return lines[0]

def co2_filter(lines, bit):
    keep = []
    num_ones = 0
    most = 0
    
    for line in lines:
        if line[bit] == "1":
            num_ones += 1

    if num_ones < (len(lines) // 2):
        most = 1

    for i, line in enumerate(lines):
        if int(line[bit]) == most:
            keep.append(i)

    return keep

def co2(lines):
    bit = 0
    keep = list(range(len(lines)))

    while len(lines) > 1:
        keep = co2_filter(lines, bit)
        lines = [ lines[i] for i in keep ]
        bit += 1

    return lines[0]

with open('input') as f:
    lines = [line.rstrip() for line in f.readlines()]

product = int(ox(lines),2) * int(co2(lines),2)

print("product = " + str(product))
