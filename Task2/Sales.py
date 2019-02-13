import sys

input1 = map(int, sys.argv[1].split(","))
input2 = int(sys.argv[2])


def scale(list1, x):
    return map(lambda i: i * x, list1)


def last_digit(y):
    return y[-1]


def sorting(list1):
    list1 = map(str, list1)
    sorted(list1, key=last_digit)
    list1 = map(int, list1)
    return list1


def good_sales(list1):
    avg = sum(list1) / len(list1)
    list2 = filter((lambda x: x > avg), list1)
    return list2


def one_program(list1, x):
    print "The scaled number is: " + str(scale(list1, x)),
    print "The sorted sales numbers are: " + str(sorting(list1)),
    print "The good sales numbers are: " + str(good_sales(list1))


one_program(input1, input2)
