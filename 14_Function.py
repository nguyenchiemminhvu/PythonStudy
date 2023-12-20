def collection_to_string(collection):
    output = ""
    if isinstance(collection, list):
        output += "list: "
        for item in collection:
            output += collection_to_string(item) + " "
    elif isinstance(collection, tuple):
        output += "tuple: "
        for item in collection:
            output += collection_to_string(item) + " "
    elif isinstance(collection, dict):
        output += "dict: "
        for key, value in collection.items():
            output += f"{key}:{value} "
    else:
        output += str(collection)
    return output

def int_to_float(n:int):
    return float(n)

def outer_func():
    print("Print from outer_func")
    
    def inner_func():
        print("Print from inner_func")
    
    inner_func()
    print("End of outer_func")

nums = (1, 2, 3, 4, 3, 2, 1)
names = ["Vu", "Truong", "Hieu", "Khoa"]
member = {
    "name": "NCMV",
    "phone": "0934359954",
    "bank_id": "0041000366989"
}
members = [
    {
        "name": "NCMV",
        "phone": "0934359954",
        "bank_id": "0041000366989"
    },
    {
        "name": "Anderson"
    },
    {
        "name": "Smith",
        "bank_id": "0041000434556"
    }
]

outer_func()

temp = ""
temp = collection_to_string(names)
print(temp)
temp = collection_to_string(collection = nums) # specify the keyword argument
print(temp)
temp = collection_to_string(member)
print(temp)
temp = collection_to_string(members)
print(temp)

members.sort(key=lambda item: item["name"])
temp = collection_to_string(members)
print(temp)

# using lambda (anonymous function)
sum_all = lambda args: sum(args)
S = sum_all(nums)
print("Sum of all numbers in nums tuple:", S)

float_numbers = map(int_to_float, nums)
for n in float_numbers:
    print(n, end=' ')