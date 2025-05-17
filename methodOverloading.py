
class Calcular:
  @staticmethod
  def show( *args):
    return sum(args) 
 

  print(show(10,20,30,40))
  print(show(10,29))
  print(show(10,20,30))