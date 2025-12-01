

keys = []
values = []
size = 0

# Insert / update: put('apple', 3)
k = "apple"; v = 3
for i in range(len(keys)):
    if keys[i] == k:
        values[i] = v
        break
else:
    keys.append(k)
    values.append(v)
    size += 1

# Insert another: put('banana', 5)
k = "banana"; v = 5
for i in range(len(keys)):
    if keys[i] == k:
        values[i] = v
        break
else:
    keys.append(k)
    values.append(v)
    size += 1

# Update existing: put('apple', 10)
k = "apple"; v = 10
for i in range(len(keys)):
    if keys[i] == k:
        values[i] = v
        break
else:
    keys.append(k)
    values.append(v)
    size += 1

# Get: get('apple')
k = "apple"
found = False
for i in range(len(keys)):
    if keys[i] == k:
        print("get", k, "->", values[i])
        found = True
        break
if not found:
    print("get", k, "->", None)

# Contains: contains('orange')
k = "orange"
found = False
for i in range(len(keys)):
    if keys[i] == k:
        found = True
        break
print("contains 'orange'?", found)

# Remove: remove('banana')
k = "banana"
for i in range(len(keys)):
    if keys[i] == k:
        keys.pop(i)
        values.pop(i)
        size -= 1
        print("removed", k)
        break
else:
    print(k, "not found to remove")

# Iterate items
print("items:")
for i in range(len(keys)):
    print(keys[i], ":", values[i])

print("size =", size)
# ...existing code...