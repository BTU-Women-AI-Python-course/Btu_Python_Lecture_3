# lambda and high order functions
def alert(func):
    print("function is running...")
    func()

alert(lambda: print("Test"))

# filter
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x%2 == 0, numbers)
print(list(even_numbers))

# map
numbers = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: x**2, numbers))
print(result)
