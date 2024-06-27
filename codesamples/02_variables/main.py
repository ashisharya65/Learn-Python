
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one": 1, "two": 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring the variables
myint = "abc"
print(myint)

# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[4])

# use slices to get parts of a sequence
print(mylist[1:4])
print(mylist[1:5:2])            # Skipping every second element from the list

# reversing a sequence
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["one"])

# error : cannot combine variables of different types
print("string type:" + str(123))

# Global vs Local Variables


def myFunction():
    global mystr
    mystr = "def"
    print(mystr)


myFunction()
print(mystr)
