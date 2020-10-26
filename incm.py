import sys
import time

ratio = 2.54

if len(sys.argv) > 1:
    inch = float(' '.join(sys.argv[1:]))
    b = inch * ratio
    print(b, "cm")
    input("Type enter to quit...")

else:
    inch = float(input("How much inches ? "))
    b = inch * ratio
    print(b, "cm")
    input("Type enter to quit...")