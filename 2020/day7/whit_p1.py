import re

bag_map = {}
patt = '(\w+ \w+) bag'  # thank you pythex.org!

with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        bags = re.findall(patt, line)
        container = bags[0]
        contained = [] if bags[-1] == 'no other' else bags[1:]
        bag_map[container] = contained
        
def get_valid_containers(targets: set, container_map: dict) -> set:
    res = set()
    for t in targets:
        res.update([k for k in container_map if t in container_map[k]])
    if all(r in targets for r in res):
        return res
    return get_valid_containers(targets.union(res), container_map)

valid_containers = get_valid_containers({'shiny gold'}, bag_map)

if __name__ == '__main__':
    print(len(valid_containers))
