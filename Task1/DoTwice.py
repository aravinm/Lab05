import sys

input1 = int(sys.argv[1])
input2 = int(sys.argv[2])


def double(x):
    a = 2 * x
    return a


def square(x):
    a = x ** 2
    return a


def cube(x):
    a = x ** 3
    return a


try:
    if input2 == 1:
        print double(double(input1))
    elif input2 == 2:
        print square(square(input1))
    elif input2 == 3:
        print cube(cube(input1))
    else:
        print "It cannot be supported!"
except:
    print "It cannot be supported!"
