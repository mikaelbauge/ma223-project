#!/usr/bin/python3
import sys

# Generates a dict with keys a:b and set all values to 0. 
# Defaults to 1:100
def gen_dict(a=1,b=100):
    dict = {}
    for i in range(a, b+1):
        dict[str(i)] = 0
    return dict


def get_raw(FILE):
    with open(FILE, 'r') as raw:
        pass


def main():
    # Check to see if a filename was given
    if len(sys.argv) < 2:
        print("Use: ./rincewind.py FILE")
        exit()
    else:    
        table = gen_dict()
        # Open the given file
        with open(sys.argv[1], 'r') as raw:
            for line in raw:
                # Strip newline from each number
                line = line.strip('\n')
                table[line] += 1
        # Print key value. File creation can be done 
        # with BASH: .rincewind.py RAW > DATA
        for key, value in table.items():
            print(key, value)
main()
