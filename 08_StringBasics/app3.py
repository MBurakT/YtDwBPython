price = "1234,56"
print(price.replace(",", "."))

phone = "176-1234-56"
print(phone.replace("-", "/"))

price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))
print()

first_name = "Micheal"
last_name = "Scott"

last_name = first_name + " " + last_name
print(last_name)

folder = "C:/Users/Burak"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)