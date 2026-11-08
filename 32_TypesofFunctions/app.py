# Action Function
def write_log(message):
    with open(r"app.log", "a") as file:
        file.write(message + "\n")

# write_log("App Started")
# write_log("user logged in")
# write_log("App Stopped")

# Transformation Function
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    username, domain = cl_email.split("@")
    return {"username": username, "domain": domain}


print(clean_and_split_email("sara@gmail.com"))

# Validation Function
def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password("123456"))
print(is_valid_password("12345678"))

# Orchestration Function
# calls the other functions