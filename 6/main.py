# Dictionary of addresses to objects
memory = {}

# Return the memory address for the obj
def get_pointer(obj):
    return hex(id(obj))

# Return the object at a memory address
def dereference_pointer(addr):
    return memory[addr]


class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.value = val
        self.both = None
    def xor(x, y):
        return get_pointer(x) ^ get_pointer(y)

class LinkedList:
    def __init__(self):
        n = Node("root")
        memory[get_pointer(n)] = n
        self.root = n
        self.last = n

    def add(element):
        '''
        Adds an element to the linked list
        '''
        # Store the obj in memory
        memory[get_pointer(element)] = element
        # Get the last element in the list 
        cur = deference_pointer(self.last)
        print(cur)


        return

    def get(index):
        '''
        Get element at the index
        '''
        return
    
