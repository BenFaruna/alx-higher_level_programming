#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from add_0 import add
    count = len(sys.argv)
    total = int()
    if (count == 1):
        print("{}".format(total))
    elif (count > 1):
        for i in range(1, count):
            total = add(total, int(sys.argv[i]))
        print("{:d}".format(total))
