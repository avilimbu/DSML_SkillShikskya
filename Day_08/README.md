# Day 08 | Conditional Statements

> **Theory**

## What are Conditions?

A **condition** is an expression that evaluates to either **True** or **False**. It helps a program decide which block of code should be executed.

### Real-Life Example

- If it is raining, carry an umbrella.
- If you pass the exam, you get promoted.

In Python, conditions are commonly created using **comparison operators** and are used with decision-making statements.

---

# Branching in Python

**Branching** is the process of executing different blocks of code depending on whether a condition is true or false.

Python provides several ways to perform branching:

- `if`
- `if...else`
- `if...elif...else`
- Nested `if`
- Ternary Operator

---

# The `if` Statement

The `if` statement executes a block of code only when the condition is **True**.

## Syntax

```python
if condition:
    # code to execute
```

## Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

### Output

```
Eligible to vote
```

---

# The `if...else` Statement

The `else` block executes when the condition is **False**.

## Syntax

```python
if condition:
    # executes if condition is True
else:
    # executes if condition is False
```

## Example

```python
age = 10

if age <= 12:
    print("Travel for free")
else:
    print("Pay for ticket")
```

### Output

```
Travel for free
```

---

# The `if...elif...else` Statement

Used when multiple conditions need to be checked.

Python evaluates the conditions from top to bottom and executes the first matching block.

## Syntax

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...
```

## Example

```python
age = 25

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young Adult")
else:
    print("Adult")
```

### Output

```
Young Adult
```

---

# Nested `if` Statement

A nested `if` means placing one `if` statement inside another.

It is useful when one condition should only be checked after another condition becomes true.

## Example

```python
age = int(input("Enter your age: "))

if age >= 18:
    citizenship = input("Are you a citizen? (yes/no): ")

    if citizenship == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are under 18.")
```

---

# Another Nested `if` Example

```python
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
```

---

# Ternary Operator

The **Ternary Operator** is a shorthand way of writing an `if...else` statement.

## Syntax

```python
value_if_true if condition else value_if_false
```

## Example

```python
n = int(input("Enter a number: "))

print("Even" if n % 2 == 0 else "Odd")
```

---

# Comparison Operators

Comparison operators compare two values and always return either **True** or **False**.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

## Example

```python
alpha = 7

print(alpha == 6)
```

### Output

```
False
```

---

# Logical Operators

Logical operators combine multiple conditions.

Python provides three logical operators:

- `and`
- `or`
- `not`

---

## `and` Operator

Returns **True** only if **both conditions are True**.

### Example

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

### Output

```
Eligible to vote
```

---

## `or` Operator

Returns **True** if **at least one condition is True**.

### Example

```python
username = "admin"
password = "1234"

if username == "admin" or password == "admin123":
    print("Access granted")
```

### Output

```
Access granted
```

---

## `not` Operator

Reverses the result of a condition.

- `True` becomes `False`
- `False` becomes `True`

### Example

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in first")
```

### Output

```
Please log in first
```

---

# `any()` Function with `if`

The `any()` function returns **True** if **at least one element** in an iterable is True.

## Example 1

```python
marks = [25, 30, 45, 20]

if any(mark >= 40 for mark in marks):
    print("At least one student passed")
```

### Output

```
At least one student passed
```

---

## Example 2

```python
is_admin = False
is_teacher = True

if any([is_admin, is_teacher]):
    print("Access granted")
```

### Output

```
Access granted
```

---

# `all()` Function with `if`

The `all()` function returns **True** only if **every element** in an iterable is True.

## Example 1

```python
marks = [50, 60, 70]

if all(mark >= 40 for mark in marks):
    print("All students passed")
```

### Output

```
All students passed
```

---

## Example 2

```python
name = "Ram"
email = "ram@gmail.com"
phone = "9841000000"

if all([name, email, phone]):
    print("Form submitted")
```

### Output

```
Form submitted
```

---
