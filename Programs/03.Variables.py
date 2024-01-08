
print("\n########################################################")
print("This is a script explaining about variables in Python!")
print("########################################################\n")

fname = "Ashish"
lname = "Arya"
age = 30

print(f"My name is {fname} {lname} and I am {age} years old.")

print("\nType Casting is done in two ways: ")
print("1. Implicit")
print("2. Explicit")
while True:
    option=input("Enter your choice: ")
    match option:
        case "1":
                print("In implicit typecasting, python converts the datatype into another datatype automatically.")
        case "2":
                print("In explicit typecasting, Python needs user involvement to convert the variable data type into the required data type.")
        case _:
                print("Invalid input so please enter 1 or 2.")
    user_input = input("Enter your input again - (y/n): ")
    if user_input.casefold() == "n".casefold():
        print("Exiting the script.")
        break
            
            
