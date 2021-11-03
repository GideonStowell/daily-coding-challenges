# Test cases
# Assuming all lists contain only numbers and have greater than 1 element
def ex1():
    return [1,2,3,4,5], [120,60,40,30,24]
def ex2():
    return [3,2,1], [2,3,6]
def ex3(): 
    return [1,1,0,1], [0,0,1,0]
def ex4(): 
    return [1,2,3], [6,3,2]
def ex5():
    return [1,2], [2,1]
def ex6():
    return [0,0], [0,0]
def ex7():
    return [10,1,1,1,1], [1,10,10,10,10]
def ex8():
    return [2,2,2,2], [8,8,8,8]
def ex9():
    return [3,3,3], [9,9,9]
def ex10():
    return [17,2,1], [2,17,34]


def tests():
    return [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10]

# Compute the product of all elements in the list execpt the one at list[index]
def product(start_list, index):
    # Starting with 1 is allowed because 1*x = x
    output = 1
    #Iterate through list, skipping index
    for x in range(len(start_list)):
        if index != x:
            output *= start_list[x]
    #return computed product
    return output

def solution(start_list):
    #Create target list
    output = []
    #Iterate over target list, appending products as we go
    for i in range(len(start_list)):
        output.append(product(start_list, i))
    return output

def run_tests():
    t = tests()
    #Iterate through tests, get an answer and compare to expectation
    for x in t:
        start, result = x()
        res = solution(start)
        assert result == res, "Failed on L: %s (got %s, should be %s)" % (start, res, result)
        print("Passed")

run_tests()
