import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/2/input'
datas = requests.get(url, cookies=cookies_session_data).text.split("\n")
datas.pop(-1)

test_datas = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split("\n")

edge_data = """48 46 47 49 51 54 56
1 1 2 3 4 5
1 2 3 4 5 5
5 1 2 3 4 5
1 4 3 2 1
1 6 7 8 9
1 2 3 4 3
9 8 7 6 7
7 10 8 10 11
29 28 27 25 26 25 22 20""".split("\n")

def conditions(prev, curr, is_asc):
    if is_asc:
        diff = curr - prev
        return prev < curr and 1 <= diff <= 3
    else:
        diff = prev - curr
        return prev > curr and 1 <= diff <= 3

def solve_part1(datas):
    res = 0
    for levels in datas:
        safe = True
        levels_data = levels.split(" ")
        is_asc = int(levels_data[-1]) - int(levels_data[0]) > 0
        for pos in range(1, len(levels_data)):
            prev, cur = int(levels_data[pos-1]),  int(levels_data[pos])
            if conditions(prev, cur, is_asc):
                continue
            else:
                safe = False
                break
        if safe: 
            res += 1
    return res

def solve_part2(datas):
    def solve(_levels_data):
        is_asc = int(_levels_data[-1]) - int(_levels_data[0]) > 0
        tolerance = True
        pos = 1
        while pos < len(_levels_data):
            prev, cur = int(_levels_data[pos-1]), int(_levels_data[pos])
            if not conditions(prev, cur, is_asc):
                if tolerance:
                    if pos+1 < len(_levels_data):
                        jump = int(_levels_data[pos+1])
                        tolerance = False
                        print("Attempt: ", conditions(prev, jump, is_asc), " ", conditions(cur, jump, is_asc), " ", _levels_data, prev, cur, jump)
                        if pos == 1:
                            is_asc = int(_levels_data[-1]) - int(_levels_data[1]) > 0
                            if not conditions(cur, jump, is_asc):
                                return False
                        elif not conditions(prev, jump, is_asc):
                            return False
                        pos += 1
                else:
                    print(prev, cur, jump, is_asc)
                    return False
            pos += 1
        return True

    res = 0
    for levels in datas:
        levels_data = levels.split(" ")
        if solve(levels_data):
            res += 1
        else:
            r2 = levels.split(" ")
            r2.reverse()
            if solve(r2):
                res += 1
            else:
                print("Failed on")
                print(r2)
    return res

print("Solution 1: ", solve_part1(datas))
print("Solution 2: ", solve_part2(datas))
# print("Solution 2: ", solve_part2(test_datas))

pass