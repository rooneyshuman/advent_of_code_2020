import os
import sys

sys.path.append(".")
from utils import Utils

def password_philosophy(input):
    valid = 0
    for policy in input:
        lower_bound = int(policy.split()[0].split("-")[0])
        upper_bound = int(policy.split()[0].split("-")[1])
        letter = policy.split()[1][0]
        pw = policy.split()[2]
        if (pw.count(letter) >= lower_bound) and (pw.count(letter) <= upper_bound):
            valid += 1 
    return valid

def password_philosophy_part2(input):
    valid = 0
    for policy in input:
        pos1 = int(policy.split()[0].split("-")[0]) - 1
        pos2 = int(policy.split()[0].split("-")[1]) - 1
        letter = policy.split()[1][0]
        pw = policy.split()[2]
        if (pw[pos1] == letter) ^ (pw[pos2] == letter):
            valid += 1
    return valid

if __name__ == "__main__":
    input = Utils.input_as_str("day2/input.txt")
    print(password_philosophy(input)) # 625
    print(password_philosophy_part2(input)) # 391