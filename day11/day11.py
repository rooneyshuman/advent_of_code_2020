import os
import sys
import copy

sys.path.append(".")
from utils import Utils

def seating_system(input):
    take_layout = take_seat(input)
    abandon_layout = abandon_seat(take_layout, 4)
    while(take_layout != abandon_layout):
        take_layout = take_seat(abandon_layout)
        abandon_layout = abandon_seat(take_layout, 4)

    occupied_count = 0
    for row in abandon_layout:
        for spot in row:
            if spot == "#":
                occupied_count += 1
    return occupied_count

def take_seat(layout):
    new_layout = copy.deepcopy(layout)
    for i, row in enumerate(layout):
        for j, spot in enumerate(row):
            if spot == "L":
                if has_empty_adj(i, j, layout):
                    new_layout[i][j] = "#"
    return new_layout

def abandon_seat(layout, max_occ):
    new_layout = copy.deepcopy(layout)
    for i, row in enumerate(layout):
        for j, spot in enumerate(row):
            if spot == "#":
                if has_occupied_adj(i, j, layout, max_occ):
                    new_layout[i][j] = "L"
    return new_layout

def has_occupied_adj(i, j, layout, max_occ):
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    occupied_count = 0
    for d in directions:
        x = i + d[0]
        y = j + d[1]
        if 0 <= x < len(layout) and 0 <= y < len(layout[0]) and layout[x][y] == "#": 
            occupied_count += 1
    if occupied_count >= max_occ:
        return True
    return False

def has_empty_adj(i, j, layout):
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for d in directions:
        x = i + d[0]
        y = j + d[1]
        if 0 <= x < len(layout) and 0 <= y < len(layout[0]) and layout[x][y] == "#":
            return False
    return True

if __name__ == "__main__":
    input = Utils.input_as_lists("day11/input.txt")
    print(seating_system(input)) # 2152