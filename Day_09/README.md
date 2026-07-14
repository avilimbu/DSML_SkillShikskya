# Day 09

## Python While Loop

A **while loop** repeatedly executes a block of code as long as a specified condition evaluates to `True`. It is useful when the number of iterations is unknown beforehand.

### Syntax

```python
while condition:
    # Code to execute
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```
1
2
3
4
5
```

---

## Infinite Loop

An **infinite loop** is a loop that never ends because its condition always remains `True`. Infinite loops are commonly used in games, servers, and menu-driven programs until a `break` statement is encountered.

### Example

```python
while True:
    print("Program is running...")
```

### Output

```
Program is running...
Program is running...
Program is running...
...
```

*(The program continues until it is manually stopped.)*

---

## Break Statement

The **break** statement immediately terminates the loop, even if the loop condition is still `True`.

### Example

```python
count = 1

while count <= 5:
    if count == 3:
        break

    print(count)
    count += 1
```

### Output

```
1
2
```

---

## Continue Statement

The **continue** statement skips the current iteration and moves directly to the next iteration of the loop.

### Example

```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)
```

### Output

```
1
2
4
5
```

---

## Pass Statement

The **pass** statement is a placeholder that performs no action. It is used when a statement is syntactically required but no code needs to be executed.

### Example

```python
count = 1

while count <= 4:
    if count == 2:
        pass
    else:
        print(count)

    count += 1
```

### Output

```
1
3
4
```

---

# Range

The **`range()`** function generates a sequence of numbers. It is commonly used with `for` loops to repeat a block of code a specific number of times.

### Syntax

```python
range(stop)
```

or

```python
range(start, stop)
```

or

```python
range(start, stop, step)
```

### Example

```python
for i in range(5):
    print(i)
```

### Output

```
0
1
2
3
4
```

---

## For Range Loop (`start`, `stop`)

The `range(start, stop)` function starts from the **start** value and stops **before** reaching the **stop** value.

### Example

```python
for i in range(2, 7):
    print(i)
```

### Output

```
2
3
4
5
6
```

---

## For Range Loop (`start`, `stop`, `step`)

The `range(start, stop, step)` function allows you to specify the increment (or decrement) between numbers.

### Example

```python
for i in range(2, 11, 2):
    print(i)
```

### Output

```
2
4
6
8
10
```

---

# While Loop vs For-Range Loop

| Feature | While Loop | For-Range Loop |
|---------|------------|----------------|
| Purpose | Executes while a condition is `True`. | Iterates over a fixed range of values. |
| Number of Iterations | Usually unknown before execution. | Usually known before execution. |
| Condition | Controlled by a Boolean condition. | Controlled by the `range()` function. |
| Counter Update | Must be updated manually. | Updated automatically by `range()`. |
| Risk of Infinite Loop | High if the condition never becomes `False`. | Very low when using `range()`. |
| Best Used For | Menu-driven programs, user input, real-time systems. | Counting, traversing ranges, repeated tasks. |
| Syntax | `while condition:` | `for variable in range(...):` |

---

# Key Takeaways

- A **while loop** runs until its condition becomes `False`.
- An **infinite loop** continues forever unless stopped using `break`.
- **break** exits a loop immediately.
- **continue** skips the current iteration.
- **pass** acts as a placeholder without performing any action.
- **range()** generates a sequence of numbers for iteration.
- Use **while loops** when the number of iterations is unknown.
- Use **for-range loops** when the number of iterations is known in advance.
```