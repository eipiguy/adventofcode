#!/usr/bin/env python3

def parse_pt(token):
    return [ int(x) for x in token.split(",") ]

def parse_line(line):
    pt_tokens = line.split(" -> ")
    return [ parse_pt(token) for token in pt_tokens ]

with open('input') as f:
    lines = [line.rstrip() for line in f.readlines()]

grid = []

x_range = [ 0, 0 ]
y_range = [ 0, 0 ]

segments = []

for line in lines:
    pts = parse_line(line)

    if pts[0][0] < x_range[0]:
        x_range[0] = pts[0][0]
    if pts[1][0] < x_range[0]:
        x_range[0] = pts[1][0]
    
    if pts[0][0] > x_range[1]:
        x_range[1] = pts[0][0]
    if pts[1][0] > x_range[1]:
        x_range[1] = pts[1][0]
    
    if pts[0][1] < y_range[0]:
        y_range[0] = pts[0][1]
    if pts[1][1] < y_range[0]:
        y_range[0] = pts[1][1]

    if pts[0][1] > y_range[1]:
        y_range[1] = pts[0][1]
    if pts[1][1] > y_range[1]:
        y_range[1] = pts[1][1]

    segments.append(parse_line(line))

print(f"x range = {x_range}")
print(f"y range = {y_range}")
grid = [ [ 0 for i in range(y_range[1]+1) ] for j in range(x_range[1]+1) ]

for segment in segments:
    
    if segment[0][1] == segment[1][1]:
        
        if segment[0][0] < segment[1][0]:
            start = segment[0][0]
            end = segment[1][0]
        else:
            start = segment[1][0]
            end = segment[0][0]
       
        while start <= end:
            grid[start][segment[0][1]] += 1
            start += 1
    
    elif segment[0][0] == segment[1][0]:
        
        if segment[0][1] < segment[1][1]:
            start = segment[0][1]
            end = segment[1][1]
        else:
            start = segment[1][1]
            end = segment[0][1]
        
        while start <= end:
            grid[segment[0][0]][start] += 1
            start += 1

overlaps = 0
for col in grid:
    for row in col:
        if row > 1:
            overlaps += 1

print(overlaps)
