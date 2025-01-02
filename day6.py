import requests
from credentials import cookies_session_data
import copy

url = 'https://adventofcode.com/2024/day/6/input'
response = requests.get(url, cookies=cookies_session_data)

datas = response.text.split("\n")
datas.pop(-1) # There is an empty string at the end of the data
map_data_part_1 = [[i for i in text] for text in datas]
map_data_part_2 = [[i for i in text] for text in datas]

# X,Y
moves = [(0,-1), #up
         (1,0), #right
         (0,1), #down
         (-1,0), #left
         ]

testdata = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
testdatas = testdata.split("\n")
testdatas.pop(-1) # There is an empty string at the end of the data
testmap_data_1 = [list(text) for text in testdatas]
testmap_data_2 = [list(text) for text in testdatas]

def find_start_pos(map_data):
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == '^':
                return row, col

def calc_crosses(map_data):
    res = 0
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == 'X':
                res += 1
    return res

def solve_part1(map_data, row, col, cur_direction=0, part2=False):
    visited:set = set()
    while True:
        if not part2: map_data[row][col] = "X"
        next_row, next_col = row + moves[cur_direction][1], col + moves[cur_direction][0]

        if (0<=next_row<len(map_data) and 0<=next_col<len(map_data[0])):
            while map_data[row + moves[cur_direction][1]][col + moves[cur_direction][0]] == "#":
                cur_direction = (cur_direction+1) % 4
            row, col = row + moves[cur_direction][1], col + moves[cur_direction][0]
            if part2 and f"{row},{col},{cur_direction}" in visited:
                # print(f"Found, obstacle at: {start_row+moves[start_direction][1]},{start_col+ moves[start_direction][0]},{start_direction}")
                return True
            visited.add(f"{row},{col},{cur_direction}")
        else:
            if part2:
                # print(f"Exited at: {next_row} {next_row} {cur_direction}")
                return False
            else:
                return calc_crosses(map_data)

def solve_part2(map_data):
    (row, col), cur_direction = find_start_pos(map_data), 0
    start_row, start_col = row, col
    
    res = set()
    while True:
        next_row, next_col = row + moves[cur_direction][1], col + moves[cur_direction][0]

        if (0<=next_row<len(map_data) and 0<=next_col<len(map_data[0])):
            
            # Set the next valid direction
            while map_data[row + moves[cur_direction][1]][col + moves[cur_direction][0]] == "#":
                cur_direction = (cur_direction+1) % 4

            next_row, next_column = row + moves[cur_direction][1], col + moves[cur_direction][0]
            
            # part 2, set new map and obstacle
            map_data_copy = copy.deepcopy(map_data)
            map_data_copy[next_row][next_column] = "#"
            if (solve_part1(map_data_copy, start_row, start_col, 0, True)):
                res.add(f"{next_row},{next_column}")

            row, col = row + moves[cur_direction][1], col + moves[cur_direction][0]
        else:
            print(res)
            return len(res)
        # print(f"Moving... {row}-{col}-{cur_direction} = {map_data[row][col]}")

temp_row, temp_col = find_start_pos(testmap_data_1)
print("Solution 1: ", solve_part1(testmap_data_1, temp_row, temp_col))
temp_row, temp_col = find_start_pos(map_data_part_1)
print("Solution 1: ", solve_part1(map_data_part_1, temp_row, temp_col))

print("Solution 2: ", solve_part2(testmap_data_2))
print("Solution 2: ", solve_part2(map_data_part_2))

pass