import requests
from credentials import cookies_session_data
from collections import defaultdict, Counter

url = 'https://adventofcode.com/2024/day/5/input'
rules, updates = requests.get(url, cookies=cookies_session_data).text.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")
updates.pop(-1)

test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
test_rules, test_updates = test_data.split("\n\n")
test_rules = test_rules.split("\n")
test_updates = test_updates.split("\n")
test_updates.pop(-1)

def define_rules(rules):
    prefix_dict = defaultdict(list) # Key page before Value pages
    postfix_dict = defaultdict(list) # Key page after Value pages
    for rule in rules:
        before, after = rule.split("|")
        prefix_dict[before].append(after)
        postfix_dict[after].append(before)
    return prefix_dict, postfix_dict

def two_pass(update_arr, prefix_dict, postfix_dict, store=False):
    pos = 0
    invalid_page = set()
    while pos < len(update_arr)-1:
        invalid_pages = postfix_dict[update_arr[pos]]
        for i in range(pos+1, len(update_arr)):
            if update_arr[i] in invalid_pages: 
                if store:
                    invalid_page.add(update_arr[pos])
                else:
                    return False
        pos += 1
        
    pos = len(update_arr)-1
    while 1 < pos:
        invalid_pages = prefix_dict[update_arr[pos]]
        for i in range(pos, -1, -1):
            if update_arr[i] in invalid_pages: 
                if store:
                    invalid_page.add(update_arr[pos])
                else:
                    return False
        pos -= 1
    return list(invalid_page) if store else True

def solve_part1(rules, updates):
    prefix_dict, postfix_dict = define_rules(rules)

    res = 0
    for update in updates:
        pages = update.split(",")
        if two_pass(pages, prefix_dict, postfix_dict):
            res += int(pages[len(pages)//2])
    return res

def solve_part2(rules, updates):
    prefix_dict, postfix_dict = define_rules(rules)
    postfix_dict_counts = Counter(postfix_dict)

    def fix(update_arr):
        return sorted(update_arr, key=lambda item: len(postfix_dict_counts[item]) if postfix_dict_counts[item] else 0, reverse=True)
    
    def append_page(page:int , valid_order: list, prefix_dict:dict, postfix_dict:dict):
        i = 0
        while i < len(valid_order):
            if page in postfix_dict[valid_order[i]] or valid_order[i] in prefix_dict[page]:
                valid_order.insert(i, page)
                return
            i += 1
        valid_order.append(page)
    
    
    res = 0
    for update in updates:
        pages = update.split(",")
        if not two_pass(pages, prefix_dict, postfix_dict):
            reordered_pages = []
            for page in pages:
                append_page(page, reordered_pages, prefix_dict, postfix_dict)
            
            # reordered_pages = fix(pages)
            # invalid_pages = two_pass(reordered_pages, prefix_dict, postfix_dict, True)
            # if len(invalid_pages) > 0:
            #     print(reordered_pages, invalid_pages)
            res += int(reordered_pages[len(reordered_pages)//2])
    return res


print("Solution 1: ", solve_part1(rules, updates))
print("Solution 2: ", solve_part2(rules, updates))

pass