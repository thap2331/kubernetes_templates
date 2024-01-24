list_of_dicts = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]
tbh = {}
for i in list_of_dicts:
    if i['age'] == 30:
        tbh = i
        break
print(tbh)