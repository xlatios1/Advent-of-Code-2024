import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/8/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text.split("\n")
datas.pop(-1) # There is an empty string at the end of the data

map_data = [list(text) for text in datas]

testdata = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
testdatas = testdata.split("\n")
testdatas.pop(-1) # There is an empty string at the end of the data
testmap_data = [list(text) for text in testdatas]

def get_antinodes(a,b):
    res = [a[0]-b[0], a[1]-b[1]]
    return ((a[0]+res[0], a[1]+res[1]), (b[0]-res[0], b[1]-res[1]))

def get_vector(a,b):
    return b[0]-a[0], b[1]-a[1]

def find_antennas(map_data, start_row, start_col, tar):
    antennas = [[start_row, start_col]]
    temp_col = start_col+1
    for row in range(start_row,len(map_data)):
        for col in range(temp_col, len(map_data[row])):
            target = map_data[row][col]
            if target == tar:
                antennas.append([row, col])
        temp_col = 0
    return antennas

def solve_part1(map_data):
    visited = set()
    antinodes = set()
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            target = map_data[row][col]
            if target not in [".", "#"] and target not in visited:
                antennas = find_antennas(map_data, row, col, target)
                for id, antenna in enumerate(antennas):
                    for i in range(id+1, len(antennas)):
                        found_antinodes = get_antinodes(antenna, antennas[i])
                        for antinode in found_antinodes:
                            if 0 <= antinode[0] < len(map_data[0]) and 0 <= antinode[1] < len(map_data[0]):
                                antinodes.add(tuple(antinode))
                visited.add(target)
    return len(antinodes)

def solve_part2(map_data):
    visited = set()
    antinodes = set()
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            target = map_data[row][col]
            if target not in [".", "#"] and target not in visited:
                antennas = find_antennas(map_data, row, col, target)
                for id, antenna in enumerate(antennas):
                    antinodes.add(tuple(antenna))
                    for i in range(id+1, len(antennas)):
                        vector, scaler = get_vector(antenna, antennas[i]), 1
                        while 0 <= antenna[0]+(vector[0]*scaler) < len(map_data[0]) and 0 <= antenna[1]+(vector[1]*scaler) < len(map_data[0]):
                            antinodes.add((antenna[0]+(vector[0]*scaler), antenna[1]+(vector[1]*scaler)))
                            scaler += 1
                        
                        scaler = -1
                        while 0 <= antenna[0]+(vector[0]*scaler) < len(map_data[0]) and 0 <= antenna[1]+(vector[1]*scaler) < len(map_data[0]):
                            antinodes.add((antenna[0]+(vector[0]*scaler), antenna[1]+(vector[1]*scaler)))
                            scaler -= 1
    return len(antinodes)

print("Solution 1: ", solve_part1(testdatas))
print("Solution 1: ", solve_part1(map_data))
print("Solution 2: ", solve_part2(testdatas))
print("Solution 2: ", solve_part2(map_data))
pass