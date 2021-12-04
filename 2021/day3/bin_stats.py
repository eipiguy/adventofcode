#!/usr/bin/env python3

f = open('input', 'r')

num_bits = 12

total = 0
num_zeros = [0] * num_bits

gamma = [0] * num_bits
gamma_num = 0

epsilon = [0] * num_bits
epsilon_num = 0

for line in f:
    total += 1
    for i, bit in enumerate(line):
        if bit=='0':
            num_zeros[i] += 1

half = total // 2
for i, n in enumerate(num_zeros):
    j = num_bits - 1 - i
    if n < half:
        gamma[i] = 1
        gamma_num += 2 ** j
    else:
        epsilon[i] = 1
        epsilon_num += 2 ** j

product = gamma_num * epsilon_num

print("total entries = " + str(total))
print("num_zeros = " + str(num_zeros))
print("gamma = " + str(gamma))
print("epsilon = " + str(epsilon))
print()
print("gamma_num = " + str(gamma_num))
print("epsilon_num = " + str(epsilon_num))
print("product = " + str(product))

f.close()
