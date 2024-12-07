# def second_largest(numbers):
#     # Remove duplicates by converting the list to a set, then back to a list
#     unique_numbers = list(set(numbers))
    
#     # Check if there are at least two unique numbers
#     if len(unique_numbers) < 2:
#         return None
    
#     # Sort the unique numbers in descending order
#     unique_numbers.sort(reverse=True)
    
#     # The second largest number will be at index 1
#     return unique_numbers[1]

# Example usage
# numbers = [20,30,2,85,45,98,47]
# second_largest_number = second_largest(numbers)
# if second_largest_number is not None:
#     print("The second largest number is:", second_largest_number)
# else:
#     print("There are not enough unique numbers in the list.")

#Largest Number

from functools import reduce

scores = [88, 92, 75, 63, 98, 85,100]

# largest_num = reduce(lambda a,b : a if a > b else b,scores)

# print(largest_num)

# second_largest = sorted(set(scores), reverse=True)[2]

# 

second_largest = sorted(set(scores) )[1]

print(second_largest)