def uppercase_decorator(func):
def wrapper():
display= func()
return display.upper()
return wrapper

@uppercase_decorator
 def name ():
return "welcome to vglug"
 print(name())
