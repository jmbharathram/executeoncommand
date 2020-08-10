def square_and_multiply(*args):
	num = 1
	for x in args:
		num = num * (x**2)
	return num

def multiply(*args):
	num = 1
	for x in args:
		num = num * x
	return num

result1 = square_and_multiply(2,3,4)

result2 = multiply(2,3,4)
