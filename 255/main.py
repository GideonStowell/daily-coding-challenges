def t1():
    # Ex order: [2, 4, 1, 5, 3], 3 is the last survivor for n = 5 and k = 2
    return 5, 2, 3

def tests():
    return [t1]

def solution(n, k):
    arr = [x+1 for x in range(n)]
    cur = k
    print("Begin loop cur is {}".format(cur))
    while len(arr) > 1:
        print("arr: {}".format(arr))

        t = arr.pop(cur-1)
        cur -= 1
        print("Just killed {}".format(t))

        if len(arr) == 1:
            print("Found survivor {}".format(arr[0]))
            return arr[0]

        # Iterate cur
        cur += k 
        print("Now cur is {} and len is {}".format(cur, len(arr)))

        diff = cur - len(arr)
        if diff >= 0: # Pointer has gone past end of the array
            print("Wrapping cur around to {}".format(diff))
            cur = diff

     
    

def main():

    for t in tests():
        n, k, answer = t()
        my_answer = solution(n, k)

        assert my_answer == answer, "Failed"

main()
