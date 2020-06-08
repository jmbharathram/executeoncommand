list_name = list()
print(list_name)


string_list = ["one", "two", "three"]
print(string_list)
num_list = [1, 2, 3]
print(num_list)
mixed_list = [1, 2, 3, "one", "two", "three", [4, 5, 6], {"key":"value"}]
print(mixed_list)


vegetables = ["Potatoes", "Carrots", "Cauliflower", "Broccoli", "Bell Pepper"]

print(vegetables)

print(vegetables[0])

print(vegetables[3])

print(vegetables[-1])

#Slicing

print(vegetables[0:3])   #2nd number is exclusive

print(vegetables[2:])    #Absence of a number after colon - assumes last position

print(vegetables[:4])    #Absence of a number before colon - assumes first position (0)

print(vegetables[-2:])   #Last 2 items

print(vegetables[::-1])  #Print list in reverse order

print(vegetables[::1])

print(vegetables[::2])

vegetables2 = ["Sweet Potatoes", "Green Beans", "Egg plant"]

#Concatenate

print(vegetables + vegetables2)

#useful functions

print(dir(vegetables))

help(vegetables.extend)

vegetables.append("Cabbage")
print(vegetables)
vegetables.pop()
print(vegetables)
vegetables.remove("Carrots")
print(vegetables)
vegetables.extend(vegetables2)
print(vegetables)
vegetables.insert(0, "Spinach")
print(vegetables)
vegetables.sort()
print(vegetables)
vegetables.sort(reverse=True)
sorted_vegetables = sorted(vegetables)
print(vegetables)
print(sorted_vegetables)
print(vegetables)
print(vegetables.index("Green Beans"))

vegetables3 = vegetables
print(vegetables3)
vegetables3.remove("Sweet Potatoes")
print(vegetables3)
print(vegetables)

vegetables3 = vegetables.copy()
print(vegetables3)
vegetables3.remove("Egg plant")
print(vegetables3)
print(vegetables)
print(vegetables.count("Spinach"))
vegetables.append("Spinach")
print(vegetables)
print(vegetables.count("Spinach"))

print(len(vegetables))

numbers = [10,20,30,40,50]
print(min(numbers))
print(max(numbers))

print(10 in numbers)
print(11 not in numbers)

vegetables3.clear()
print(vegetables3)
