#start
discount = 0
age = int(input("What is your age?: "))
if age >= 13 and age <=15:
    discount = 30
else:
    if age >=16 and age <=17:
        discount = 20
    else:
        if age >= 50:
            discount = 40
print("Your discount is %d%%" %discount)
