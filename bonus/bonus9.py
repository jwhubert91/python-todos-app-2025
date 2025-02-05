password = input("Enter a new password: ")

# dict type
password_validity = {
    "over7chars": False,
    "doesContainDigit": False,
}

if len(password) >= 8:
    password_validity["over7chars"] = True
else:
    password_validity["over7chars"] = False

for i in password:
    if i.isdigit():
        password_validity["doesContainDigit"] = True

print(password_validity)

if all(password_validity.values()):
    print("Strong password")
else:
    print("Weak password")