import os
import sys

class Utils:
    def input_as_str(filepath):
        input = []
        with open(filepath) as fp:
            line = fp.readline().strip()
            while line:
                input.append(line)
                line = fp.readline().strip()
        return input
    
    def input_as_int(filepath):
        input = []
        with open(filepath) as fp:
            line = fp.readline().strip()
            while line:
                input.append(int(line))
                line = fp.readline().strip()
        return input
    
    def read_input(filepath):
        fp = open(filepath, "r")
        input = fp.read().splitlines()
        return input