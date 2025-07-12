## **Lists in Python**
A list is a collection of items that are **ordered**, **mutable** (changeable), and **allow duplicate elements**. Lists can hold items of different data types, such as integers, strings, or even other lists.
lists are denoted with [ ](square brackets}

### **Example**:
```python
fruits = ["Apple", "Banana", "Strawberry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Apple", 1, True]
```
### **List Operations**:
#### **1.Accessing List Elements**:
can access individual elements in list using the indexs
Example:
```python
print(fruits[0]) #Here it gives the Apple as a output
```
like this we can accesss any character using the index value
We can access elements from the end of a list or string using negative indexing. For example, -1 refers to the last element, -2 refers to the second last element, and so on.
```python
print(fruits[-1]) #Here it gives the cherry as a output
```
#### **2.Modifying the List Elements**:
Lists are mutable, which means you can change the value of items in a list.
Example:
#### *changing the specific element*:
```python
fruits[1] = "orange"
print(fruits)  # Output: ['Apple', 'orange', 'Strawberry']
```
#### *Adding elements*:
There are two ways to add the elements into a list 
#### **1.Append**: Which will append (add) the element to the end of the list 
```python
fruits.append("grape")
print(fruits)  # Output: ['Apple', 'orange', 'Strawberry', 'grape']
```
#### **2.Insert**: which is used to insert the element at the specified location
```python
fruits.insert(1, "Lichi")
print(fruits)  # Output: ['Apple', 'Lichi','orange', 'Strawberry', 'grape']
```
#### *Removing element*:
1.### *remove()* : Removes the first occurrence of an element.
```python
fruits.remove("orange")
print(fruits)  # Output: [Apple','Strawberry', 'grape']
```
2.### *pop()*: Removes the element at a specific index (or the last item if no index is provided).
```python
fruits.pop()  # Removes the last item
print(fruits)  # Output: [Apple','Strawberry']

fruits.pop(0)  # Removes the first item
print(fruits)  # Output: ['Strawberry']
```
3.### *clear()*: Removes all elements from the list.
```python
fruits.clear()
print(fruits)  # Output: []
```
### **Slicing Lists**
We can extract a portion of a list using slicing.

Syntax:
list_name[start:stop:step]
- start: The index to start the slice (inclusive).
- stop: The index to stop the slice (exclusive).
- step: The number of steps to skip elements (default is 1).
```python
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)
```

#### **. List Functions and Methods**:
Python provides several built-in functions and methods for working with lists.
List methods: 
- Modify original list, use dot notation (list.method())
- List methods as actions a list can do to itself(mainly for the lists only)
Built-in functions:
- Create new values, called directly (function(list))
- Built-in functions as tools that work with many types of data
### *Example*:
```python
# List of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# List Methods (using dot notation)
numbers.append(8)      # Adds 8 to the end
numbers.sort()         # Sorts in-place
numbers.reverse()      # Reverses in-place
numbers.clear()        # Removes all items
print(numbers.index(4))  # Output: 2
print(numbers.count(1))  # Output: 2

# Built-in Functions
length = len(numbers)  # Returns length
maximum = max(numbers) # Returns maximum value
minimum = min(numbers) # Returns minimum value
sorted_nums = sorted(numbers) # Returns new sorted list without changing the original list.
sum_elements=sum(numbers) #returns sum of the list elements
```
#### **Nested Lists**
Lists can contain other lists, allowing you to create nested lists. This can be useful for storing matrix-like data structures.
- if we access that with index it gives the row value eg: matrix[0] which returns the 0th row
- matrix[0][1] returns the element in the 0th row and 1st column.
