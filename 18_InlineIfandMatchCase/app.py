score = 85

print("A" if score >= 90 else "B" if score >= 80 else "F")
print()

country = "Germany"

match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown Country")
