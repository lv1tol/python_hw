import pickle
# === Dictionary homework ===
names = {
    0 : "admin",
    1 : "user1",
    2 : "user2",
    3 : "user3"
}

passwords = {
    0 : "123456",
    1 : "654321",
    2 : "121212",
    3 : "323232"
}

def addUser(user, password):
    for i in names:
        if user in names[i]:
            print("Name already taken")
            return
    if len(password) < 6:
        print("Password too short")
        return
    for n in password:
        if n == '0' or n == '1' or n == '2' or n == '3' or n == '4' or n == '5' or n == '6' or n == '7' or n == '8' or n == '9':
            names[len(names)] = user
            passwords[len(passwords)] = password
            print(f"User {user} added")
            return
    print("Password invalid")     
    return

def delUser(user):
    for i in names:
        if user in names[i]:
            names.pop(i)
            print(f"User {user} deleted")
            return
    print(f"User {user} not found")

def chngPassword(user, password):
    for i in names:
        if user in names[i]:
            if password not in password[i]:
                passwords[i] = password
                print("Password changed")
                return
            else:
                print("Enter diffrent password")
                return    
    print(f"User {user} not found")
    return

def getPassword(user):
    for i in names:
        if user in names[i]:
            print(f"{names[i]}`s password: {passwords[i]}")
            return
    print(f"User {user} not found")

def save():
    with open('data_names.txt', 'wb') as n:
        pickle.dump(names, n)
    with open('data_passwords.txt', 'wb') as p:
        pickle.dump(names, p)
    print('Users saved successfully to file')

def show():
    for i in names:
        print(f"{names[i]} - {passwords[i]}")

show()
addUser("user4", "bbbbb7")
show()
delUser("user4")
show()
chngPassword("user2", "vv1jon3")
show()
getPassword("admin")
save()