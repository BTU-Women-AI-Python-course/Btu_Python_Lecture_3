# Python Introduction

## Topics Covered

1. **Defining and Calling Functions** - https://www.w3schools.com/python/python_functions.asp
   - Learn how to define and call functions in Python.
   - Understand the syntax and use cases for functions.

2. **Parameters and Return Values** - https://www.w3schools.com/python/python_functions.asp
   - Explore how to pass parameters to functions and how to return values.
   - Understand the importance of parameters in making functions flexible and reusable.

3. **Lambda Functions** - https://www.w3schools.com/python/python_lambda.asp
   - Discover the power of lambda functions for creating anonymous functions in Python.
   - Learn how to use lambda functions in various contexts for concise and readable code.

  
# 📚 Higher-Order Functions with Lambda

## Objective
Implement higher-order functions using lambda functions.

## Requirements

1. **Define the Function**

   Create the `apply_operation` function with the following signature:

   ```python
   def apply_operation(numbers, operation):
       """
       Apply the given operation to each element in the list of numbers.
       
       :param numbers: List of numbers to be processed.
       :param operation: A function that defines the operation to apply to each element.
       :return: A new list with the operation applied to each element.
       """
       return [operation(number) for number in numbers]


## Example input and output

input: [1, 2, 3, 4, 5]
Doubled: [2, 4, 6, 8, 10]
Squared: [1, 4, 9, 16, 25]
Filtered (odd numbers): [1, 3, 5]
