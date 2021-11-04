

def t1():
    return [3,4,-1,1], 2

def t2():
    return [1,2,0], 3

def t3():
    return [-1,2,3,4,5], 1

def t4():
    # Arr from 0 to 999
    return [i for i in range(1000)], 1000

def t5():
    return [-5,-4,-3,-2,-1,1,2,3], 4

def t6():
    return [5,4,3,2,1], 6

def t7():
    return [4,6,2,4,1,1,1,1], 3

def tests():
    return [t1,t2,t3,t4,t5,t6,t7]

def solution(arr):
    # Remove negative numbers
    arr = [item for item in arr if item > 0]
    # Get the max and min
    low = min(arr)
    high = max(arr)
    full = [i for i in range(1, high+2)]
    # Get the difference between the two lists
    out = [item for item in full if item not in arr]
    return out[0]


def run_tests():
    t = tests()
    for x in t:
        arr, answer = x()
        res = solution(arr)
        assert answer == res, "Failed on L: %s, (%s should be %s)" % (arr, res, answer)
        print("Passed")

run_tests()

