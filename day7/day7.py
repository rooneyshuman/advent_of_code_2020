import os
import sys
import re

sys.path.append(".")
from utils import Utils

def handy_haversacks(input):
    rules = parse_rules(input)
    count = 0
    for bag in rules:
        if has_shiny_gold(rules[bag], rules):
            count += 1
    return count

def handy_haversacks_part2(input):
    rules = parse_rules(input)
    return sub_bag_count(rules['shiny gold'], rules)

def parse_rules(input):
    rules = {}
    for line in input:
        words = line.split()
        key = words[0]+ " " + words[1]
        rules[key] = {}
        for i, word in enumerate(words):
            if word.isnumeric():
                rules[key][(words[i+1]+ " " + words[i+2])] = int(word)
    return rules

def has_shiny_gold(sub_bags, rules):
    for sub_bag in sub_bags:
        if sub_bag == 'shiny gold':
            return True
        if has_shiny_gold(rules[sub_bag], rules):
            return True
    return False

def sub_bag_count(sub_bags, rules):
    if sub_bags == {}:
        return 0
    total = 0
    for sub_bag in sub_bags:
        total += ((sub_bag_count(rules[sub_bag], rules) + 1) * sub_bags[sub_bag])
    return total

if __name__ == "__main__":
    input = Utils.read_input("day7/input.txt")
    print(handy_haversacks(input)) # 337
    print(handy_haversacks_part2(input)) # 50100