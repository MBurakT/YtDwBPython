text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

search = "Email ".lower().strip()
data = " emAil".lower().strip()

print(search == data)
print()

phone = "+49-176-12345"
print(phone.startswith("+49"))

email = "burak@outlook.com"
print(email.endswith("gmail.com"))

print("@" in email)

url = "https://api.company.com/v1/data"
print("/api" in url)
print()

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
print(phone1[phone1.find("-") + 1:])
print(phone2[phone2.find("-") + 1:])
print()

country = "USA1"
print(country.isalpha())

phone = "3.19"
print(phone.isnumeric())