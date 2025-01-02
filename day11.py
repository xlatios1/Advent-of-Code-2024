import requests
from credentials import cookies_session_data

url = 'https://adventofcode.com/2024/day/11/input'
response = requests.get(url, cookies=cookies_session_data)
stones = response.text.split("\n")
stones = stones[0].split(" ")

testdata = ["125", "17"]

def solve_part1(original_stones: list, blink_count):
    stones = list(original_stones)
    for _ in range(blink_count):
        i = len(stones)-1
        while i >= 0:
            stone = stones[i]
            stone_len = len(stone)
            if stone == "0":
                stones[i] = "1"
            elif stone_len % 2 == 0:
                l, r = stone[:stone_len//2], stone[stone_len//2:]
                stones[i] = r
                stones.insert(i, l)
            else:
                stones[i] = str(int(stone)*2024)
            i -= 1
        stones = [str(int(stone)) for stone in stones]
    return len(stones)

def solve_part2(initial_stones:str, total_blinks:int):
    memo = {}

    def dfs(stone, blinks):
        if blinks == 0:
            return 1

        if (stone, blinks) in memo:
            return memo[(stone, blinks)]

        if stone == "0":
            transformed_stones = ["1"]
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left, right = int(stone[:mid]), int(stone[mid:])
            transformed_stones = [str(left), str(right)]
        else:
            transformed_stones = [str(int(stone) * 2024)]

        result = sum(dfs(new_stone, blinks - 1) for new_stone in transformed_stones)

        memo[(stone, blinks)] = result
        return result

    total_stones = sum(dfs(stone, total_blinks) for stone in initial_stones)
    print(memo)
    return total_stones

print("Solution 1: ", solve_part1(testdata, 25))
print("Solution 1: ", solve_part1(stones, 25))
print("Solution 2: ", solve_part2(stones, 75))

pass