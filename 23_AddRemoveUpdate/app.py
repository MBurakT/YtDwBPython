letters = ['a', 'b', 'c']
letters.append('x')
letters.append('y')
letters.insert(0, 't')
letters.insert(2, 'y')
print(letters)
print()

matrix = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f'], 
    ['g', 'h', 'i']
]
matrix[1].append('x')
matrix[0].insert(0, 'z')
print(matrix)
print()

letters = ['a', 'b', 'c']
# letters.clear()
# letters.remove('a')
removed = letters.pop(0) # pop() => removes last item

print(letters)
print("Removed Item:", removed)
print()

matrix = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f'], 
    ['g', 'h', 'i']
]
# matrix.remove(['a', 'b', 'c'])
# matrix.pop()
matrix[1].remove('e')
matrix[-1].pop(0)
matrix[0].pop()
print(matrix)
print()

letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y'
print(letters)
print()

matrix = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f'], 
    ['g', 'h', 'i']
]
matrix[-1] = ['x', 'y', 'z']
matrix[0][0] = '-'
matrix[1][1] = '-'
matrix[-1][-1] = '-'
print(matrix)
