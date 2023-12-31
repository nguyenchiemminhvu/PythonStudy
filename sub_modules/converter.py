def collection_to_string(collection):
    print(__name__)
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

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    output = collection_to_string(args)
    print(output)