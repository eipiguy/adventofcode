#!/usr/bin/env python3

class Crabs:
    def __init__(self, positions):
        largest = 0
        for x in positions:
            if x > largest:
                largest = x
        self.places = [0] * (largest+1)
        for x in positions:
            self.places[x] += 1
    def align(self, place):
        fuel = 0
        for i,x in enumerate(self.places):
            fuel += sum(range(abs(i-place)+1))*x
        return fuel

with open('input') as f:
    lines = [line.rstrip() for line in f.readlines()]

start = Crabs([ int(x) for x in lines[0].split(",") ])
#print(start.places)

cheapest_place = 0
least_fuel = start.align(0)
for i,x in enumerate(start.places):
    fuel_here = start.align(i)
    if fuel_here < least_fuel:
        cheapest_place = i
        least_fuel = fuel_here
    print(f"postition {i} = {fuel_here} fuel")

print(f"cheapest place = {cheapest_place}")
print(f"least fuel = {least_fuel}")
