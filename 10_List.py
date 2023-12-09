import random

names = ["Vu", "Truong", "Hieu", "Khoa"]
lucky_one = names[random.randint(0, len(names) - 1)]
print("lucky one is", lucky_one)

# Elements in the List can have different type
if lucky_one == "Vu":
    Vu_properties = ["Nguyen Chiem Minh Vu", 1992, "0934359954"]
    for info in Vu_properties:
        print(info)
    del Vu_properties

names.append("Newbie")
print(names)

names.remove("Khoa")
print(names)

names.append("Khoa")
names.pop(2)
print(names)

names.clear()
if (len(names) == 0):
    print("names collection has been cleared")

del names
# print(names) # Error, names is not defined anymore

nums = [x for x in range(10, 0, -1)]
print("before sorting:", nums)
nums.sort()
print("after sorting:", nums)
nums.sort(reverse = True)
print("reverted sort:", nums)
nums.sort(key = str) # call str() function on each element of List
print("custom sort:", nums)
another_nums = nums
print("copy list:", another_nums)
another_nums.extend(nums)
print("join list:", another_nums)
another_nums.reverse()
print("reversed list:", another_nums)

# In this part, we cover the 2-dimensional lists
matrix = [
    [x for x in range(0, 5)],
    [y for y in range(5, 10)],
    [z for z in range(10, 15)]
]
print("Print a 2D list called matrix")
print(matrix)
print("access the middle element of this matrix:", matrix[1][2])
print("print the matrix in multiple rows")
for row in matrix:
    line = ""
    for n in row:
        line += str(n) + " "
    print(line)

matrix.append(val for val in range(15, 20))
print("add a row in matrix")
for row in matrix:
    line = ""
    for n in row:
        line += str(n) + " "
    print(line)

print("check if element 5 is in the matrix:", 5 in matrix)
print("the above way is not correct, because each element of the matrix is a list object, try to find the value in each row")
for row in matrix:
    if 5 in row:
        print("found value 5 in the matrix")
        break
