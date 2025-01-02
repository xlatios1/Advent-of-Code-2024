import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/4/input'
datas = requests.get(url, cookies=cookies_session_data).text.split("\n")
datas.pop(-1)

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")

test_map_data = [list(text) for text in test_data]
map_data = [list(text) for text in datas]

# X,Y
moves = [(0,-1), #up
         (0,1), #down
         (-1,0), #left
         (1,0), #right
         (-1,-1), #top-left
         (1,-1), #top-right
         (-1,1), #bottom-left
         (1,1)] #bottom-right

lateral_moves = [(-1,1), #bottom-left-direction
         (1,1)] #bottom-right-direction

def check_boundary(row, col, max_x, max_y, direction, boundary):
    if direction == 0: # UP
        return 3 <= row
    elif direction == 1: # DOWN
        return row <= max_y - boundary
    elif direction == 2: # LEFT
        return 3 <= col
    elif direction == 3: # RIGHT
        return col <= max_x - boundary
    elif direction == 4: # TOP-LEFT
        return 3 <= row and 3 <= col
    elif direction == 5: # TOP-RIGHT
        return 3 <= row and col <= max_x - boundary
    elif direction == 6: # BOTTOM-LEFT
        return row <= max_y - boundary and 3 <= col
    elif direction == 7: # BOTTOM-RIGHT
        return row <= max_y - boundary and col <= max_x - boundary

def check_lateral_boundary(row, col, max_x, max_y, boundary):
    return 3 <= row <= max_y - boundary and 3 <= col <= max_x - boundary

def solve_part1(map_data):
    max_x = len(map_data[0])
    max_y = len(map_data)
    res = 0
    
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            for direction, move in enumerate(moves):
                if check_boundary(row, col, max_x, max_y, direction, 4):
                    stack = ""
                    for i in range(4):
                        x, y = col + move[0] * i, row + move[1] * i
                        stack += map_data[x][y]
                    if stack == "XMAS":
                        res += 1
    return res

def solve_part2(map_data):
    res = 0
    
    for row in range(1, len(map_data)-1):
        for col in range(1, len(map_data[0])-1):
            is_x = [False, False]
            for id, lateral_move in enumerate(lateral_moves):
                stack = ""
                for i in range(-1, 2):
                    x, y = col + lateral_move[0] * i, row + lateral_move[1] * i
                    stack += map_data[x][y]
                if stack in ("MAS", "SAM"):
                    is_x[id] = True
            if all(is_x):
                res += 1
    return res

print("Solution 1: ", solve_part1(map_data))
print("Solution 2: ", solve_part2(map_data))

pass