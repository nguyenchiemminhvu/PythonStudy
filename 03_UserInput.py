import getpass

username = input("username: ")
password = getpass.getpass("password: ")
print("username:", username, "\npassword:", password)
print("username: {}\npassword: {}".format(username, password))
print("username: %s\npassword: %s" % (username, password))
print("username: " + username + "\npassword: " + password)