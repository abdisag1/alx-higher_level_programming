#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    x = 10
    y = 5
    print("{:d} + {:d} = {:d}".format(x, y, add(x, y)))
    print("{:d} - {:d} = {:d}".format(x, y, sub(x, y)))
    print("{:d} * {:d} = {:d}".format(x, y, mul(x, y)))
    print("{:d} / {:d} = {:d}".format(x, y, int(div(x, y))))
