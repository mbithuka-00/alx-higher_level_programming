#!/usr/bin/python3
#AUTHOR:MATTHEW MBITHUKA

if __name__ == "__main__":
    """Print the addition of all the  arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
