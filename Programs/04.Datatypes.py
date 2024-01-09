
print("\n################################################################")
print("This is the second script explaining about Datatypes in Python!")
print("################################################################\n")

print("Below are the different type of data types in Python: ")
print("\tText Type\t\t:\tstr \n\tNumeric Types\t\t:\tint, float, complex \n\tSequence Types\t\t:\tlist, tuple, range \n\tMapping Type\t\t:\tdict \n\tSet Types\t\t:\tset, frozenset \n\tBoolean Type\t\t:\tbool \n\tBinary Types\t\t:\tbytes, bytearray, memoryview \n\tNone Type\t\t:\tNoneType\n")

# Setting the data type
a = "Hello World"
b = ["apple", "banana", "cherry"]
c = ("apple", "banana", "cherry")
d = range(6)
e = {"name" : "John", "age" : 36}
f = {"apple", "banana", "cherry"}
g = frozenset({"apple", "banana", "cherry"})

# Setting the Specific Data Type
h = str("Hello World")	
i = int(20)
j = float(20.5)
k = complex(1j)
l = list(("apple", "banana", "cherry"))	
m = tuple(("apple", "banana", "cherry"))	
n = range(6)	
o = dict(name="John", age=36)	
p = set(("apple", "banana", "cherry"))	
q = frozenset(("apple", "banana", "cherry"))	
r = bool(5)		
s = bytes(5)	
t = bytearray(5)	
u = memoryview(bytes(5)) 

# printing all the values using eval() function & chr() function
print("Printing variable values using chr() & eval() functions.")
for i in range(97,118):
    print(f"Value of {chr(i)}: {eval(chr(i))}")

# Second way of prniting all the values using the globals() funtion and chr() functio
print("\nSecond way of printing all the variable values using chr() & globals() functions.")
for i in range(97,118):
    print(f"Value of {chr(i)}: {globals()[chr(i)]}")

