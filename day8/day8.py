import os
import sys
import re

sys.path.append(".")
from utils import Utils

def handheld_halting(input):
    insts = get_instructions(input)
    seen = []
    i = acc = 0
    while i not in seen:
        seen.append(i)
        op, arg = insts[i]
        if op == "nop":
            i += 1
        elif op == "acc":
            acc += int(arg)
            i += 1
        elif op == "jmp":
            i += int(arg)
    return acc

def handheld_halting_part2(input):
    insts = get_instructions(input)
    acc = None
    for inst in insts:
        inst[0] = change_nop_jmp(inst[0])
        if acc := execute(insts):
            break
        inst[0] = change_nop_jmp(inst[0]) # change back to retry
    return acc

def get_instructions(input):
    insts = []
    for line in input:
        insts.append(line.split())
    return insts

def execute(insts):
    i = acc = 0
    seen = []
    while i <= len(insts) - 1:
        seen.append(i)
        op, arg = insts[i]
        if op == "nop":
            i += 1
        elif op == "acc":
            acc += int(arg)
            i += 1
        elif op == "jmp":
            i += int(arg)
        if i in seen:
            return False
    return acc
    
def change_nop_jmp(op):
    if op == "nop":
        return "jmp"
    if op == "jmp":
        return "nop"
    return op
    

if __name__ == "__main__":
    input = Utils.read_input("day8/input.txt")
    print(handheld_halting(input)) # 1179
    print(handheld_halting_part2(input)) # 1089