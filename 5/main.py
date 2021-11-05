


# Provided function
def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def helper(x,y):
    return x, y

def car(pair):
    '''
    Returns the first element 
    '''
    return pair(helper)[0]
def cdr(pair):
    '''
    Returns last element
    '''
    return pair(helper)[1]

def t1():
    assert car(cons(3,4)) == 3, "Failed test1"
    print("Passed")

def t2():
    assert cdr(cons(3,4)) == 4, "Failed test2"
    print("Passed")

def t3():
    assert cdr(cons(3,1000)) == 1000, "Failed test3"
    print("Passed")


t1()
t2()
t3()
