def t1():
    return [5, 1, 3, 5, 2, 3, 4, 1], 5

def t2():
    return [1,2,3,4,5,5,5,5,5], 5

def t3():
    return [1,2,1,2,1,2,1,2,1,2,1], 2

def t4():
    return [1], 1

def t5():
    return [], 0

def t6():
    return [1,2,3], 3

def tests():
    return [t1,t2,t3,t4,t5,t6]

def solution(arr):
    distinct_set = set()
    for val in arr:
        distinct_set.add(val)

    return len(distinct_set)

def main():

    t = tests()
    for x in t:
        arr, expected_length = x()
        calc_length = solution(arr)

        assert calc_length == expected_length, "Answer is {}, calculated {}".format(expected_length, calc_length)
        print("passed")
main()
