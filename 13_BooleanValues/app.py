print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))
print()

email = ""
phone = "0176-123456"
username = ""

print(any([email, phone, username]))
print(all([email, phone, username]))
print()

print(isinstance(123, int))
print(isinstance(True, str))
print("Hello".endswith("o"))
print("Hello".startswith("o"))