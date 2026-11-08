def clean_name(name):
    if name:
        cleaned = name.strip()
        if len(cleaned) > 0:
            cleaned = cleaned[0].upper() + cleaned[1:].lower()
            return cleaned
        else:
            return "Unknown"
    else:
        return "Unknown"


def clean_names(first_name, last_name=""):
    cleaned_first_name = clean_name(first_name)
    cleaned_last_name = clean_name(last_name)
    cleanead = cleaned_first_name + " " + cleaned_last_name
    print(cleanead)


clean_names(first_name=" MariA  ", last_name="SMITH ")
clean_names("AHMET ", last_name="")
clean_names("  ", "SMITH  ")
clean_names(None, None)
print()


def total(*args):  # when you pass similar values
    print(sum(args))


total(1, 2)
total(1, 2, 3)
total(1, 2, 3, 4, 5, 6)


def create_user(**kwargs):  # when you pass different values
    print(kwargs)


create_user(first_name="Mo", last_name="Salah", age=33, country="Egypt")
create_user(name="Ronaldo", country="Portugal")


def clean_n(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned


lo_name, up_name = clean_n(" MariA ")
print(lo_name)
print(up_name)
