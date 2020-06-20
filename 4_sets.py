#set_variable_name = set(<iterable>)

#Caveat while initializing an empty set
vegetables = set()
print(type(vegetables))
vegetables = {}
print(type(vegetables))

vegetables = {"Potatoes", "Carrots", "Cauliflower", "Broccoli", "Bell Pepper"}

print(vegetables)
print(type(vegetables))

vegetables = set(["Potatoes", "Carrots", "Cauliflower", "Broccoli", "Bell Pepper"])

print(vegetables)
print(type(vegetables))

vegetables = set("Potatoes")
print(vegetables)
print(type(vegetables))

#Mixed datatype set
vegetables = {"Potatoes", "Carrots", "Cauliflower", "Broccoli", "Bell Pepper", 12}
print(vegetables)

#vegetables = {"Potatoes", "Carrots", "Cauliflower", "Broccoli", "Bell Pepper", [1,2]}
#lst = [1,2]
#print(lst.__hash__())
#num = 1
#print(num.__hash__())

vegetables.remove(12)
print(vegetables)
#vegetables.remove(12)
#print(vegetables)
vegetables.discard(12)
print(vegetables)

vegetables2 = set()
vegetables2.add("Egg Plant")
vegetables2.add("Sweet Potatoes")
vegetables2.add("Green Beans")
print(vegetables2)

print(vegetables | vegetables2)

vegetables2.add("Potatoes")
print(vegetables2)

print(vegetables & vegetables2)

print(vegetables - vegetables2)

vegetables2.pop()
print(vegetables2)
