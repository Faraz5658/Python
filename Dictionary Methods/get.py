# keys(), values(), items()
d = {'name': 'Ali', 'age': 20}
print(list(d.keys())) # ['name', 'age']
print(list(d.values())) # ['Ali', 20]
print(list(d.items())) # [('name', 'Ali'), ('age', 20)]
# get(key, default)
print(d.get('age')) # 20
print(d.get('city', 'N/A')) # N/A
