count = 1
while count <= 5:
    print(count)
    count += 2
print()

answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no):")
print()

while True:
    answer = input("Do you agree?(yes/no):")
    if answer == "yes":
        break
