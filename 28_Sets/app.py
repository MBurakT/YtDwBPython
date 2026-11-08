my_set = {10, 30, 20, 10}
print(my_set)
# print(my_set[1])
my_set.remove(20)
print(my_set)
print()

a = {10,20, 30, 40}
a.add(50)
print(a)

# a.update({1, 2})
a |= {1, 2}
print(a)

# a.remove(100)
a.discard(100)
# a.pop()
print(a)
print()

a = {10,20, 30, 40}
b = {30, 40, 50, 60}
# print(a.union(b))
print(a | b)

# print(a.intersection(b))
print(a & b)

# print(a.difference(b))
print(a - b)
print(b - a)

print(a.symmetric_difference(b))
print()

a = {30, 40}
b = {30, 40, 50, 60}
print(a.issubset(b))
print(b.issuperset(a))

print(a.isdisjoint(b))