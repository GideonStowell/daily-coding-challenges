import time

def scheduler (f, n):
    time.sleep(n/1000)
    f() 

def test():
    print("Hello world")


scheduler(test, 1000)
