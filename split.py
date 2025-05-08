# .split() - divided with specific character inside ("□") and make list
           # - default () is divided by space.
           
food = "apple,ban ana,orange"

things = food.split(",")
print()  # ['apple', 'ban ana', 'orange']

lst = food.split()
print(lst)  # ['apple,ban', 'ana,orange']
