# map() - acts as iteratively and move from iteam to iteam
#       - must be mention the data type we want inside the map(int, ...)
#       - when in inputs, inputs must be seperated in spaces or we must use .split("□") at the end

# map(int, ###) - convertering the iteams while iterating 
# list(map(int, ####)) - make list from iterations

# list(map(int, input('Enter names::: ').split(",")))  - use .split("□") at the end of the input
# lsit(map(str.strip, input('Enter::: ').split("/")))  - avoid whitespaces on the iteams after they splitted
# list(map({function name}, {list_1}, {list_2})) - use with functions

# 1
numbers = ["1", "2", "3"]
int_numbers = list(map(int, numbers)) # make list with converting strings to int
print(int_numbers)  # [1, 2, 3]

# 2
names = list(map(str.strip, input('Enter names::: ').split("/")))  # ::: A/B/  C/D/E F
# inputs must be seperated by the "/"
# avoid whitespaces on the iteams after they splitted
print(names)  # ['A', 'B', 'C', 'D', 'E F']

# 3 
names_2 = list(map(str, input('Enter names::: ').split("/")))  # ::: A/B/  C/D/E F
# inputs must be seperated by the "/"
print(names_2)  # ['A', 'B', '  C', 'D', 'E F']
