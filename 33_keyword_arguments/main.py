
#! keyword arguments = an argument preceded by an identifier
#?                     helps with readability
#?                     order of arguments doesn't matter
#*                     1. positonal 2. default 3. KEYWORD 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")

#TODO: Another Example

# for x in range(1, 11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+63", area="912", first="345", last="6789")

print(phone_num)