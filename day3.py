import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/3/input'
datas = requests.get(url, cookies=cookies_session_data).text


def solve_part1(datas):
    res = 0
    for potential in datas.split("mul"):
        if potential and potential[0] == "(":
            inner_potential = potential.split(")")
            if len(inner_potential) > 1: #means got stuffs
                temp = inner_potential[0][1:].split(",")
                if len(temp) == 2:
                    try:
                        a, b = temp
                        res += int(a) * int(b)
                    except:
                        ...
    return res

def solve_part2(datas):
    res = 0
    for idx, ignores in enumerate(datas.split("don't()")):
        if idx == 0:
            res += solve_part1(ignores)
        else:
            potentials = ignores.split("do()", maxsplit=1)
            if len(potentials) > 1:
                res += solve_part1(potentials[1])
    return res

print("Solution 1: ", solve_part1(datas))
print("Solution 2: ", solve_part2(datas))

pass
