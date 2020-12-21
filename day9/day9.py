import os
import sys

sys.path.append(".")
from utils import Utils

def encoding_error(cypher, p_len):
    i = p_len
    breaking = None
    while i < len(cypher[p_len::]):
        preamble = cypher[i-p_len:i]
        if breaking := is_breaking_num(cypher[i], preamble):
            break
        i += 1
    return breaking

def is_breaking_num(target, preamble):
    for num in preamble:
        to_find = target - num
        if to_find in preamble and to_find != num:
            return False
    return target

def encoding_error_part2(cypher, p_len):
    breaking_num = encoding_error(cypher, p_len)
    enc_weakness = find_enc_weakness(breaking_num, cypher)
    return max(enc_weakness) + min(enc_weakness)

def find_enc_weakness(breaking_num, cypher):
    enc_weakness = []
    for i, num in enumerate(cypher):
        while sum(enc_weakness) < breaking_num:
            enc_weakness.append(cypher[i])
            i += 1
        if sum(enc_weakness) == breaking_num:
            break
        enc_weakness.clear()
    return enc_weakness

if __name__ == "__main__":
    input = Utils.input_as_int("day9/input.txt")
    print(encoding_error(input, 25)) # 88311122
    print(encoding_error_part2(input, 25)) # 13549369