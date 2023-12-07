full_name = "Nguyen Chiem Minh Vu"
last_name = full_name[0:6]
middle_name = full_name[7:-3]
first_name = full_name[-2:]

print(full_name)
print(last_name, middle_name, first_name)
print(full_name[0:])

introduction = first_name + " [{}] ".format(last_name) + "is a C++ programmer."
introduction = introduction + """
He started to learn C++ programming language in 2013.
Until now, when he already has a little bit experience with C++ programming language, he want to learn Python programming language.
And here he is.
"""
introduction = introduction + f"His full name is {full_name}, but you can call him {first_name} for short.\n"

favorite_quote = "Favorite quote: 'The most important thing is to keep the most important thing the most important thing'"

message = introduction + favorite_quote

print(message)
print("He just represent an introduction about himself in a message with " + str(len(message)) + " characters")
print("Now, he gonna do something cool with his name storing in the full_name variable.\n")
print("He capitalized the characters and here is the result: " + full_name.capitalize())
print("He makes all the characters in his name become upper: " + full_name.upper())
print("And he reorder the characters in an opposite way: " + full_name[::-1])
print("These methods does not change anything in the original string, it just modifies the apprarent of a copy instance and returns the copy instance.")
print("As you can see, the original variable holding his full name stays the same: " + full_name)
print("Another important method of string class is find, it returns the index of the first occurance of the sub-text in the target string.")
print("Let's find a pattern from his full name: " + full_name[full_name.find("Nguyen"):])
print("If the sub-text does not appear in the target string, -1 is returned: " + str(full_name.find("Anything")))
print("Another way to find out if a substring exists in a particular string, but don't need a string in return, try this: " + str("Vu" in full_name))
print("He found another way to extract the last name: " + full_name.removesuffix(" Chiem Minh Vu"))
print("In the same way, to obtain his first name: " + full_name.removeprefix("Nguyen Chiem Minh "))
print("He wants to conclude this topic by doing replacement in his full name: " + full_name.replace(" Chiem", ""))