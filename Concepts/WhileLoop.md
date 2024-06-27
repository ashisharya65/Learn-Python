
# Python `while` Loop Examples

## Basic `while` Loop

A basic `while` loop continues to execute as long as its condition is true.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

**Output:**
```
0
1
2
3
4
```

## `while` Loop with `else`

The `else` block in a `while` loop executes when the loop condition becomes false.

```python
i = 0
while i < 3:
    print(i)
    i += 1
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

## Infinite `while` Loop

An infinite loop runs indefinitely unless stopped.

```python
while True:
    print("This loop runs forever")
    break  # Remove this line to see the infinite loop in action
```

**Output:**
```
This loop runs forever
```

## `while` Loop with `break`

The `break` statement terminates the loop completely.

```python
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
```

**Output:**
```
0
1
2
3
4
```

## `while` Loop with `continue`

The `continue` statement skips the rest of the code inside the loop for the current iteration only.

```python
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
```

**Output:**
```
1
2
3
4
6
7
8
9
10
```

## `while` Loop with `pass`

The `pass` statement does nothing and can be used as a placeholder for future code.

```python
i = 0
while i < 5:
    if i == 3:
        pass
    print(i)
    i += 1
```

**Output:**
```
0
1
2
3
4
```
