if __name__ == "__main__":
    scripts = "print('This code has been executed by exec() function')"
    exec(scripts)
    
    with open("./09_For_Loop.py", "r") as F:
        exec(F.read())