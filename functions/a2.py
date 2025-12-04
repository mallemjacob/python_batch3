# import a1
from a1 import adder, subtractor
# from a1 import adder as aa
# as is alias

def as_caller():
    a = adder(1,3) #4
    b = subtractor(10,5) #5
    return a, b