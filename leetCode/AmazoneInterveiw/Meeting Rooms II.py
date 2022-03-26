def way1(intervals):
    curr = sorted(intervals, key=lambda x:x[0])
    print(curr)

    all_rooms = []

    for room in curr:
        if len(all_rooms) == 0:
            all_rooms.append(room)
        else:
            flag = False
            for i in range(len(all_rooms)):

                if all_rooms[i][1]<=room[0]:
                    all_rooms[i] = room
                    flag = True
                    break
            if not flag:
                all_rooms.append(room)
        print(all_rooms)

    return len(all_rooms)


def way2(intervals):
    room_dict = {}
    for b,e in intervals:
        if b in room_dict:
            room_dict[b] += 1
        else:
            room_dict[b] = 1
        if e in room_dict:
            room_dict[e] -= 1
        else:
            room_dict[e] = -1

    max_room = 0
    cur_room = 0
    for t in sorted(room_dict.keys()):
        cur_room += room_dict[t]
        max_room = max(cur_room,max_room)
    return max_room

intervals = [[0,30],[5,10],[15,20]]
# intervals = [[7,10],[2,4]]
# intervals = [[1,5],[8,9],[8,9]]
# intervals = [[300, 5870], [518, 2918], [848, 3846], [1293, 2986], [4284, 5907], [4466, 4781]]

print(way2(intervals))