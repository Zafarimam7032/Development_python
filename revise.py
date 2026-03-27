age =45

if age>50:
  print("this is true phase")
elif age<40:
  print("this is false block")
else:
  print("this is else block")    


try:
  if(age>30):
    raise Exception("this is normal Exception")
except Exception as e:
  print(e)

def display():
  try:
   return 10;
  except:
    return 20;
  finally:
   return 30;

result=display()

print(result)

  
