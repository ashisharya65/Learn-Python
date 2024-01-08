
print("\n########################################################")
print("This is a script explaining about variables in Python!")
print("########################################################\n")

# declaring variables
fname = "Ashish"
lname = "Arya"
age = 38

print(f"First variable : {fname} \nSecond variable : {lname} \nThird variable : {age}")

# Use of type() function
print("\nUse of type() function is to get the type of variable: ")
x = "Karan"
y = 20
print(f"Type of variable x : {type(x)} \ntype of variable y : {type(y)}\n")

# Global variable
a = "awesome"
print(f"Value of a outside the function : {a}")
def myfunc():
    a = "fantastic"
    print(f"Value of a inside the function : {a}")
myfunc()
print(f"Value of a outside the function : {a}")

print("\nWith global keyword with in the function , local variable belongs to the global scope.\nYou can also change the value of a variable using the global keyword.")
b = "awesome"
print(f"Value of b outside the function : {a}")
def myfunc2():
    global b
    b = "great"
    print(f"Value of b inside the function : {b}")
myfunc2()
print(f"Value of b outside the function : {b}")





