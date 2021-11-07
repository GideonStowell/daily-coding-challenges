def get_value(string):
    '''
    Returns a number from the letter
    according to mapping a=1, b=1,... z=26
    '''
    return int(hex(ord(string)), base=16) - 0x60

def parse_msg(msg):
    '''
    Needs to iterate over all the possible ways interpret a msg
    '''
    count = 0;
    # Create a set and store all possibilities in the set
    options = {}
    for x in msg:
        print(x)

def make_lists(msg):
    
    for i in range(len(msg)+1):
        ll = []
        for j in range(msg):
            ll.append(msg)

make_lists('111')

