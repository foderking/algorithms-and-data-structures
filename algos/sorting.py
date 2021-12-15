#!/usr/bin/python3
from utility import getArray
from benchmark import testSuite
from timing import timeThis

@timeThis
def insertionSort(array, debug=False):
    """
    https://www.youtube.com/watch?v=Kg4bqzAqRBM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3
    
    Complexity: O(n2)
    """
    def swapTillSorted(array, index):
        """
        With all arrays to left of element at `index` are sorted
        keep swapping element till its sorted within the array
        BEFORE
        ======
            current elem
                v
        _______ _________
        |1|3|4| 2|8|22|1|
        ------- ---------
          ^          ^
        sorted    unsorted
        part      part

        AFTER
        ======
        current elem
           v
        _________ _______
        |1|2|3|4| 8|22|1|
        --------- -------
          ^         ^
        sorted    unsorted
        part      part
        """
        current_elem = array[index]
        if debug:
            print(f"{array[:index]}: {current_elem}: {array[index+1:]}")

        for i in range(index-1, -1, -1):
            if array[i] <= current_elem:
                array.pop(index)
                array.insert(i+1, current_elem)
                return

        # if it reaches here, the current elem is the smallest elem
        array.pop(index)
        array.insert(0, current_elem)


    array_len = len(array)
    for index in range(1, array_len):
        swapTillSorted(array, index)


def test():
    array_dic = {}
    max_no = 10**5

    def getNo(no):
        if no in array_dic:
            return array_dic[no]
        else:
            value = getArray(max_no, no)
            array_dic[no] = value
            return value

    def sortWrapper(no, func):
        arr = getNo(no)
        return func(arr)
    
    testSuite(sortWrapper, insertionSort)


if __name__ == "__main__":
    test()