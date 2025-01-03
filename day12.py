import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/12/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text.split("\n")
datas.pop(-1)
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
    visited = [[False]*len(n) for n in map_data]
    res = 0
    map_w, map_h = len(map_data[0]) - 1, len(map_data) - 1
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            if not visited[row][col]:
                target = map_data[row][col]
                total_parameter = 0
                total_area = 0
                area = set([(row, col)])
                while area:
                    _row, _col = area.pop()
                    print(map_data[_row][_col], _row, _col)
                    visited[_row][_col] = True
                    total_area += 1
                    # check for exterior corners...
                    
                    # bottom - left
                    if _row == map_h and _col == 0: 
                        total_parameter += 1
                    elif _row == map_h and map_data[_row][_col-1] != target:
                        total_parameter += 1
                    elif _col == 0 and map_data[_row+1][_col] != target:
                        total_parameter += 1
                    elif _row < map_h and _col > 0 and map_data[_row+1][_col] != target and map_data[_row][_col-1] != target:
                        total_parameter += 1

                    # bottom - right
                    if _row == map_h and _col == map_w: 
                        total_parameter += 1
                    elif _row == map_h and map_data[_row][_col+1] != target:
                        total_parameter += 1
                    elif _col == map_w and map_data[_row+1][_col] != target:
                        total_parameter += 1
                    elif _row < map_h and _col < map_w and map_data[_row+1][_col] != target and map_data[_row][_col+1] != target:
                        total_parameter += 1
                    
                    # top - left
                    if _row == 0 and _col == 0:
                        total_parameter += 1
                    elif _row == 0 and map_data[_row][_col-1] != target: 
                        total_parameter += 1
                    elif _col == 0 and map_data[_row-1][_col] != target: 
                        total_parameter += 1
                    elif _row > 0 and _col > 0 and map_data[_row-1][_col] != target and map_data[_row][_col-1] != target: 
                        total_parameter += 1
                    
                    # top - right
                    if _row == 0 and _col == map_w:
                        total_parameter += 1
                    elif _row == 0 and map_data[_row][_col+1] != target: 
                        total_parameter += 1
                    elif _col == map_w and map_data[_row-1][_col] != target: 
                        total_parameter += 1
                    elif _row > 0 and _col < map_w and map_data[_row-1][_col] != target and map_data[_row][_col+1] != target: 
                        total_parameter += 1
                    
                    # check for interier corners...
                    if ((_row < map_h and _col > 0 and (map_data[_row+1][_col] == target and map_data[_row][_col-1] == target and map_data[_row+1][_col-1] != target))): # bottom - left
                        total_parameter += 1
                    if ((_row < map_h and _col < map_w and (map_data[_row+1][_col] == target and map_data[_row][_col+1] == target and map_data[_row+1][_col+1] != target))): # bottom - right
                        total_parameter += 1
                    if ((_row > 0 and _col > 0 and (map_data[_row-1][_col] == target and map_data[_row][_col-1] == target and map_data[_row-1][_col-1] != target))): # top - left
                        total_parameter += 1
                    if ((_row > 0 and _col < map_w and (map_data[_row-1][_col] == target and map_data[_row][_col+1] == target and map_data[_row-1][_col+1] != target))): # top - right
                        total_parameter += 1

                    for move in moves:
                        next_row, next_col = _row + move[0], _col + move[1]
                        if 0 <= next_row < len(map_data) and 0 <= next_col < len(map_data[row]) and map_data[next_row][next_col] == target and not visited[next_row][next_col]:
                            area.add((next_row, next_col))
                res += total_parameter*total_area
    return res

print("Solution 1: ", solve_part1(map_data))
print("Solution 2: ", solve_part2(map_data))
pass