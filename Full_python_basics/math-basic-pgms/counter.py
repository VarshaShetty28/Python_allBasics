#You are given a number ’n’.Find the number of digits of ‘n’ that evenly divide ‘n’.Note: A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.

num = int(input("Enter the number: "))  # Convert input to integer
count = 0

for i in str(num):  # Iterate through digits as strings
    d = int(i)  # Convert each character back to integer
    if d != 0 and num % d == 0:  # Check if digit divides num
        count += 1  # Increment count if condition is met

print(count)  # Output the count of digits that evenly divide num

