# reduce || returns final value

# lambda is a built in keyword in python
# It is simply an anonymous function.
# Anonymous means it has no name.
# syntax: lambda parameters: expression

from functools import reduce
mylist = [1,2,3,4,5]
def add(x,y):
    return x + y
red_obj =reduce(add, mylist)
print(red_obj)

# find the largest number
from functools import reduce

numbers = [12, 7, 45, 20]

largest = reduce(lambda x, y: x if x > y else y, numbers)

print(f"largest number = {largest}")

#using maximum
from functools import reduce

numbers = [12, 7, 45, 20]

largest = reduce(max, numbers)

print(largest)