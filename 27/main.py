import logging
logging.basicConfig(level=logging.DEBUG)


# Tests

def t1():
    return "([])[]({})", True

def t2():
    return "([)]", False

def t3():
    return "((()", False

def t4():
    return "()", True

def t5():
    return "{", False

def t6():
    return "}", False

def t7():
    return "([]{}[]{}[]{}{}{})()", True

def t8():
    return "{}()[]q", False

def tests():
    return [t1, t2, t3, t4, t5, t6, t7, t8]


def solution(string):
    balanced = False
    stack = []
    types = {"(":")", "[":"]", "{":"}"}
        
    #Add opening types to stack, closing types pop off if they match
    for x in string:

        # Opening types
        if x in list(types.keys()):
            # Adding opening types to the stack
            stack.append(x)
        elif x in list(types.values()): # Closing types
            # Try to pop opening types off stack with matching closing type
            try:
                c = stack.pop()
                if types[c] != x:
                    return False
            except:
                logging.error("Error occured popping off the stack")
                return False
        else:
            # Invalid type, not defined
            return False
    
    # Check if stack is empty
    if len(stack) == 0:
        balanced = True

    return balanced

def main():
    t = tests()
    for x in t:
        string, expected = x()
        logging.debug("Test string: %s, balanced: %s" % (string, expected))
        logging.debug("Run solution on test")
        res = solution(string)
        assert res == expected, "Failed on: %s, expected %s but got %s" % (string, expected, res)

main()
