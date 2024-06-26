import re 
password = input("Enter your password :")
if len(password) < 8:
    print("Password must contain be at least 8 characters long.")
elif not re.search("[A-Z]",password):
    print("password must contain at least one uppercase letter.")
elif not re.search("[a-z]",password):
    print("password must contain at least one lowercase letter.")
elif not re.search("[!,@,#,$,%,&]" ,password):
    print("password must contain special characters.")
elif not re.search("[0-9]"):
    print("password must contain at least one number")
else:
    print("Password is strong")    