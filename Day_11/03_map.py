#find square of each number || map applies to each item in a iterable
numbers = [2,4,6,8,0]
def mult(x):
    return x ** 2
map_obj = map(mult, numbers)
print(list(map_obj))

# converts string to integer
numbers = ["10", "20", "30", "40"]

result = map(int, numbers)

print(list(result))

# map working in multiple iterables
lsta = [1, 2, 3]
lstb = [4, 5, 6]

result = map(lambda x, y: x + y, lsta, lstb)
print("addition between two list")
print(list(result))

