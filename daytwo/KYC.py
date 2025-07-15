from re import match

patterns = {
    "name":r"^[A-Za-z ]{3,}$",
    "password":r"^(?=.*[@#$!])[A-Za-z0-9?=.@#$!*]{8,}$",
    "aadhaar":r"^[0-9]{12}$",
    "pan":r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",
    "email":r"^[a-z0-9-_]{2,}@[a-z]{3,}\.[a-z]{2,}$"
}

def validateKYC(userData):
    flag = True
    for field, value in userData.items():
        if not match(patterns[field],value):
            print("Invalid ",field)
            flag=False
    if flag==True: return "Account created"
    else: return "Invalid User data"

print(validateKYC({
    "name":"Razak Mohamed S",
    "password":"Razak@123",
    "aadhaar":"987654567834",
    "pan":"ABCDE0882W",
    "email":"dlithe@gmail.com"
}))
print(validateKYC({
    "name":"Ra",
    "password":"Razak123",
    "aadhaar":"987567834",
    "pan":"ABCDE08",
    "email":"dlithe@gmil.m"
}))