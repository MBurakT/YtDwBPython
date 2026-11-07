person = ['Maria', 29, 'Data Engineer', 'Spain']
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]
name, age, role, country = person

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *details, country = person

print(name)
print(details)
print(country)
print()

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *details = person
print(name)
print(details)
print()

person = ['Maria', 29, 'Data Engineer', 'Spain']
*details, country = person
print(details)
print(country)
print()

numbers = [1]
first, *rest = numbers
print(first)
print(rest)
print()

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, _, role, _ = person
print(name)
print(role)
print()

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *_, country = person
print(name)
print(country)
print()

numbers = [1, 5, 5, 4, 3]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

print("All:", all(numbers))
print("All:", all([1, 0, 2]))
print("All:", all(['a', '', 'b']))

print("Any:", any(numbers))
print("Any:", any([1, 0, 2]))
print("Any:", any(['a', '', 'b']))
print("Any:", any([0, 0, 0]))

print("Count:", numbers.count(5))

print("Index:", numbers.index(5))

print(4 in numbers)
print(8 in numbers)
print(8 not in numbers)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)
print(list1 == [1, 2, 3, 4])
print(list1 < list2) # checks first item
print(list1 > list2)
print(list1 is list2)
