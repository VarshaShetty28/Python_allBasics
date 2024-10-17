## **Conditional Statements in Python: `if`, `elif`, and `else`**

In programming, **conditional statements** are used to perform different actions based on different conditions. Python uses `if`, `elif`, and `else` statements to allow your program to make decisions.

### **1. The `if` Statement**

The `if` statement is used to test a condition. If the condition is **True**, the block of code under the `if` statement is executed.

#### **Syntax**:
```python
if condition:
    # Code block to execute if the condition is True
```

### **2. The `else` Statement**

The `else` statement provides an alternative block of code to execute when the `if` condition is **False**.

#### **Syntax**:
```python
if condition:
    # Code block if the condition is True
else:
    # Code block if the condition is False
```
### **3. The `elif` Statement**

The `elif` (short for "else if") statement checks another condition if the previous `if` or `elif` condition was False. You can have multiple `elif` statements to test various conditions.

#### **Syntax**:
```python
if condition1:
    # Code block if condition1 is True
elif condition2:
    # Code block if condition2 is True
else:
    # Code block if none of the above conditions are True
```
## **While Loops in Python**

A **loop** is a programming structure that repeats a set of instructions as long as a specified condition is True. In Python, the **`while` loop** allows you to repeatedly execute a block of code as long as the condition is True.

### **1. The Basic Structure of a `while` Loop**

The `while` loop repeatedly executes a block of code as long as the condition is `True`.

#### **Syntax**:
```python
while condition:
    # Code to execute as long as condition is True
```

Overall Example
### ** Real-life Example:redbus Availability**

Let’s say you want to simulate a  redbus seat booking system. The bus has 5 available seats. Each time a seat is booked, the available seats decrease.

```python
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")
```

Here, the loop keeps running until all seats are booked. It checks the available seats and asks the user if they want to book one. The loop stops when there are no more seats available.

**Output Example**:
```
5 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
4 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
...
1 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
All seats are booked!
```
## **For Loops in Python**

In Python, a **`for` loop** is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code repeatedly for each element in the sequence.

### **1. The Basic Structure of a `for` Loop**

A **`for` loop** allows you to repeat a block of code a fixed number of times, or once for each element in a sequence.

#### **Syntax**:
```python
for item in sequence:
    # Code to execute for each item in the sequence
```
### **2. Using `range()` with `for` Loops**

The `range()` function generates a sequence of numbers, which you can use in a `for` loop when you want to repeat a block of code a specific number of times.

#### **Syntax of `range()`**:
```python
range(start, stop, step)
```
- `start`: The starting value (inclusive).
- `stop`: The ending value (exclusive).
- `step`: The increment (optional, default is 1).

### **3. Looping Over Strings**

You can also loop over each character in a string using a `for` loop.

#### **Example**: Printing each character in a string
```python
name = "Karnataka"
for letter in name:
    print(letter)
```

**Output**:
```
K
a
r
n
a
t
a
k
a
```

This loop goes through the string `"Karnataka"` one character at a time.
### **7. Looping Through a List with `enumerate()`**

The `enumerate()` function allows you to loop over a sequence and get both the index and the value of each item.
basically enumerator means which will provide the each character and its index in string and items if it list and so on 

#### **Example**: Displaying the index and value of each city
```python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}")
```

**Output**:
```
City 1: Bengaluru
City 2: Mysuru
City 3: Hubballi
City 4: Mangaluru
```
### **8. Using `else` with `for` Loops**

You can also use an **`else` clause** with a `for` loop. The code inside the `else` block will execute once the loop finishes, unless the loop is terminated by a `break` statement.

#### **Example**:
```python
for city in cities:
    print(city)
else:
    print("No more cities!")
```

**Output**:
```
Bengaluru
Mysuru
Hubballi
Mangaluru
No more cities!
```

In this case, after the loop has finished going through all the cities, it prints `"No more cities!"`.

### **9. Real-Life Example: Distributing pens**

Imagine you have 5 pens to distribute among friends. You can use a `for` loop to give each friend one laddu.

```python
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya"]

for friend in friends:
    if pens > 0:
        print(f"{friend} gets a pen!")
        pen -= 1
    else:
        print("No pens left!")
```

**Output**:
```
Rahul gets a pen!
Sneha gets a pen!
Aman gets a pen!
Priya gets a pen!
No pens left!
```

Here, the loop goes through the list of friends and distributes the pens one by one.

---
