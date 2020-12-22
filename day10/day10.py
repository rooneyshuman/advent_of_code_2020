import os
import sys
from collections import defaultdict

sys.path.append(".")
from utils import Utils

def adapter_array(jolts):
    prev_jolt = 0
    diffs = defaultdict(int)
    jolts.sort()
    jolts.append(jolts[-1] + 3)     # last adapter to device

    for jolt in jolts:
        diff = jolt - prev_jolt
        diffs[diff] += 1
        prev_jolt = jolt

    return diffs[1] * diffs[3]

def adapter_array_part2(jolts):
    jolts.sort()
    paths = defaultdict(int, {0: 1})
    for jolt in jolts:
        paths[jolt] = paths[jolt - 3] + paths[jolt - 2] + paths[jolt - 1]
    return paths[jolts[-1]]

if __name__ == "__main__":
    input = Utils.input_as_int("day10/input.txt")
    print(adapter_array(input)) # 2812
    print(adapter_array_part2(input)) # 386869246296064
