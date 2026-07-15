# class task 2
def Calculate(a,b,c):
  if (c == "+"):
    return a+b
  elif (c == "-"):
    return a-b
  elif (c == "*"):
    return a*b
  elif (c == "/"):
    return a/b
  else:
    return "Invalid sign"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sign = input("Enter sign: ").strip()

d = Calculate(a,b,sign)
print("After performing the calculation: ",d)
