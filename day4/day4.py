import os
import sys
import re

sys.path.append(".")
from utils import Utils

def passport_processing(input):
    passports = get_passports(input)
    valid = 0
    for passport in passports:
        if has_valid_fields(passport):
            valid += 1
    return valid

def passport_processing_part2(input):
    passports = get_passports(input)
    valid = 0
    for passport in passports:
        if has_valid_fields(passport) and has_valid_values(passport):
            valid += 1
    return valid

def get_passports(input):
    passports = []
    passport = ""
    for line in input:
        passport += line + " "
        if line == "" or input.index(line) == len(input) - 1:
            passports.append(passport.strip())
            passport = ""
    return passports

def get_fields(passport):
    fields = {}
    data = passport.split()
    for d in data:
        field = d.split(":")
        fields[field[0]] = field[1]
    return fields

def has_valid_fields(passport):
    valid_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    fields = set(get_fields(passport).keys())
    return not bool(valid_fields.difference(fields))

def has_valid_values(passport):
    fields = get_fields(passport)
    result = True
    for key in fields:
        if key == "byr":
            result = result and byr(fields[key])
        elif key == "iyr":
            result = result and iyr(fields[key])
        elif key == "eyr":
            result = result and eyr(fields[key])
        elif key == "hgt":
            result = result and hgt(fields[key])
        elif key == "hcl":
            result = result and hcl(fields[key])
        elif key == "ecl":
            result = result and ecl(fields[key])
        elif key == "pid":
            result = result and pid(fields[key])
    return result

def byr(year):
    return 1920 <= int(year) <= 2002

def iyr(year):
    return 2010 <= int(year) <= 2020

def eyr(year):
    return 2020 <= int(year) <= 2030

def hgt(height):
    if "cm" not in height and "in" not in height:
        return False
    num = int(''.join(filter(str.isdigit, height)))
    if ("cm" in height and 150 <= num <= 193) or ("in" in height and 59 <= num <= 76):
        return True
    return False

def hcl(color):
    return bool(re.match("^#([a-f0-9]{6})$", color))

def ecl(color):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return color in valid_colors

def pid(id):
    return id.isnumeric() and len(id) == 9

if __name__ == "__main__":
    input = Utils.read_input("day4/input.txt")
    print(passport_processing(input)) # 192
    print(passport_processing_part2(input)) # 101