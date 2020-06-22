'''
Definition

A dictionary is a collection of key/value pairs, very similar to lists except you use keys instead of indexes to access the values in it. 

Syntax:

d = { key1: val1, key2: val2, ... }

A key can be of any immutable data type.

'''


#d = { [1,2] : True }
#print(d)
d = { (1,2) : True }
print(d)


emails = {} or dict()

emails = { "David" : "david.r@abc.com" }

#Accessing
emails = { "David" : "david.r@abc.com" }

print (emails["David"])

print (emails["Sam"])

print (emails.get("Sam", None))

#Add
emails["Brian"] = "brian123@testmail.com"
emails["Tom"] = "tom.sawyer@xyz.com"

#Modify
emails["David"] = "david.s@abc.com"

#Remove
del emails["David"]

#update
new_emails = { "David" : "david.r@xyz.com", "Sam" : "sam.wes@testmail.com" }

emails.update(new_emails)

#pop, popitem

element = emails.pop("Sam")
print(element)

emails["Sam"] = "sam.wes@testmail.com"
element = emails.popitem()
print(element)

#items, keys and values
emails.items()
emails.keys()
emails.values()

#len
len(email)

#clear
emails.clear()
print(emails)
