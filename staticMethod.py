class Information:

  @staticmethod
  def display():
    return "this is static method in python"

  def show(self):
    return "this is show method"
  
inf=Information()
print(inf.show())
print(Information.display())

from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
  name="Zafar Imam"
  id=1222

cons=Constants()
print(cons.name)
try:
  cons.name="Imam Hussain"
except Exception as e:
  print(f"constant can not chnages {e}")

@dataclass(frozen=True)
class Config:
    timeout: int = 30
    version: str = "1.0.0"