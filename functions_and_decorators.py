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


import logging
logging.basicConfig(filename='multiply.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running with arguments {}'.format(args))
        func(*args)
    return log_func


def multiply(*args):
    num = 1
    for x in args:
      num = num * x
    print(num)


multiply_logger = logger(multiply)

multiply_logger(2,3,4)
multiply_logger(1,2,3)


#1 Normal function call

def outer_func():
  message = "Hi"

  def inner_func():
    print(message)

  return inner_func()

outer_func()

#2 First class function

def outer_func():
  message = "Hi"

  def inner_func():
    print(message)

  return inner_func

my_func = outer_func()
my_func()

#3 Closure / Free variable

def outer_func(msg):

  def inner_func():
    print(msg)

  return inner_func

hi_func = outer_func("Hi")
hi_func()

#4 With arguments

def double():

  def inner_func(num):
    print(num*2)

  return inner_func

twox = double()
twox(2)

#4.1 passing function as arguments

def say(msg):
  print(msg)

def saytwice(msg):
  print(msg*2)

def outer_func(func):

  def inner_func(msg):
    func(msg)

  return inner_func

hi_func1 = outer_func(say)
hi_func1("Hi")

hi_func2 = outer_func(saytwice)
hi_func2("Hi")

for f in (say, saytwice):
  of = outer_func(f)
  of("Hi")

#5 *arguments

def multiply():

  def inner_func(*args):
    num = 1
    for x in args:
      num = num * x
    print(num)

  return inner_func

calc = multiply()
calc(2,3,4)
calc(1,2,3)


def decorator_function(original_function):
  def wrapper():
    print(f"Wrapper ran before {original_function.__name__}")
    original_function()
  return wrapper

def display():
  print("Display function ran.")

display = decorator_function(display)

display()

#8

def decorator_function(original_function):
  def wrapper():
    print(f"Wrapper ran before {original_function.__name__}")
    original_function()
  return wrapper

@decorator_function
def display():
  print("Display function ran.")

display()

@decorator_function
def display2():
  print("Display2 function ran.")

display2()

#9 

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self):
        print('call method before {}'.format(self.original_function.__name__))
        self.original_function()
        
@decorator_class
def display3():
  print("Display3 function ran.")

display3()

#10

# Practical Examples

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

@my_logger
@my_timer
def display2(caller):
  import time
  time.sleep(1)
  print(f"Display function ran by {caller}.")

display2("Bharath")
