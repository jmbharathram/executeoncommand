# Normal method
import memory_profiler

def generate_even_squares(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num*num)

    return even_list

m1 = memory_profiler.memory_usage()
es = generate_even_squares(range(30000000))

counter=0
for x in es:
    if counter > 10:
       break
    print(x)
    counter = counter + 1

m2 = memory_profiler.memory_usage()
print("Memory used (mb): ", round(m2[0]-m1[0]))


# Generator method
import memory_profiler
def generate_even_squares(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            yield (num*num)

m1 = memory_profiler.memory_usage()
es = generate_even_squares(range(10000))
'''
print(next(es))
print(next(es))
print(next(es))
'''
counter=0
for x in es:
    if counter > 10:
       break
    print(x)
    counter = counter + 1

m2 = memory_profiler.memory_usage()
print("Memory used (mb): ", round(m2[0]-m1[0]))
