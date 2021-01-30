import re

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = []
buffer = ''
with open('input.txt', 'r') as infile:
    for line in infile:
        raw = line.strip()
        if len(raw) > 0:
            buffer = ' '.join([buffer, raw])
        else:
            passports.append(buffer)
            buffer = ''
passports.append(buffer)  # last row is NOT a newline so need to append final record

n_valid = 0
for passport in passports:
    val_fields = 0
    for field in req_fields:
        if re.search('{}:'.format(field), passport):
            val_fields += 1
    if val_fields == len(req_fields):
        n_valid += 1

print(n_valid)