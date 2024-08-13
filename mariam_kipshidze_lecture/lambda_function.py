# A lambda function that adds 10 to the input
add_ten = lambda x: x + 10

# Example usage
print(add_ten(5))  # Output: 15


# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y

# Example usage
print(multiply(3, 4))  # Output: 12


# List of tuples
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# Sort the list by the second element in each tuple (the string)
pairs.sort(key=lambda pair: pair[1])

# Example usage
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Use filter() to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Example usage
print(even_numbers)  # Output: [2, 4, 6]
