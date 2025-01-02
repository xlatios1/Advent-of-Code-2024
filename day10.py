import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/10/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text.split("\n")
datas.pop()
data_map = [list(data) for data in datas]

test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split("\n")
test_data_map = [list(data) for data in test_data]

moves = [ # row, col
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1) # left
]

def find_trailheads(map_data, cur_row, cur_col, prev, part_one):
    total = set() if part_one else 0
    if 0 <= cur_row < len(map_data) and 0 <= cur_col < len(map_data[cur_row]):
        cur_val = int(map_data[cur_row][cur_col])
        if cur_val == prev + 1:
            if cur_val == 9:
                return [tuple([cur_row, cur_col])] if part_one else 1
            for move in moves:
                next_row, next_col = cur_row + move[0], cur_col + move[1]
                temp = find_trailheads(map_data, next_row, next_col, cur_val, part_one)
                if part_one:
                    total.update(temp)
                else:
                    total += temp
    return total

def solve_part(map_data, part_one):
    res = 0
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == "0":
                temp_res = find_trailheads(map_data, row, col, -1, part_one)
                res += len(temp_res) if part_one else temp_res
    return res

print("Solution 1: ", solve_part(test_data_map, True))
print("Solution 1: ", solve_part(data_map, True))
print("Solution 2: ", solve_part(test_data_map, False))
print("Solution 2: ", solve_part(datas, False))
pass