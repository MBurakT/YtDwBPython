import copy

letters = ['c', 'a', 'b']
letters.sort()
letters.sort(reverse = True) # Desc
print(letters)
print()

matrix = [
    ['d', 'e', 'f'], 
    ['g', 'h', 'i'], 
    ['a', 'b', 'c']
]
matrix.sort()
matrix[1].sort()
print(matrix)
print()

letters = ['c', 'a', 'b']
new_list = sorted(letters, reverse = True)
print(letters)
print(new_list)
print()

letters = ['c', 'a', 'b']
# letters.reverse()
new_list = list(reversed(letters))
print(letters)
print(new_list)
print()

letters = ['a', 'b', 'c']
letters_copy = letters
letters_copy.pop()
letters_copy.append('z')
print(letters)
print(letters_copy)
print()

letters = ['a', 'b', 'c']
letters_copy = letters_copy.copy()
letters_copy.pop()
letters_copy.append('z')
print(letters)
print(letters_copy)
print()

original = [
    ['a', 'b'], 
    ['c', 'd']
]

#Assignment
copy1 = original
print("Same Object?", original is copy1, "\n")

#Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Same Object?", original is copy2, "\n")

#Deep Copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Same Object?", original is copy3, "\n")
print()

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers
print(comb)
print(letters * 2)
print()

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = [letters, numbers]
print(comb)
print()

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)
print()

letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers, "Hi"))
print(comb)
print()

ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
print(list(zip(ids, names)))