import os
import sys

sys.path.append(".")
from utils import Utils

def toboggan_trajectory(input, right, down):
    i, traversed, trees = 0, 0, 0
    while i < len(input):
        row = input[i]
        loc = row[(right * traversed) % len(row)]
        if loc == "#":
            trees += 1
        i += down
        traversed += 1

    return trees

def toboggan_trajectory_part2(input):
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    prod_trees = 1
    for slope in slopes:
        trees = toboggan_trajectory(input, slope[0], slope[1])
        prod_trees *= trees
    
    return prod_trees

if __name__ == "__main__":
    input = Utils.input_as_str("day3/input.txt")
    print(toboggan_trajectory(input, 3, 1)) # 167
    print(toboggan_trajectory_part2(input)) # 736527114