items = (1, 2, 3, 4, 5)
for item in items:
    print(f"Round {item}")
print()

items = "Python"
for item in items:
    print(item)
print()

for item in range(5):
    print(f"Round {item + 1}")
print()

for item in range(1, 6):
    print(f"Round {item}")
print()

for item in range(2, 10, 2):
    print(f"Round {item}")
print()

scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total:", total)
print()

for i in range(1,7):
    print("*" * i)
print()

names = ['john', 'maria', '', 'ali']
for name in names:
    if not name:
        break
    print(f'Name = {name}')
print()

names = ['john', 'maria', '', 'ali']
for name in names:
    if not name:
        continue
    print(f'Name = {name}')
print()

for i in range(10):
    pass # do something later

for item in range(3):
    if isinstance(item, str):
        break
else:
    print("All items are number")
print()

for x in range(3):
    for y in range(3):
        print(f"X: {x} Y: {y}")
print()

tables = ['customer', 'orders', 'products', 'prices']
columns = ['id', 'create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')
