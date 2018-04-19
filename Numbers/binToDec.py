#! python3

import sys

def BinaryToDecimal(bin):
    decimal = 0
    maxComp = 2**(len(bin)-1)

    for i in range(len(bin)):
        if bin[i] == "1":
            decimal += maxComp
        maxComp /=2

    return int(decimal)

def main():
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        print(BinaryToDecimal(sys.argv[1]))

if __name__ == "__main__":
    main()
