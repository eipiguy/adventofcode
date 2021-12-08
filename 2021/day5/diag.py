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
       
        print(f"{segment} horizontal from ({start},{segment[1][1]})") 
        while start <= end:
            grid[start][segment[0][1]] += 1
            start += 1
        print(f"end = ({start-1},{segment[1][1]})")
    
    elif segment[0][0] == segment[1][0]:

        if segment[0][1] < segment[1][1]:
            start = segment[0][1]
            end = segment[1][1]
        else:
            start = segment[1][1]
            end = segment[0][1]
        
        print(f"{segment} vertical from ({segment[0][0]},{start})")
        while start <= end:
            grid[segment[0][0]][start] += 1
            start += 1
        print(f"end = ({segment[0][0]},{start-1})")


    elif segment[1][1]-segment[0][1] == segment[1][0]-segment[0][0]:

        if segment[0][0] < segment[1][0]:
            x = segment[0][0]
            end = segment[1][0]
            y = segment[0][1]
        else:
            x = segment[1][0]
            end = segment[0][0]
            y = segment[1][1]
        
        print(f"{segment} positive diagonal from ({x},{y})")
        while x <= end:
            grid[x][y] += 1
            x += 1
            y += 1
        print(f"end = ({x-1},{y-1})")

    elif segment[1][1]-segment[0][1] == segment[0][0]-segment[1][0]:

        if segment[0][0] < segment[1][0]:
            x = segment[0][0]
            end = segment[1][0]
            y = segment[0][1]
        else:
            x = segment[1][0]
            end = segment[0][0]
            y = segment[1][1]
        
        print(f"{segment} negative diagonal from ({x},{y})")
        while x <= end:
            grid[x][y] += 1
            x += 1
            y -= 1
        print(f"end = ({x-1},{y+1})")

    else:
        print("error")
        break

total = 0
zero = 0
one = 0
overlaps = 0
for row in grid:
    #print("".join([ str(n) if n>0 else "." for n in row[:200] ]))
    for col in row:
        total += 1
        if col > 1:
            overlaps += 1
        elif col == 1:
            one += 1
        else:
            zero += 1

print(f"x range = {x_range}")
print(f"y range = {y_range}")
print(f"total = {total}")
print(f"overlaps = {overlaps}")
print(f"ones = {one}")
print(f"zero = {zero}")
