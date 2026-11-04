print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)
print(3 > 1 or 5 < 1)
print(3 > 1 or 5 > 1)
print()

cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)
print()

email = True
password = False
print(email and password)
print()

print(not 3 > 2)
print(not True)
print(not False)
print(not not False)

name = ""

print(not name)
print(not 0)
print()

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)