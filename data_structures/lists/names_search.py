# Linear Search using in

names = ["Jordan", "James", "O'neill", "Johnson"]
item = "Johnson"

def search(item, listing):
    for element in listing:
        if element == item:
            return True
    return False

print(search(item, names))
index = names.index(item)