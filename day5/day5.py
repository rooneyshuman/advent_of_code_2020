import os
import sys

sys.path.append(".")
from utils import Utils

def binary_boarding(input):
    highest_id = 0
    for bp in input:
        row = find_seat_section(bp[0:7], [0,127])
        col = find_seat_section(bp[7::], [0,7])
        id = row * 8 + col
        if id > highest_id:
            highest_id = id 
    return highest_id

def find_seat_section(bp, range):
    for section in bp:
        if section == "F" or section == "L":
            range[1] = range[1] - (range[1] - range[0])//2 - 1
        elif section == "B" or section == "R":
            range[0] = range[1] - (range[1] - range[0])//2 
    return range[0]

def binary_boarding_part2(input):
    ids = [] 
    for bp in input:
        row = find_seat_section(bp[0:7], [0,127])
        col = find_seat_section(bp[7::], [0,7])
        id = row * 8 + col
        ids.append(id)

    for id in ids:
        if (id + 1) not in ids and (id + 2) in ids:
            return id + 1

if __name__ == "__main__":
    input = Utils.input_as_str("day5/input.txt")
    print(binary_boarding(input)) # 926
    print(binary_boarding_part2(input)) # 657