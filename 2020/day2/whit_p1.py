# AoC 2-1
# goal - make sure the specified letter shows up the appropriate amount of times and return the count of valid pw's
# approach - self explanatory? see below
import re
valid_pw = 0
pattern = '(\d+)-(\d+)\s(\w+?):\s(\w+)'
with open('input.txt', 'r') as infile:
    for line in infile:
        regex = re.search(pattern, line.strip())
        caps = regex.groups()
        lo = int(caps[0])
        hi = int(caps[1])
        char = caps[2]
        text = caps[3]
        test = text.count(char)
        if lo <= test <= hi:
            valid_pw += 1
print(valid_pw)