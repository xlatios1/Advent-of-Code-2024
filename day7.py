import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/7/input'
response = requests.get(url, cookies=cookies_session_data)
datas = response.text.split("\n")
datas.pop(-1) # There is an empty string at the end of the data

test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
test_datas = test_data.split("\n")
def evaluate_left_to_right(data:str)->int:
    res = 0
    last_operation = "+"
    temp = ""
    for c in data + "+":
        if c.isdigit():
            temp += c
        else:
            if last_operation == "+":
                res += int(temp)
            elif last_operation == "*":
                res *= int(temp)
            else:
                res = int(f'{res}{temp}')
            last_operation = c
            temp = ""
    return res

def build(target:int, equation:list, part_2:bool):
    if len(equation) == 1:
        # if (evaluate_left_to_right(equation[0]) == target):
        #     print(equation, target)
        #     return True
        # else:
        #     return False
        return evaluate_left_to_right(equation[0]) == target
    
    temp_equation = [i for i in equation]
    a = temp_equation.pop(0)
    b = temp_equation.pop(0)
    new_equation1 = [f"{a}*{b}"] + temp_equation
    new_equation2 = [f"{a}+{b}"] + temp_equation
    if part_2:
        new_equation3 = [f"{a}|{b}"] + temp_equation
        return build(target, new_equation1, part_2) or build(target, new_equation2, part_2) or build(target, new_equation3, part_2)
    else:
        return build(target, new_equation1, part_2) or build(target, new_equation2, part_2)
    

def solve_part1(rows, is_part2:bool):
    res = 0
    for row in rows:
        items = row.split(" ")
        result, item = int(items[0][:-1]), items[1:]

        if build(result, item, is_part2):
            res += result
    return res


print("Solution 1: ", solve_part1(test_datas,True))
print("Solution 1: ", solve_part1(datas, False))
print("Solution 2: ", solve_part1(datas, True))
pass