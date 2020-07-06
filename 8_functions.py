'''
Function

a function is a self-contained block of code that encapsulates a specific task or related group of tasks
'''

def my_func():
	print("This is my function.")

my_func()

def my_func():
	"""
	This is a dummy function.
	"""
	print("This is my function.")

	'''

Why do we need them?

- Code Reusability
- Chunking
Breaking a large task into smaller, bite-sized sub-tasks helps make the large task easier to think about and manage. 
As programs become more complicated, it becomes increasingly beneficial to modularize them in this way.
- ETL

'''

def after_tax(price):
	 print(price * 1.1)

def after_tax(price, tax_percent):
	print(price * (1 + (tax_percent/100)))

def after_tax(price, tax_percent=10):
	print(price * (1 + (tax_percent/100)))

def after_tax(price, tax_percent):
	return price * (1 + (tax_percent/100))


#When a parameter name in a Python function definition is preceded by an asterisk (*), it indicates argument tuple packing

*args

def multiply(*args):
	print("Parameters passed in", args)
	print("Type of args", type(args))
	num = 1
    for x in args:
      num = num * x
    return num

**kwargs

def sample_func(**kwargs):
    print("Parameters passed in", kwargs)
    print("Type of kwargs", type(kwargs))
    for k, v in kwargs.items():
        print(key, val)

#Python has a similar operator, the double asterisk (**), which can be used with Python function parameters and arguments to specify dictionary packing and unpacking.


def say(msg):
  print(msg)

def saytwice(msg):
  print(msg*2)

def wrapper_func(func):
  msg = "Hello."
  func(msg)

wrapper_func(say)

wrapper_func(saytwice)


