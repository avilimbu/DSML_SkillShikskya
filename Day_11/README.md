# Day 11 | Python Function Practice & Built-in Functions

---

# Topics Covered

- Function Practice
- Python Built-in Functions
- File Handling Basics
- Functional Programming (`map()`, `filter()`, `reduce()`)
- Lambda Function

# Python Built-in Functions

Python provides many built-in functions that simplify programming by reducing the amount of code we need to write.

---

## `print()`

Displays output on the screen.

### Useful Parameters

- `sep`
- `end`
- `file`

---

## `input()`

Accepts user input from the keyboard.

**Note:** It always returns data as a string unless explicitly converted.

---

## `type()`

Returns the data type of an object.

Examples

- Integer
- Float
- String
- Boolean
- List
- Dictionary

---

## `len()`

Returns the total number of elements or characters in a sequence.

Works with

- String
- List
- Tuple
- Dictionary
- Set

---

## `dir()`

Displays all available attributes and methods of an object.

Useful while learning Python because it helps discover what operations an object supports.

---

# File Handling

## `open()`

Used to open files.

Common Modes

| Mode | Description |
|------|-------------|
| `r` | Read |
| `w` | Write |
| `a` | Append |
| `r+` | Read and Write |

### Learned

- Reading files
- Writing files
- Closing files
- Reading after writing

---

# `enumerate()`

Adds an index while iterating through a sequence.

Useful when both the index and value are required.

Example Uses

- Numbering students
- Menu systems
- Printing indexed values

---

# `zip()`

Combines multiple iterables into a single iterable.

Useful for iterating through two or more lists simultaneously.

---

# `map()`

Applies a function to every element of an iterable.

### Syntax

```python
map(function, iterable)
```

### Common Uses

- Squaring numbers
- Converting data types
- Applying transformations

---

# `filter()`

Returns only those elements that satisfy a given condition.

### Syntax

```python
filter(function, iterable)
```

### Common Uses

- Filtering even numbers
- Filtering positive values
- Removing unwanted data

---

# `reduce()`

Performs cumulative operations on iterable elements and returns a single value.

### Syntax

```python
from functools import reduce

reduce(function, iterable)
```

### Common Uses

- Sum of numbers
- Product of numbers
- Finding maximum value
- Finding minimum value

---

### About Lambda function

- `lambda` is a built-in **keyword** in Python used to create anonymous functions.
- Anonymous functions do not have a function name.
- They are useful for writing short, one-line functions.
- Lambda functions are commonly used with:
  - `map()`
  - `filter()`
  - `reduce()`
  - `sorted()`

Example:

```python
square = lambda x: x ** 2
print(square(5))   # Output: 25
```

