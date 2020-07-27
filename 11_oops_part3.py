# ability to leverage the same interface for different underlying forms such as data types or classes

# Polymorphism allows for flexibility and loose coupling so that code can be extended and easily maintained over time.


# Polymorphism - the condition of occurring in several different forms

+
[]

print(5 + 6)
print("Hello" + "World")

str = "Hello"
str[0]

l = ["a","b","c","d"]
l[2]


# creating class methods as Python allows different classes to have methods with the same name

class Browser:
	def __init__(self):
		print("Browser is created.")

	def open_website(self, address):
		print(f"Going to www.{address}.com")

	def About():
		print("I am a Browser.")

class Chrome(Browser):
    def __init__(self):
        print("Chrome Browser Created")

    def About(self):
        print("Version: 83.0.4103.116 64-bit")

    def Extension(self):
        print("I have lots of cool extensions.")


class Firefox(Browser):
    def __init__(self):
        print("Firefox Browser Created")

    def About(self):
        print("Version: 78.0.1 64-bit")

    def AddOn(self):
        print("I have lots of cool Add-ons")


c = Chrome()
f = Firefox()


for browse in (c, f):
	browse.About()

c.open_website("google")
f.open_website("facebook")
c.About()
f.About()



