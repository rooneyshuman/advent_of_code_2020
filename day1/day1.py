import os
import sys

sys.path.append(".")
from utils import Utils

def report_repair(input):
    for num in input:
        target = 2020 - num
        if target in input:
            return num * target

def report_repair_part2(input):
    input.sort()
    for i, num in enumerate(input):
        for j, num1 in enumerate(input[i+1::]):
            target = 2020 - num - num1
            if target in input[j+1::]:
                return num * num1 * target
            

if __name__ == "__main__":
    input = Utils.input_as_int("day1/input.txt")
    print(report_repair(input)) # 982464
    print(report_repair_part2(input)) # 162292410