# def increasing_triplet(nums):
#     # Initialize first and second to positive infinity
#     first = float('inf')
#     second = float('inf')
    
#     # Traverse the array
#     for num in nums:
#         # Check if current number is greater than second
#         if num > second:
#             return True
#         # Update second if current number is between first and second
#         elif num > first:
#             second = num
#         # Update first if current number is less than first
#         else:
#             first = num
    
#     return False

# # Test the function with the given example
# nums = [5, 2, 12, 15]
# print(increasing_triplet(nums))  # Output: True

# Example: Finding the maximum value in a list

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,12]

# Initialize max_value to negative infinity
max_value = float('-inf')

# Traverse the list and update max_value
for number in numbers:
    if number > max_value:
        max_value = number

print("The maximum value is:", max_value)  # Output: The maximum value is: 9

