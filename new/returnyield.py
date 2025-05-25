# 


# return example: compute squares of numbers and return all at once
def get_squares_return(nums):
    result = []
    for n in nums:
        result.append(n * n)
    return result

# yield example: generate squares of numbers one by one
def get_squares_yield(nums):
    for n in nums:
        yield n * n


# Calling both
numbers = [1, 2, 3, 4, 5]

# Using return
print("Using return:")
squares_list = get_squares_return(numbers)
print(squares_list)

# Using yield
print("\nUsing yield:")
for square in get_squares_yield(numbers):
    print(square)
