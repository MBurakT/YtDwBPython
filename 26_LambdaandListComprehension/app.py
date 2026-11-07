multiple = lambda x: x * 2
print(multiple(2))
print()

add = lambda x, y: x + y
print(add(1, 2))
print()

check = lambda i: i in "python"
print(check('n'))
print(check('z'))
print()

prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))
print()

prices = [120, 30, 300, 80]
print(list(filter(lambda x: x >= 100, prices)))
print()

students = [
    ['Maria', 85],
    ['Ali', 90], 
    ['Veli', 60]
]
print(list(filter(lambda row: row[1] > 70, students)))
print(list(filter(lambda row: row[0].startswith('M'), students)))
print()

# Comprehension
domains = [
    'www.google.com', 
    'www.openai.com', 
    'localhost', 
    'WWW.DATAWITHBARAA.COM'
]

cleaned = [
    d.lower().replace('www.', '') # d
    for d in domains
    if '.' in d
]
print(cleaned)
