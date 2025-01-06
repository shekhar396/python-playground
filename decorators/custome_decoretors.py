def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with:")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)  # Call the original function
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

# Usage
print(add(3, 4))
# Output:
# Function 'add' called with:
# Positional arguments: (3, 4)
# Keyword arguments: {}
# Function 'add' returned: 7
# 7
