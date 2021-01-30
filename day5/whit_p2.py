from whit_p1 import seat_ids

seat_ids.sort()
for i in range(len(seat_ids)-2):
    a = seat_ids[i]
    b = seat_ids[i+1]
    if b - a == 2:
        print(a+1)
        break
