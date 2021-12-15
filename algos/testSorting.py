from random import random
from math import floor
import timing
import matplotlib.pyplot as plt
# from timeit import timeit
  

def testSuite(buildFunc, *funcs):
    """
    Measures the time it takes multiple functions to execute with
    a varying number of inputs (1, 10, 100, 1000, ...)
    (currently supports max three funcs)
    
    Plots the graph comparing the time taken with respect
    to the number of input for the functions

    buildFunc is wrapper that takes no of functions to execute, and the function as arguments
        returns => the value of the execution, time taken, name of function
    funcs is a tuple of functions to test
    """
    max = 1000000
    x = []
    y1 = []
    y2 = []
    y3 = []
    name1 = ""
    name2 = ""
    name3 = ""

    no_funcs = len(funcs)
    no_elems = 1

    if no_funcs <= 1:
        raise "Needs at least one function"

    while no_elems < max:
        if no_funcs == 2:
            _, y11, name1 = buildFunc(no_elems, funcs[0])
            _, y22, name2 = buildFunc(no_elems, funcs[1])
            # _, y11 =buildArray(max, no_elems)
            # _, y22 =altBuild(max, no_elems)

            y1.append(y11)
            y2.append(y22)

        elif no_funcs == 3:
            _, y11, name1 = buildFunc(no_elems, funcs[0])
            _, y22, name2 = buildFunc(no_elems, funcs[1])
            _, y33, name3 = buildFunc(no_elems, funcs[2])

            y1.append(y11)
            y2.append(y22)
            y3.append(y33)

        x.append(no_elems)
        no_elems *= 10

    y3 = [0] * 6 if not y3 else y3

    plt.xlabel("No of elements")
    plt.ylabel("Time taken")

    plt.plot(x, y1, 'r', label=name1)
    plt.plot(x, y2, 'b', label=name2)
    plt.plot(x, y3, 'g', label=name3)

    plt.legend()
    plt.show()

def test():
    """
    Tests the test suite
    """
    @timing.timeThis
    def buildArray(max, length):
        arr = []
        for _ in range(length):
            arr.append( floor(random() * max) )
        return arr

    @timing.timeThis
    def altBuild(max, length):
        return [ floor(random() * max) for i in range(length)]
    
    @timing.timeThis
    def slowBuildArray(max, length):
        arr = []
        for _ in range(length):
            sum([max, max])
            arr.append( floor(random() * max) )
        return arr
 
    def testBuildFunc(no, func):
        return func(100000, no)

    testSuite(testBuildFunc, buildArray, altBuild, slowBuildArray)

if __name__ == "__main__":
    test()