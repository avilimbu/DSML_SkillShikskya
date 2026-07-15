# Write a user-defined function that takes 5 user inputs.
# If the user enters an integer, add it to a list 
# If the user enters a float number, remove the last element 
# Finally, display the updated list after each operatio

#class task 3
def udf():
  l = []
  for i in range(5):
    n = input("Enter a number: ")
    if "." in n:
      if (len(l)>0):
        remove = l.pop()
        print(f"float detected. Removed: {remove}")
      else:
        print("float detected but the list is empty")
    else:
      l.append(int(n))
      print(f"{n} added to the list")
  return l

c = udf()
print(c)