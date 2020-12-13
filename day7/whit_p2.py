# goal - find out how many bags must fit inside the specified bag based on
#        the mapping from part 1.

# we have to re-import since we ignored the number of contained bags earlier.
bag_map = {}  # {container : [(N, contained0), (M, contained1), ...]}
with open('input.txt', 'r') as infile:
    import re
    for line in infile.readlines():
        container = re.match('(\w+ \w+) bag', line).groups()[0]
        contained = [] if 'no other' in line else re.findall('([\d]?) (\w+ \w+) bag', line)
        bag_map[container] = contained

def get_bags_inside(target: str, mapping: dict) -> int:
    """does what it says on the tin"""
    total = 0
    for b in mapping[target]:
        total += int(b[0]) * (1 + get_bags_inside(b[1], bag_map))
    return total

print(get_bags_inside('shiny gold', bag_map))