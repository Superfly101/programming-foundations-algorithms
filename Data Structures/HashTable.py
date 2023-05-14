# Create hashtable all at once
items1 = dict({"key1": 1, "key2": 2, "key3": "three"})

print(items1)
# Creat a hashtable pro
# gressively
items2 = {}

items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3

print(items2)

print(items1.items())

# iterate the keys and values in the dictionary
for key, value in items2.items():
    print("key: ", key, "value: ", value)
