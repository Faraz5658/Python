# keys(), values(), items()
d = {'name': 'Ali', 'age': 20}
print(list(d.keys())) # ['name', 'age']
print(list(d.values())) # ['Ali', 20]
print(list(d.items())) # [('name', 'Ali'), ('age', 20)]

# update()
d.update({'age': 21, 'city': 'Lahore'})
print(d) # {'name': 'Ali', 'age': 21, 'city': 'Lahore'}
