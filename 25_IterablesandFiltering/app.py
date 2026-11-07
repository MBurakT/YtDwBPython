letters = ['a', 'b', 'c']
new_list = []
for letter in letters:
    new_list.append(letter.upper())
    print(new_list)
print()

letters = ['a', '', 'c']
# print(list(enumerate(letters, start=1)))
for index, value in enumerate(letters):
    print(index, value)
print()

letters = ['a', 'b', 'c']
# print(reversed(letters))
for letter in reversed(letters):
    print(letter)
print()

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
# print(list(zip(letters, numbers)))
for letter, index in zip(letters, numbers):
    print(letter, index)
print()

letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))

number = ['1', '2', '3']
print(list(map(int, numbers)))
print()

letters = ['a', '', 'b', None, 'c', False]
print(list(filter(bool, letters)))
print()

items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))

for i in filter(str.isalpha, items):
    print(i)