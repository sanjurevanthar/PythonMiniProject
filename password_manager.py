from cryptography.fernet import Fernet

def load_key():
    file= open("key.key", "rb") #rb -> read bytes
    key = file.read()
    file.close()
    return key
#
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#
# write_key()

key = load_key()
fernet = Fernet(key)

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.strip() # line.strip() removes whitespace from both the beginning and the end of the string.
            #this removes "\n", "\t","\r"," "
            user, password = data.split("|")
            #print("User: ", user)
            print("User:", user, "| Password:",
                  fernet.decrypt(password.encode()).decode())

def add():
    name = input("Please Enter the account name: ")
    password = input("Please enter your password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fernet.encrypt(password.encode()).decode() + "\n") #We create a file if not present
        #we open and write the username and password in the file
        #then it closes

while True:
    choice = input("WOULD YOU LIKE TO ADD A NEW PASSWORD OR VIEW THE EXISTING PROJECT?, choose from 'new','view' and 'q'").lower()

    if choice == "new":
        add()

    elif choice == "view":
        view()

    elif choice == "q":
        break
    else:
        print("Please choose a valid option")

