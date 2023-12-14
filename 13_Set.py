items = {1, 2, 3, 3, 4, 5, 4, 6}
print("non-duplicated values in items:", items)

nums = [1, 2, 3, 3, 4, 5, 4, 6]
print("non-duplicated values in nums:", set(nums))

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
print("A:", A)
print("B:", B)
print("in A but not in B:", A - B)
print("in A or in B:", A | B)
print("in A and in B:", A & B)
print("in A or B but not both:", A ^ B)