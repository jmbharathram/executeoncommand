#[expression for item in iterable_object]

#Find the cubes of the even numbers between 0 and 10

#Using for loop

even_cubes = []
for num in range(0,11,2):
   even_cubes.append(num**3)

print("Even Cubes:", even_cubes)

#Using Map

def calculate_cube(num):
  return num**3

result = map(calculate_cube,range(0,11,2))

print(list(result))

#List comprehension

even_cubes = [ num**3 for num in range(0,11,2) ]

print("Even Cubes:", even_cubes)


#Using a function instead of expression

def calculate_power(num, power):
	return num**power

result = [ calculate_power(num,3) for num in range(0,11,2) ]

print(result)


#Using if condition

def calculate_power(num, power):
	return num**power

result = [ calculate_power(num,3) for num in range(0,11) if num % 2 == 0 ]

print(result)
