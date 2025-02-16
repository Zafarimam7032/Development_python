
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
