# The correct, but not-so-good way of doing it
age = 0
def setAge(a):
  global age
  age = a 
setAge(100)
print age
