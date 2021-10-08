# This will be one of the most advanced results you will find.

# We will be using classes and simple operators like +,-,*,/

class Calculator:
  def addition(a,b):
    return a + b

  def subtraction(a,b):
    if a<b:
      return b - a
    else:
      return a - b

  def multiplication(a,b):
    return a * b

  def division(a,b):	
    if a<b:
      return b / a
    else:
      return a / b

# You can do this in terminal.
<C:/Users/username>python
>>> from main import Calculator
>>> result = Calculator.[addition|subtraction|multiplication|division](anyNumber, anyNumber)
>>> print(result)