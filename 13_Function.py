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


names = ["Vu", "Truong", "Hieu", "Khoa"]
nums = (1, 2, 3, 4, 3, 2, 1)
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
        "name": "Neo"
    },
    {
        "name": "Smith",
        "bank_id": "0041000434556"
    }
]

temp = ""
temp = collection_to_string(names)
print(temp)
temp = collection_to_string(collection = nums) # specify the keyword argument
print(temp)
temp = collection_to_string(member)
print(temp)
temp = collection_to_string(members)
print(temp)