name = input("Name: ")
year = input("Year of birth: ")
age = 2023 - int(year)
print(name + " is " + str(age) + " olds")

print(type(name), type(year), type(age), type(""), type(type(name) == type(year)))

final_result = name + " is " + str(age) + " olds\n"
final_result = final_result * 3
print(final_result)
print(type(final_result))