# AoC 1-1
# goal - find pair in the input that sums to 2020 then multiply those numbers
# approach - read data into a dict of {compliment : data} such that if data matches an existing key that's
#   equal to 2020 and we can begin the multiplication.
data = {}
with open('input.txt', 'r') as infile:
    for line in infile:
        num = int(line.strip())
        if num in data.keys():
            print(num, data[num], num*data[num])
            break
        idx = int(2020-num)
        data[idx] = num