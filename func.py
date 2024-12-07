# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=30, city="New York", job= "IT", num="85")

# #print(print_info())


# def greet(name):
#     """Greets the person with their name."""
#     print(f"Hello, {name}!")


# greet("sai")

# def snak(type,quantity):
#     print(f"give the {type} of {quantity} ml.")

# snak("capichano", 30 )

# def greet(name, age):
#     print(f"Hello, {name}! You are {age} years old.")

# greet(name="Alice", age=30)
# greet(age=30, name="Alice")

# default args

# def greet(name="Guest", age=0):
#     print(f"Hello, {name}! You are {age} years old.")

# greet()
# greet("Alice")
# greet("Alice", 30)





# def form(**info):
#     for key, value in info.items():
#         print(f"{key}:{value}")

# form(name="sai", age=30,city="hyd")


def process_data(*args):
    for data in args:
        print(data)

process_data("Data1", "Data2", "Data3")





