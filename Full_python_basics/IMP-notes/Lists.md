## **Lists in Python**
A list is a collection of items that are **ordered**, **mutable** (changeable), and **allow duplicate elements**. Lists can hold items of different data types, such as integers, strings, or even other lists.
lists are denoted with [ ](square brackets}

###**Example**:
```python
fruits = ["Apple", "Banana", "Strawberry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Apple", 1, True]
```
###**List Operations**:
**1.Accessing List Elements:
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
**2.Modifying the List Elements:
Lists are mutable, which means you can change the value of items in a list.
Example:
*changing the specific element:
```python
fruits[1] = "orange"
print(fruits)  # Output: ['Apple', 'orange', 'Strawberry']
```
*Adding elements:
There are tqwo ways ti add the element into a list 
**1.Append: Which will append (add) the element to the end of the list 
```python
fruits.append("grape")
print(fruits)  # Output: ['Apple', 'orange', 'Strawberry', 'grape']
```
**2.Insert: which is used to insert the element at the specified location
```python
fruits.insert(1, "Lichi")
print(fruits)  # Output: ['Apple', 'Lichi','orange', 'Strawberry', 'grape']
```
                      
