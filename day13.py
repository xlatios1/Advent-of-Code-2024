import requests
from credentials import cookies_session_data
import numpy as np

url = 'https://adventofcode.com/2024/day/13/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text.split("\n")
datas.pop()

test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split("\n")


def parsed_data(datas, addition=0):
    i = 0
    res = []
    while i < len(datas):
        split_data_a = datas[i].split(" ")
        ax = split_data_a[2][2:][:-1]
        ay = split_data_a[3][2:]

        split_data_b = datas[i+1].split(" ")
        bx = split_data_b[2][2:][:-1]
        by = split_data_b[3][2:]
        
        rewards = datas[i+2].split(" ")
        rx = rewards[1][2:][:-1]
        ry = rewards[2][2:]

        res.append([(int(ax), int(ay), 3), (int(bx), int(by), 1), (int(rx)+addition, int(ry)+addition)])
        i += 4
    return res

def tabulate(a, opt_a:int, b, opt_b:int, target):
    return a[0] * opt_a + b[0] * opt_b == target[0] and a[1] * opt_a + b[1] * opt_b == target[1]

def find_optimal_cost(a, b, prize):
    ax, ay, acost = a
    bx, by, bcost = b
    rx, ry = prize
    
    opt = rx // bx if rx // bx < ry // by else ry // by
    if (bx*opt == rx and by*opt == ry):
        return opt
    else:
        i = opt
        while i > 0:
            remaining_x = rx - bx*i # 6640
            remaining_y = ry - by*i # 40
            if remaining_y > remaining_x:
                if remaining_y % ay == 0:
                    opt_a = remaining_y // ay
                    if tabulate(a, opt_a, b, i, prize):
                        return opt_a * acost + i * bcost
            else:
                if remaining_x % ax == 0:
                    opt_a = remaining_x // ax
                    if tabulate(a, opt_a, b, i, prize):
                        return opt_a * acost + i * bcost
            i -= 1
        return -1

    
def solve_part1(input):
    res = 0
    datas = parsed_data(input)
    for a,b,prize in datas:
        r = find_optimal_cost(a,b,prize)
        if r!= -1:
            res += r
    return res
    
def solve_part2(input, addition):
    res = 0
    datas = parsed_data(input, addition)
    for a,b,prize in datas:
        A = np.array([[a[0], b[0]], [a[1], b[1]]])
        B = np.array(prize)
        x = np.linalg.solve(A, B)
        if round(x[0], 1) % 1 == 0 and round(x[1], 1) % 1 == 0:
            res += round(x[0],0)*3 + round(x[1],0)
    return int(res)

print("Solution 1: ", solve_part1(datas))
print("Solution 2: ", solve_part2(datas, 10000000000000))
pass

