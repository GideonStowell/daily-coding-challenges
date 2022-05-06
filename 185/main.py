def test1():
    return {
            "rect1": {"cords": (1,4), "dim": (3,3)},
            "rect2": {"cords": (0,5), "dim": (4,3)},
            "answer": 6
           }

def test2():
    return {
            "rect1": {"cords": (0,0), "dim": (1,1)},
            "rect2": {"cords": (0,0), "dim": (2,2)},
            "answer": 1
           }
def test3():
     return {
            "rect1": {"cords": (0,0), "dim": (1,1)},
            "rect2": {"cords": (1,1), "dim": (1,1)},
            "answer": 0
           }
def test4():
     return {
            "rect1": {"cords": (0,0), "dim": (3,3)},
            "rect2": {"cords": (0,0), "dim": (3,3)},
            "answer": 9
           }

def tests() :
    return [test1, test2, test3, test4]

def greatest(val1, val2):
    return val1 if val1 > val2 else val2

def least(val1, val2):
    return val1 if val1 < val2 else val2

def get_overlap_area(args):
    '''
       Args should have rect1, rect2
       Each with a cords and dim property

       Solution is to get highest x cord
       get lowest x + width cord
       get lowest y cord
       get highest y+ dim cord

    '''
    cords = "cords"
    dim   = "dim"
    x     = 0
    y     = 1

    # Greatest beginning x position (left)
    rect1_x_cord = args["rect1"][cords][x]
    rect2_x_cord = args["rect2"][cords][x]
    left = greatest(rect2_x_cord, rect1_x_cord)
    # Least of x position pluz width (right)
    rect1_x_cord = args["rect1"][dim][x] + rect1_x_cord
    rect2_x_cord = args["rect2"][dim][x] + rect2_x_cord
    right      = least(rect1_x_cord, rect2_x_cord)

    # Least y beginning position (top)
    rect1_y_cord = args["rect1"][cords][y]
    rect2_y_cord = args["rect2"][cords][y]
    top      = least(rect1_y_cord, rect2_y_cord)

    # Greatest y plus height (bottom)
    rect1_y_cord =  rect1_y_cord - args["rect1"][dim][y]
    rect2_y_cord =  rect2_y_cord - args["rect2"][dim][y]
    bottom   = greatest(rect1_y_cord, rect2_y_cord)

    width  = right - left
    height = top - bottom

    return width * height


def main():
    t = tests()
    for x in t:
        args = x()
        ans = get_overlap_area(args)
        assert args["answer"] == ans, "Expect {}, calculated {}".format(args["answer"], ans)




main()
