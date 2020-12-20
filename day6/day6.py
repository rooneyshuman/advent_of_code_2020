import os
import sys

sys.path.append(".")
from utils import Utils

def custom_customs(input):
    counts = 0
    group = set()
    for line in input:
        for char in line:
            group.add(char)
        if line == "" or input.index(line) == len(input) - 1:
            counts += len(group)
            group = set()
    return counts

def custom_customs_part2(input):
    counts_sum = 0
    group = []
    person = set()
    for line in input:
        if line == "" or input.index(line) == len(input) - 1:
            counts_sum += len(group[0].intersection(*group))
            group = []
        else:
            for char in line:
                person.add(char)
            group.append(person)
            person = set()
    return counts_sum
    

if __name__ == "__main__":
    input = Utils.read_input("day6/input.txt")
    print(custom_customs(input)) # 6443
    print(custom_customs_part2(input)) # 3232