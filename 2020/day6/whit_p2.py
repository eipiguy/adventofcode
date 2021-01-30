from collections import defaultdict

total = 0
with open('input.txt', 'r') as infile:
    group_vote = defaultdict(int)
    group_size = 0
    for line in infile.readlines():
        temp = line.strip().lower()
        if len(temp) > 0:
            group_size += 1
            for char in temp:
                group_vote[char] += 1
        else:  # new group, sum up everything with a vote count > group size
            for k in group_vote.keys():
                total += int(group_vote[k] == group_size)
                group_vote[k] = 0
            group_size = 0
    # fencepost  - thanks paul!
    for k in group_vote.keys():
        total += int(group_vote[k] == group_size)
        group_vote[k] = 0

print(total)