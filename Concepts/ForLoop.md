
# Python `for` Loop Examples

## Basic `for` Loop

A basic `for` loop iterates over a sequence of numbers produced by the `range()` function.

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

## Iterating Over a List

You can use a `for` loop to iterate over each element in a list.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

## Iterating Over a String

A `for` loop can iterate over each character in a string.

```python
for char in "hello":
    print(char)
```

**Output:**
```
h
e
l
l
o
```

## Using `for` Loop with `else`

The `else` block in a `for` loop executes after the loop completes normally (without encountering a `break` statement).

```python
for i in range(3):
    print(i)
else:
    print("Loop is done")
```

**Output:**
```
0
1
2
Loop is done
```

## Nested `for` Loops

You can nest one `for` loop inside another to iterate over multiple sequences.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

**Output:**
```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

## Iterating Over a Dictionary

A `for` loop can iterate over the keys of a dictionary.

```python
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(f"Key: {key}, Value: {d[key]}")
```

**Output:**
```
Key: a, Value: 1
Key: b, Value: 2
Key: c, Value: 3
```

## Using `enumerate` in `for` Loop

The `enumerate()` function adds a counter to an iterable, and returns it as an enumerate object.

```python
names = ["John", "Jane", "Doe"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
```

**Output:**
```
0: John
1: Jane
2: Doe
```

## Using `zip` in `for` Loop

The `zip()` function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

```python
names = ["John", "Jane", "Doe"]
ages = [23, 29, 31]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

**Output:**
```
John is 23 years old
Jane is 29 years old
Doe is 31 years old
```

## List Comprehension with `for` Loop

List comprehensions provide a concise way to create lists. It consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses.

```python
squares = [x ** 2 for x in range(10)]
print(squares)
```

**Output:**
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## `for` Loop with `break`

The `break` statement terminates the loop completely.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Output:**
```
0
1
2
3
4
```

## `for` Loop with `continue`

The `continue` statement skips the rest of the code inside the loop for the current iteration only.

```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```

**Output:**
```
0
1
2
3
4
6
7
8
9
```

## `for` Loop with `pass`

The `pass` statement does nothing and can be used as a placeholder for future code.

```python
for i in range(10):
    if i == 5:
        pass
    print(i)
```

**Output:**
```
0
1
2
3
4
5
6
7
8
9
```

## Using `for` Loop to Read Lines from a File

You can use a `for` loop to iterate over each line in a file.

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

**Output:**
```
(Line by line content of the file example.txt)
```
