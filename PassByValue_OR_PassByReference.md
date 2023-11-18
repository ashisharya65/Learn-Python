# PassByValue Or PassByReference

In Python, arguments are passed by assignment, which means that the way values are passed to functions depends on the type of the object being passed:

1. <b>Immutable Objects (e.g., integers, strings, tuples):</b>
    When you pass an immutable object to a function, a new local variable with the same value is created. Changes made to this local variable do not affect the original object.

```python
       def modify_value(num):
            num += 10
            print("Inside function:", num)

       x = 5
       modify_value(x)
       print("Outside function:", x)

       # Output:
       # Inside function: 15
       # Outside function: 5
```
    
In this example, <b>x</b> is an integer (an immutable object). When x is passed to <b>modify_value</b>, a new local variable <b>num</b> is created, which initially has the same value as x. 
    However, when num is modified, it does not affect the original variable x.

3. <b>Mutable Objects (e.g., lists, dictionaries):</b>
    When you pass a mutable object to a function, a new local variable is created, but it refers to the same object in memory.
    This means that changes made to the object inside the function will affect the original object.

```python
        def modify_list(my_list):
            my_list.append(30)
            print("Inside function:", my_list)

        my_list = [10, 20, 25]
        modify_list(my_list)
        print("Outside function:", my_list)
        
        # Output:
        # Inside function: [10, 20, 25, 30]
        # Outside function: [10, 20, 25, 30]

```
    
In this example, <b>my_list</b> is a list (a mutable object). When it is passed to <b>modify_list</b>, the function receives a reference to the same list.
    Therefore, any modifications made to the list inside the function are reflected in the original list.

So, in Python, it's more accurate to say that it uses a form of "pass by object reference". 
The crucial point to remember is that whether changes to an object inside a function affect the original object or not depends on whether the object is mutable or immutable.
         
