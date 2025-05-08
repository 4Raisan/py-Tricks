'''
for item in iterable:
    # do something with item
'''
# All output come Line-by-Line
# break - stop whole loop
# continue - skip just one iterations 

#------------------------------------------------#

#1. One-liner loop (no result stored):
for i in range(5): print(i)

#2. List comprehension (to create a list):
squares = [i**2 for i in range(5)]
print(squares)

#3. One-liner with condition:
evens = [i for i in range(10) if i % 2 == 0]
print(evens)

#------------------------------------------------#

# Going through Dataset
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Going through range (start, end, step)
for i in range(1,5,2):
    print(i)

# Going through string using str index
for letter in "hello":
    print(letter)



