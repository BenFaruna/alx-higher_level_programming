#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if (len(sys.argv) < 4):
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    result = int()
    if (operator == "+"):
        result = add(a, b)
    elif (operator == "-"):
        result = sub(a, b)
    elif (operator == "*"):
        result = mul(a, b)
    elif (operator == "/"):
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
