# Dictionary in Python is a type of key:value pair collection

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

methods = [method for method in dir(members[0]) if not method.startswith("__")]
print("All the methods that a Dictionary supports:")
print(methods)

print("List of members before updating:")
for member in members:
    print(member)

for member in members:
    if (not member.get("phone") is None):
        print("member {} has phone number".format(member.get("name")))
    else:
        member["phone"] = "N/A"
    
    if (not member.get("bank_id") is None):
        print("member {} has bank account".format(member.get("name")))
    else:
        member["bank_id"] = "N/A"

print("List of members after updating:")
for member in members:
    print(member)