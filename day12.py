import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/12/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text.split("\n")
map_data = [list(data) for data in datas]

moves = [#row, col
    (-1, 0), # Up,
    (0, 1), # Right,
    (1, 0), # Down,
    (0, -1) # Left,
]

test_data = """AAAA
BBCD
BBCC
EEEC""".split("\n")
test_map_data = [list(data) for data in test_data]

test_data_2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""".split("\n")
test_map_data_2 = [list(data) for data in test_data_2]

def traverse_parameter(map_data, row, col, target, temp_set):
    if (row, col) not in temp_set:
        if 0 <= row < len(map_data) and 0 <= col < len(map_data[row]) and map_data[row][col] == target:
            temp_set.add((row, col))
            res = 0
            for move in moves:
                next_row, next_col = row + move[0], col + move[1]
                res += traverse_parameter(map_data, next_row, next_col, target, temp_set)
            return res
        else:
            return 1
    else:
        return 0

def solve_part1(map_data):
    visited = set()
    regions = []

    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            if (row, col) not in visited:
                target = map_data[row][col]
                temp_area = set()
                regions.append([target, traverse_parameter(map_data, row, col, target, temp_area), len(temp_area)])
                visited.update(temp_area)
        
    return sum([r[1]*r[2] for r in regions])

def solve_part2(map_data):
    ...


print("Solution 1: ", solve_part1(map_data))
print("Solution 2: ", solve_part2(map_data))
pass