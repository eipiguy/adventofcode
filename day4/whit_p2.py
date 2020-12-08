import re

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

def get_field_data(field, record):
    fetch = re.search('{}:(\S+)'.format(field), record)
    return fetch.groups()[0]

n_valid = 0
for passport in passports:
    try:
        assert 1920 <= int(get_field_data('byr', passport)) <= 2002
        assert 2010 <= int(get_field_data('iyr', passport)) <= 2020
        assert 2020 <= int(get_field_data('eyr', passport)) <= 2030

        hgt = get_field_data('hgt', passport)
        hgt_val = int(hgt[:-2])
        hgt_unit = hgt[-2:]
        assert hgt_unit in ['in', 'cm']
        assert 150 <= hgt_val <= 193 if hgt_unit == 'cm' else 59 <= hgt_val <= 76

        assert re.search('(#[0-9a-fA-F]{6})', get_field_data('hcl', passport))
        assert get_field_data('ecl', passport) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        pid = get_field_data('pid', passport)
        assert len(pid) == 9  # regex will not catch entries >9 numbers, even with anchors
        assert (char in ['0','1','2','3','4','5','6','7','8','9'] for char in pid)
        
        n_valid += 1
    except:
        continue

print(n_valid)