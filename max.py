def find_max(*nums):
    max = 0 

    for num in nums:
       if max < num: 
           max = num
    return max

