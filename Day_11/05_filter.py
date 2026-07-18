# filter(function, iterable)

def even(num):
    return num % 2 == 0
f_obj = filter(even, [1,3,4,6,8,9])
a= list(f_obj)
print(a)
b =list(f_obj)
print(b)



#keeping words longer than 5 letters
words = ["apple", "banana", "cat", "elephant", "dog"]

result = filter(lambda word: len(word) > 5, words)

print(list(result))