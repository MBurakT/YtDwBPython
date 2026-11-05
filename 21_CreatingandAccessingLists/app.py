# Create List
empty = []
print(empty)
print(type(empty))

letters = ['a', 'b', 'c']
print(letters)
print(type(letters))

numbers = [1, 2, 3]
print(numbers)
print(type(numbers))

mixed = [1, 'a', True, None]
print(mixed)
print(type(mixed))
print()

empty = list()
print(empty)

letters = list('Python')
print(letters)

numbers = list(range(5))
print(numbers)
print()

matrix = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f']
]
print(matrix)
print(type(matrix))
print()

mixed_matrix = [
    ['a', 'b'], 
    [1, 2, 3], 
    [True]
]
print(mixed_matrix)
print(type(mixed_matrix))
print()
print()

# Access & Read
lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])
print(lst[-1])
print(lst[-2])
print()

matrix = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f'], 
    ['g', 'h', 'i']
]

print(matrix)
print(matrix[2])
print(matrix[-1][-1])
print(matrix[0][0])
print(matrix[1][1])
print()

lst = ['a', 'b', 'c', 'd']
print(lst[1:3])
print(lst[:3])
print(lst[-2:])
print(lst[:])
print()

matrix = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f'], 
    ['g', 'h', 'i']
]
print(matrix[:2])
print(matrix[1:])
print(matrix[2][:2])
