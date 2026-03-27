
list1=["zafar","meena","kirti","imam","manoj"];

for name in list1:
  print(name)
else:
  print("data print successfully")  

i=0;
while(i <len(list1)):
  print(list1[i]) 
  i+=1

list2=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for row in list2:
  for element in row:
    print(element,end=' ')
  print()  


tup=(12,23,12,45,78);

for data in tup:
  print(data)

for i in range(4):
  print("loop")
else:
  print("loop is finished")  


for i in range(5):
  if i==3:
    break
  print(i)      

for i in range(8):
  if i<7:
    continue
  print(i)  

