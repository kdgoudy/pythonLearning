#Creates standard list
list1 = ["Tiki", "Cinnamon", "River", "Ziggy", "Bane", "Panda", "Auli'i"]
print(list1)

#Prints list item on new line
for i in list1:
  print(i)

#Calls list item from list. In this case is calling fourth to last list item
print(list1[-4])

#Adding new item to end of list
list1.append("Parker")
print(list1)

#Removing item from the end of list
list1.pop()
print(list1)

#Sorts list alphabetically 
list1.sort()
print(list1)

#Reverses list order
list1.reverse()
print(list1)
