# keys(), values(), items()
d = {'name': 'Ali', 'age': 20}
print(list(d.keys())) # ['name', 'age']
print(list(d.values())) # ['Ali', 20]
print(list(d.items())) # [('name', 'Ali'), ('age', 20)]

# pop(key)
age = d.pop('age')
print(age, d) # 21 {'name': 'Ali', 'city': 'Lahore'}
