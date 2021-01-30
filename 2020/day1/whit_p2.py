# AoC 1-2
# goal - find triple that adds to 2020 and multiply those numbers
# approach - sort the list then use the two-pointer technique to find the matches 
# source^: https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
data = []
with open('input.txt', 'r') as infile:
    data.extend(int(x.strip()) for x in infile)
data.sort()
target = 2020
for i in range(len(data)-2):
    l = i + 1
    r = len(data) - 1
    while l < r:
        base = data[i]
        lo = data[l]
        hi = data[r]
        test = base + lo + hi
        if test == target:
            print(base, lo, hi, int(base*lo*hi))
            break
        elif test < target:
            l += 1
        elif test > target:
            r -= 1
        else:
            print("something went VERY wrong")