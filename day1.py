import requests
from credentials import cookies_session_data
from collections import Counter

url = 'https://adventofcode.com/2024/day/1/input'
response = requests.get(url, cookies=cookies_session_data)

datas = response.text.split("\n")
datas.pop(-1) # There is an empty string at the end of the data

def data_prep(datas):
    l1, l2 = [], []
    for data in datas:
        l_data = data.split("   ")
        l1.append(int(l_data[0]))
        l2.append(int(l_data[1]))
    return l1, l2

def solve_part1(datas):
    l1, l2 = data_prep(datas)
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)

    res = 0
    for a, b in zip(l1_sorted, l2_sorted):
        res += abs(a - b)
    return res

def solve_part2(datas):
    l1, l2 = data_prep(datas)
    l2_counter = Counter(l2)

    res = 0
    for a in l1:
        res += a * l2_counter[a]
    return res

print("Solution 1: ", solve_part1(datas))
print("Solution 2: ", solve_part2(datas))
pass