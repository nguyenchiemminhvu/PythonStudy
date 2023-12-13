sample_str = "This is a sample string"
for character in sample_str:
    print(character)

for idx in range(10):
    print(idx)

for idx in range(1, 10):
    print(idx)

for idx in range(1, 10, 3):
    print(idx)

sample_collection = ["Vu", "Truong", "Hieu", "Khoa"]
for member in zip([0, 1, 2, 3], sample_collection):
    print(member)

for idx in range(len(sample_collection)):
    print(sample_collection[idx])

for i in range(1, 5):
    print("*" * i)

for i in range(1, 5):
    temp = ""
    for j in range(0, i):
        temp += "*"
    print(temp)

for x in range(0, 4):
    for y in range(0, 3):
        print(f"({x}, {y})")

list_numbers = [1, 4, 2, 6, 4, 0, 9, 3]
max_number = list_numbers[0]
max_index = -1
for i, n in enumerate(list_numbers):
    if (max_number < n):
        max_index = i
        max_number = n
print("max number in list_numbers is {} at index {}".format(str(max_number), max_index))

reversed_list = reversed(list_numbers)
output = ""
for item in reversed_list:
    output += str(item) + " "
print("reversed list:", output)