#!/usr/bin/python

import sys

# Constants
ARRAY_SIZE = 30,000

# Implements the BF array
class BFArray:
    def __init__(self):
        self.array = []
        for x in range(0, ARRAY_SIZE):
            self.array.append(0)
        self.ptr = 0

# Implements a loop command
class LoopCMD:
    def __init__(self, loc):
        self.location = loc - 1


def print_error(error):
    print(error)
    exit()

def interpret(source):
    # First create the BF array
    bfarray = BFArray()

    # And a loop stack
    loopstack = []
    x = 0
    while x < len(source):
        char = source[x]
        x += 1

        if char == '>':
            if (bfarray.ptr < ARRAY_SIZE):
                bfarray.ptr += 1
            else:
                print_error("Error at Command {} [>]: Array capacity reached!".format(x + 1))

        elif char == '<':
            if (bfarray.ptr > 0):
                bfarray.ptr -= 1
            else:
                print_error("Error at Command {} [<]: Cannot move before 0 on the array!".format(x + 1))
            
        elif char == '+':
            bfarray.array[bfarray.ptr] += 1

        elif char == '-':
            bfarray.array[bfarray.ptr] -= 1

        elif char == '.':
            if (bfarray.array[bfarray.ptr] >= 0 and bfarray.array[bfarray.ptr] <= 255):
                character = chr(bfarray.array[bfarray.ptr])
                print(character)
            else:
                print_error("Error at Command {} [.]: Cannot print the value!".format(x + 1))

        elif char == ',':
            character = input("Enter character:").split(" ")[0]
            bfarray.array[bfarray.ptr] = ord(character)

        elif char == '[':
            # Add the loop command to the stack
            if (bfarray.array[bfarray.ptr] != 0):
                loopstack.append(LoopCMD(x))

        elif char == ']':
            # Check from the last item of the loop stack
            loopcmd = loopstack[-1]
            if (bfarray.array[bfarray.ptr] != 0):
                x = loopcmd.location
            loopstack.pop()


if (__name__ == "__main__"):
    # First load .bf file
    if len(sys.argv) == 2:
        file = open(str(sys.argv[1]))

        # Prepare and interpret the source code
        source_code = file.read().strip()
        file.close()
        interpret(source_code)

    # Ensure that there are only two arguments - the python file and the .bf file
    elif len(sys.argv) < 2:
        print_error("Error: Too few arguments!")

    else:
        print_error("Error: Too many arguments!")
