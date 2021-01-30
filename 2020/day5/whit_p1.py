# AoC day 5
# goal - basically converts binary to base-10 (inb4 every base is base 10)
# approach - map the input into a binary string, then convert with the built-in int() method
#            sprinkle some arithmetic on top and we're good to go.

def map_chars_to_int(chars: str, charmap: list) -> int:
    """ Maps the characters in chars to a base-n string based on charmap; 
        The characters in charmap are mapped to their index in the list.
            map_chars_to_int('BA', ['a', 'b']) == 2 
            map_chars_to_int('BAA', ['a', 'b']) == 4 
    """
    char_lookup = {c.upper():str(i) for i, c in enumerate(charmap)}
    temp = ''.join(char_lookup[c.upper()] for c in chars)
    return int(temp, len(charmap))

# obey the testing goat
assert map_chars_to_int('BA', ['a','b']) == 2
assert map_chars_to_int('BAA', ['a','b']) == 4

def get_seat_id(seat_loc: str, split_idx: int = 7, mult: int = 8) -> int:
    """ Given a seat location, splits the string at the specified index and 
        uses each half to calculate the row and column for the seat.
        Per the prompt, the seat id = (row * mult) + column """
    row = map_chars_to_int(seat_loc[:split_idx], ['F','B'])  # front = 0, back = 1
    col = map_chars_to_int(seat_loc[split_idx:], ['L','R'])  # left = 0, right = 1
    return int((row * mult) + col)

seat_locations = []
with open('input.txt', 'r') as infile:
    for line in infile:
        temp = line.strip().upper()
        if len(temp) > 0:
            seat_locations.append(temp)

seat_ids = [get_seat_id(sl) for sl in seat_locations]  # separated so it can be used in pt 2

if __name__ == '__main__':
    print(max(seat_ids))   