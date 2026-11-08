my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 40
}
print(my_dict)
print(my_dict['b'])
my_dict['c'] = 80
print(my_dict)
print()

user = {"id": 1, "age": 30, "city": "berlin"}
print(user["city"])  # key do not exist throw exception
print(user.get("name", "Unknown"))  # return value or None

print("age" in user)
print("name" in user)

print(user.keys())
print(user.values())
print(user.items())
print(user)

for u in user:
    print(u, user[u])

for key, value in user.items():
    print(key, value)

user["name"] = "John"
print(user)
user["age"] = 35
print(user)

age = user.pop("salary", "Not Found")
age = user.pop("age")
print(user)
print("Removed Item:", age)

user.popitem()
print(user)
print()

user = {
    "id": None,
    "name": None,
    "age": None,
    "city": None
}
user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)
user["age"] = 40
print(user)
print()

user = {"id": 1, "name": "John", "age": 30, "city": "berlin"}

user_str = {
    k.upper(): v.lower()
    for k, v in user.items()
    if isinstance(v, str)
}
print(user_str)