def ex1():
    return [10, 15, 3, 7], 17, True

def ex2():
    return [], 10, False

def ex3():
    return [1], 1, False

def ex4():
    return [1,1], 1, False

def ex5():
    return [1,1], 2, True

def ex6():
    return [1,2,3,4], 6, True

def ex7():
    return [1,2,3,4], 7, True

def ex8():
    return [0,0,3,4], 0, True

def ex9():
    return [10000000, 1, 17], 4, False

def ex10(): 
    return [10000000, 1, 17], 10000001, True

def tests():
    return [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10]

def solution(l, k):
    iterations = 0;
    # Any list with 0 or 1 elements, can't compute a sum on
    if len(l) < 2: 
        return False, iterations
    for x in range(len(l)-1):
        iterations+=1
        #x is current position in the list
        #print("X %s" % x)
        for y in range(1,len(l) - x): # Y is the rest of the positions in the list, beyond x
            #print("Y %s" %y)
            # Compute the sum of the current value and the next values
            summation = l[x] + l[x+y]
            #print("Sum of %s and %s is %s" % (l[x], l[x+y],summation))
            # Return true if we ever get the value k
            if summation == k:
                return True, iterations 
    # Return false when we've exhausted all possibilities
    return False, iterations

def run_tests():
    t = tests()
    #Iterate through the tests
    for x in t:
        l, k , r = x()
        #print("L: %s, k: %s, r: %s" % (l, k, r))
        res, count = solution(l, k)
        assert res == r, "Failed on l: %s and k: %s (%s should be %s)" %(l,k,res,r)
        print("passed: %s" % count)

run_tests()
