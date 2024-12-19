# Login System
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("The Login was successful!")
else:
    print("Login failed due to an invalid username or password.")