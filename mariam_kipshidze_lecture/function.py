def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

# Example usage
print(greet("Alice"))  # Output: Hello, Alice!


def power(base, exponent=2):
    """Calculates the power of a number with a default exponent of 2."""
    return base ** exponent

# Example usage
print(power(3))       # Output: 9
print(power(3, 3))    # Output: 27


def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120


def add(*args):
    """Returns the sum of all arguments."""
    return sum(args)

def print_kwargs(**kwargs):
    """Prints all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print(add(1, 2, 3, 4))  # Output: 10
print_kwargs(a=1, b=2, c=3)  # Output: a: 1, b: 2, c: 3
