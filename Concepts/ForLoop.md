# Looping over Lists
Looping over the lists using For loop.
```python
mylist = [1, 2, 3, 4, "Python", "is", "neat"]
for item in mylist:
    print(item,end=" ")
```

# break keyword
Use <b>break</b> keyword to stop the execution of loop.
```python
for item in mylist:
    if item == "Python":
        break
    print(item,end=" ")
```

# continue keyword
Use <b>continue</b> keyword to continue  to the next item without executing the lines occuring after continue inside the loop.
```python
for item in mylist:
    if item == 1:
        continue
    print(item,end=" ")
```

# enumerate() method
Use <b>enumerate()</b> method to get index of the list.
```python
for idx, val in enumerate(mylist):
    print(f"Key: {idx}, Value: {val}")
```

# Looping over dictionary
```python
mydict = {"name" : "Ashish Arya",
          "Age" : 22,
          "Location" : "India",
          "Email" : "abc@gmail.com"
        }

# Getting the values from the dictionary
for val in mydict:
    print(val,end=" ")
print("\n")

# Getting the keys and values of a dictionary
for key,val in mydict.items():
    print(f"Key: {key}, Value: {val}")
```

# range() function
Python's <b>range()</b> function is used with for loops.
```python
# Use the range() function with only the stop argument
for num in range(5):
    print(num,end=" ")
print()

# Use the range() function with start & stop arguments
for num in range(1,5):
    print(num,end=" ")
print()

# Use the range() function with start, stop & step arguments
for num in range(1,10,2):
    print(num,end=" ")
print()
```
