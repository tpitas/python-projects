# Implements linear search for names using loop

# A list of names
names = ["Jordan", "James", "O'neill", "Johnson"]

# Ask for name
name = input("Name: ")

# Search for name
for n in names:
    if name == n:
        print(f" {name} Found in list ")
else:
    print(f" {name} Not found in list")