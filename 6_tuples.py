Tuple is an ordered collection of objects, that is immutable.

list_1 = ['Banana', 'Apple', 'Water Melon', 'Pineapple', 'Mango']  #List

tuple_1 = ('Banana', 'Apple', 'Water Melon', 'Pineapple', 'Mango')  #Tuple

set_1 = { "v1", "v2", "v3"} #set

#unordered vs ordered data structure

print(set_1)

print(tuple_1)

#immutable

list_1[0] = "Kiwi"

tuple_1[0] = "Kiwi"

# List or a mutable object inside tuple

tuple_2 = ('Cherry', 'Kiwi', ['Strawberry'])

tuple_2[2].append('Blueberry')

# Packing and Unpacking

tuple_3 = ('Banana', 'Apple', 'Water Melon')

(fruit_1, fruit_2, fruit_3) = tuple_3

fruit_1, fruit_2, fruit_3 = tuple_3

# Swapping

a = 3
b = 4

a, b
b, a

a, b = b, a
