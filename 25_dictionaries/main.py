
#! dictionary = a collection of {key:value} pairs
#?              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") #? To remove
# capitals.popitem() #? Will remove the latest item
# capitals.clear() #? Clear the dictionary

# keys = capitals.keys() #* To get the keys or yung MAIN
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values() #* Will return the object
# print(values)

# for value in capitals.values():
#     print(value)

# items = capitals.items() #* To list all like tuple
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")