# positional arguments
def say_hi(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

say_hi("Nika", "Mdinaradze")

# keyword argumenst
def say_hi(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

say_hi(last_name="Mdinaradze", first_name="Nika")

# default arguments
def say_hi(first_name, last_name=None):
    if last_name:
        print(f"Hi {first_name} {last_name}")
    else:
        print(f"Hi {first_name}")
        
say_hi("Nika")

# arbitrary arguments
def say_hi(*names):
    for name in names:
        print(f"Hi {name}")

say_hi("Nika", "Mariami", "Giorgi", "Ana")

# arbitrary keyword arguments
def say_hi(**full_names):
    for first_name, last_name in full_names.items():
        print(f"Hi {first_name} {last_name}")

say_hi(nika="mdinaradze", mariam="dumbadze", giorgi="chumburidze")

# positional only arguments
def say_hi(first_name, last_name, /, greeting="Hi"):
    print(f"{greeting} {first_name} {last_name}")

say_hi("Nika", "Mdinaradze")

# key word only arguments
def say_hi(*, first_name, last_name):
    print(f"Hi {first_name} {last_name}")

say_hi(first_name="Nika", last_name="Mdinaradze")

# tuple unpacking
def say_hi(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

full_name = ("Nika", "Mdinaradze") # can be list, set ...
say_hi(*full_name)

# dictionary unpacking
def say_hi(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

full_name = {"first_name":"Nika", "last_name": "Mdinaradze"}
say_hi(**full_name)

# recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)

# high order function
def alert(func):
    print("function is running...")
    func()

def display():
    print("Test")

alert(display)

