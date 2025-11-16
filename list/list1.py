fruits = []
fruits = [ "Water melon", "grapes", "banana"]

print(fruits)           # ['Water melon', 'grapes', 'banana']
print(" ".join(fruits))  # Water melon grapes banana

fruits.append("fig")
print(fruits)

print(fruits[-1])  # last element
print(fruits[-2])  # second last

fruits.insert(1, "orange")      # insert at index 1
print(fruits)

fruits.remove("banana")
print(fruits)

# negative indexing
print(fruits[-1])  # fig