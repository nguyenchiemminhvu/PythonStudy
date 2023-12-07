import getpass

username = input("username: ")
password = getpass.getpass("password: ")
confirm = getpass.getpass("confirm password: ")

valid_input = False
if (len(username) > 0):    
    if (password == confirm):
        print("Create account successfully")
        valid_input = True
    else:
        print("Mismatch in your password")
else:
    print("username must not empty")

valid_profile = False
if (valid_input):
    print("Enter information for your profile")
    birthday = input("date of birth (yyyy/MM/dd): ")
    birth_year = int(birthday[0:4])
    birth_month = int(birthday[5:7])
    birth_day = int(birthday[8:])
    if (birth_year < 1900):
        print("invalid year")
    elif (birth_month <= 0 or birth_month > 12):
        print("invalid month")
    elif (birth_day <= 0 or birth_day > 31):
        print("invalid day")
    else:
        print("{}/{}/{}".format(birth_year, birth_month, birth_day))
        valid_profile = True

if (valid_profile):
    print("everything is done")