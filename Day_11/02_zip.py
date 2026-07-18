data1 = ["Richard", "David", "Robert"]
data2 = [1,2,3]

for name,rollno in zip(data1,data2):
  print(rollno,name, sep="->")