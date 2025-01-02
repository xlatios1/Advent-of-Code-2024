import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/9/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text[:-1] + "0"

testdata = "2333133121414131402" + "0"

def get_map_part1(diskmap):
    arr = []
    for i in range(0, len(diskmap), 2):
        arr += [[i//2]]*int(diskmap[i]) 
        for i in range(int(diskmap[i+1])):
            arr += "."
    return arr

def get_map_part2(diskmap):
    arr = []
    for i in range(0, len(diskmap), 2):
        arr += [[[i//2]]*int(diskmap[i])] + [int(diskmap[i+1])]
    return arr

def solve_part1(diskmap):
    map_data = get_map_part1(diskmap)
    new_map_data = []
    l, r = 0, len(map_data)-1
    while l<=r:
        if map_data[l] != ".":
            new_map_data.append(map_data[l])
        else:
            while map_data[r] == ".":
                r-=1
            new_map_data.append(map_data[r])
            r -= 1
        l += 1
    return sum([id * num[0] for id, num in enumerate(new_map_data)])

def solve_part2(diskmap):
    map_data = get_map_part2(diskmap)
    i, target = len(map_data)-2, map_data[-2][0][0]
    while i > 0:
        shifted = False
        if isinstance(map_data[i], list) and map_data[i][0][0] == target:
            target -= 1
            _size = len(map_data[i])
            for j in range(i):
                if isinstance(map_data[j], int) and _size <= map_data[j]:
                    map_data[j] -= _size
                    map_data.insert(i+1, _size)
                    map_data.insert(j, map_data.pop(i))
                    shifted = True
                    i += 1
                    break
        if not shifted:
            i -= 1
    res = []
    for item in map_data:
        if isinstance(item, int):
            res += ["."]*item
        else:
            res += item
    return sum([id * num[0] for id, num in enumerate(res) if isinstance(num[0], int)])

# print("Solution 2: ", solve_part2(testdata))
print("Solution 1: ", solve_part1(datas))
print("Solution 2: ", solve_part2(datas))
pass


