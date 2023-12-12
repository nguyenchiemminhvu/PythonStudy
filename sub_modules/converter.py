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