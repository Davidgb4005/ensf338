import sys

import math
# 1) The Code implements the Quadratic formula for finding roots of 2nd degree polynomials

# 2.0) The Compilation Error was incorrect matching of quotes causing the compiler error,
# 2.1) A possible run time error of div/0 can also occur if argv[1] is 0 or checkin if 3 argv were passed
def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"The solutions are: {root1}, {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"The solution is: {root}")
    else:
        print("There are no real solutions.")
do_stuff()