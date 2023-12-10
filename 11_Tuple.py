# Tuple is immutable, can not modify the elements of a tuple
nums = (1, 2, 3, 4, 3, 2, 1)
print("nums is a tuple object, here is the list of member variables and methods that tuple supports:")
members = [method for method in dir(nums) if not method.startswith("__")]
for member in members:
    print(member)

# Iterating the tuple
temp = ""
for n in nums:
    temp += f"{n} "
print(temp)

count = nums.count(1)
print("frequency of value 1 in tuple nums:", count)

# unpacking the tuple
a, b, c = nums[0:3]
print(a, b, c)