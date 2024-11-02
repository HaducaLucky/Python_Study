
#! collection = single "variable" used to store multiple values
#* List = [] ordered and changeable, Duplicates OK
#* Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
#* Tuple = () ordered and unchangeable, Duplicate OK. FASTER

#TODO: List

# fruits = ["apple", "orange", "banana", "coconut",]
#* print(dir(fruits))
#? print(help(fruits))
#* print(len(fruits))
#! print("haha" in fruits)

# fruits[1] = "pineapple"
# fruits.append("pineapple") #? To add an element on the list
# fruits.remove("apple") #? To remove
# fruits.insert(3, "pineapple") #? To insert
# fruits.sort() #? To sort A-Z
# fruits.reverse() #? Revers NOT alphabetical but on the oder on the list
# fruits.sort() #?% To revers add sort
# fruits.reverse() #?% then reverse
# fruits.clear() #? To clear all the element on the list
# print(fruits.index("apple")) #? To find the number
# print(fruits.count("banana")) #? To count how many

# print(fruits)

# for fruit in fruits:
#     print(fruit)

#TODO: Set
#? Set is Ok for like colors

fruits = {"apple", "orange", "banana", "coconut", "coconut"}
#* print(dir(fruits))
#? print(help(fruits))
#* print(len(fruits))
#! print("haha" in fruits)

# fruits.add("pineapple") #? To add
# fruits.remove("apple") #? To add
# fruits.pop() #? To remove but random
# fruits.clear() #? To clear all the element on the list

# print(fruits)

#TODO: Tuple

fruits = ("apple", "orange", "banana", "coconut", "coconut")
#* print(dir(fruits))
#? print(help(fruits))
#* print(len(fruits))
#! print("haha" in fruits)

# print(fruits.index("apple")) #? To fint what index number
# print(fruits.count("coconut")) #? To count how many

# print(fruits)
for fruit in fruits:
    print(fruit)

