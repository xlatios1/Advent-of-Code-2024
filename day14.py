import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/14/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text.split("\n")
datas.pop()
map_boundary = (103, 101)
quadrant = (103//2, 101//2)

test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split('\n')
test_map_boundary = (7, 11)
test_quadrant = (7//2, 11//2)

def parse_data(input):
    data = []
    for robot in input:
        parts = robot.split(' ')
        p = tuple(map(int, parts[0][2:].split(',')))
        v = tuple(map(int, parts[1][2:].split(',')))
        data.append([[p[1], p[0]], [v[1], v[0]]])
    return data

def solve_part1(data, map_boundary, boundary, seconds):
    robots = parse_data(data)
    quadrants = [0,0,0,0]
    for p, v in robots:
        final_row = (p[0] + v[0] * seconds) % map_boundary[0]
        final_col = (p[1] + v[1] * seconds) % map_boundary[1]
        if final_row != boundary[0] and final_col != boundary[1]:
            if final_row < boundary[0] and final_col < boundary[1]: quadrants[0] += 1
            if final_row < boundary[0] and final_col > boundary[1]: quadrants[1] += 1
            if final_row > boundary[0] and final_col < boundary[1]: quadrants[2] += 1
            if final_row > boundary[0] and final_col > boundary[1]: quadrants[3] += 1
    return quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]

def solve_part2(data, map_boundary):
    robots = parse_data(data)
    for seconds in range(100000):
        curr_map = [[0]*map_boundary[1] for _ in range(map_boundary[0])]
        for p, v in robots:
            final_row = (p[0] + v[0] * seconds) % map_boundary[0]
            final_col = (p[1] + v[1] * seconds) % map_boundary[1]
            curr_map[final_row][final_col] = 1
        for row in range(len(curr_map)-1, -1, -1):
            cons = 0
            for col in range(len(curr_map[row])):
                if curr_map[row][col] == 1:
                    cons += 1
                elif cons > 10:
                    return seconds
                else:
                    cons = 0

# solve_part1(test_data, test_map_boundary, test_quadrant, 100)
print("Solution 1: ", solve_part1(datas, map_boundary, quadrant, 100))
print("Solution 2: ", solve_part2(datas, map_boundary))
pass