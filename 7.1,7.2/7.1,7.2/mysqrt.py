import math
epsilon = 0.0000001
def mysqrt(a):
    x = 10
    while True:
        y = (x+ a/x)/2
        if abs(y-x) < epsilon:
            return y
            break
        x=y
        
def test_square_root():
    a = 1.0
    print('a'," " , "mysqrt(a)","  ", "(math.sqrt(a))"," ", "diff")
    print("-   ---------     ------------     ----")
    while a < 10.0:
        print(a, "   ", round(mysqrt(a), 1), "     ", round(math.sqrt(a), 1), "              ", round(abs(mysqrt(a)-math.sqrt(a)), 1))
        a += 1

test_square_root()