import json 

class Node:
    def __init__ (self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_tree(root):
    '''
    Recursive function
    Base case: Left and right values are not Node class types, they will be None types
    '''
    if root == None:
        return 
    else:
        return {'val': root.val, 'left': traverse_tree(root.left), 'right': traverse_tree(root.right)}

def remove_nulls(d):
    dd = {}
    for k,v in d.items():
        if isinstance(v, dict):
            dd[k] = remove_nulls(v)
        elif v is not None:
            dd[k] = v
    return dd

def serialize(node):
    '''
    Takes in a node object and returns a string
    '''
    dict_obj = traverse_tree(node)
    out = remove_nulls(dict_obj)
    string = json.dumps(out)
    print(string)
    return string

def create_tree(json_obj):
    '''
    Recurisvely create a tree from json object
    Base case: return current node's value
    Otherwise the right/left nodes have values, create a tree for those
    '''
    right = None
    left = None
    if 'right' in json_obj:
        right = create_tree(json_obj['right'])
    if 'left' in json_obj:
        left = create_tree(json_obj['left'])

    return Node(json_obj['val'], left, right)



def deserialize(string):
    '''
    Takes a string object and returns a node object
    '''
    obj = json.loads(string)
    
    node = create_tree(obj)
    print(serialize(node))
    return node

def test1():
    '''
     Example tree looks like this:
          root
         /   \
       left  right
       /  
    left.left
    ''' 
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


def main():
    test1()

main()
