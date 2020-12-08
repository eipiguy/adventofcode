# AoC 2-2
# goal - given the previous input use the "lo" and "hi" as indexes to check that the given letter only appears
#   once (and ONCE ONLY) between those locations. note that in this schema the text's index ...starts at 1 >.<
# approach - very similar to p1
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
        lpos = text[lo-1]
        rpos = text[hi-1]
        if (char == lpos or char == rpos) and  lpos != rpos:
            valid_pw += 1
print(valid_pw)