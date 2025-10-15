# keys(), values(), items()
d = {'name': 'Ali', 'age': 20}
print(list(d.keys())) # ['name', 'age']
print(list(d.values())) # ['Ali', 20]
print(list(d.items())) # [('name', 'Ali'), ('age', 20)]

# popitem()
k, v = d.popitem()
print(k, v, d) # 'city' 'Lahore' {'name': 'Ali'}