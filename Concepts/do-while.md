
# Python `do-while` Loop Examples (Simulated with `while True` and `break`)

Python does not have a built-in `do-while` loop, but you can simulate it using `while True` and `break`.

## Basic `do-while` Loop Simulation

A `do-while` loop runs the block of code once before checking the condition.

```python
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break
```

**Output:**
```
0
1
2
3
4
```

## `do-while` Loop with User Input Simulation

Simulating a `do-while` loop to take user input until a specific condition is met.

```python
while True:
    user_input = input("Enter a number (0 to stop): ")
    if user_input == "0":
        break
    print(f"You entered: {user_input}")
```

**Output:**
```
Enter a number (0 to stop): 5
You entered: 5
Enter a number (0 to stop): 3
You entered: 3
Enter a number (0 to stop): 0
```
