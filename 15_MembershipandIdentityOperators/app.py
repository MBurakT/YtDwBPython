print("f" in "python")
print(3 in [1, 2, 3])
print()

domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)
print()

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)
print(x is y)

x = 10
y = 10

print(x == y)
print(x is y)
print()

email = None
print(email is not None and email != "")
