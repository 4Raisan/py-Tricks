'''
.split() - divided with specific character inside ("□") and make list
          - default () is divided by space.
'''

food = "apple,ban ana,orange"

things = food.split(",")
print()  # ['apple', 'ban ana', 'orange']

lst = food.split()
print(lst)  # ['apple,ban', 'ana,orange']

############################################################################

''' .strip() - Both Ends

# .strip() - remove whitespaces or specific_charactor form BOTH-ENDS of the string.
# .lstrip() removes only from the left (start).
# .rstrip() removes only from the right (end).

Whitespaces:
         >  Space (' ')   |   Tab ('\t')   |   Newline ('\n')
         >  Carriage Return ('\r') – Used in Windows line endings (\r\n).
         >  Vertical Tab ('\v') – Rarely used.
         >  Form Feed ('\f') – Page break character. 
'''

text = '  Hello Rashen  \n'
print(text.strip())   # 'Hello Rashen'
print(text.lstrip())  # 'Hello Rashen  \n'
print(text.rstrip())  # '  Hello Rashen'

text2 = '19 7 Sri Lanka Rx x'
print(text2.strip('1 Rx'))  # '9 7 Sri Lanka'
print(text2.lstrip('19'))   # ' 7 Sri Lanka Rx x'
print(text2.rstrip(' x'))    # '19 7 Sri Lanka R'
