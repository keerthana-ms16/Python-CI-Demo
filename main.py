
def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Simple Python Calculator")
    print("Addition:", add_numbers(10, 5))
    print("Subtraction:", subtract_numbers(10, 5))
    print("Multiplication:", multiply_numbers(10, 5))
    print("Division:", divide_numbers(10, 5))
