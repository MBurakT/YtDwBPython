text = "Python"

print(text[0])
print(text[-6])
print()

date = "2026-09-20"
print(date[0:4])
print(date[:4])
print(date[5:7])
print(date[8:])
print(date[-2:])
print()

text = " Engineering".lstrip()
print(text)

text = "Engineering ".rsplit()
print(text)

text = " Engineering ".strip()
print(text)

text = "Data Engineering".strip()
print(text)

text = "###Abc###".strip("#")
print(text)

text = "  Engineering"
print(len(text))
print(len(text.strip()))
print(len(text) - len(text.strip()))