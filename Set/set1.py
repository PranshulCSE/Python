# Basic set declaration and iteration examples

# Declare a set with some values
my_set = {1, 2, 3, "apple", "banana"}

print("Set contents (unordered):", my_set)

# Iterate over set elements (order is arbitrary)
for item in my_set:
    print("Item:", item)

# Can't index a set (this would raise TypeError):
# first = my_set[0]  # uncommenting this will fail

# If you need an index or stable order, convert to a list
for index, item in enumerate(list(my_set)):
    print(index, item)

# Empty set must be created with set()
empty = set()
print("Empty set:", empty)