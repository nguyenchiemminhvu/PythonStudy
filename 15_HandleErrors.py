def example_function(x, y):
    try:
        result = x / y  # Potential ZeroDivisionError
        z = some_undefined_variable  # Potential NameError
        int("abc")  # Potential ValueError
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    except NameError as e:
        print("NameError:", e)
    except ValueError as e:
        print("ValueError:", e)
    except TypeError as e:
        print("TypeError:", e)
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")

example_function(10, 0)  # Trigger ZeroDivisionError
example_function(10, 10) # Trigger NameError
