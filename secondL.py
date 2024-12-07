Data = [45,54,69,32,89,19, 45,19 ,111,111]
def sec_max(Data):
    first_max = max(Data[0],Data[1]) # 54
    second_max= min(Data[0],Data[1]) #45
    

    for num in range(2 , len(Data)):
        if Data[num] > first_max:
            second_max = first_max  # sm = 589
            first_max = Data[num] # fm #69 #111
            
             
        

        elif Data[num] > second_max and Data[num] < first_max:# here is you check the num the greater the first max and here it it checking if it greater than secmax
            second_max = Data[num] #111
 
    return second_max
    



res =sec_max(Data)
print(res)



# Data = [45,54,111,69,32,19,111,128,149]
# #def sec_max(Data):
# first_max = max(Data[0],Data[1]) # 54
# second_max= min(Data[0],Data[1])
# third_max = float('-inf')
    

# for num in range(2 , len(Data)):
#     if Data[num] > first_max:
#         third_max = second_max
#         second_max = first_max  # sm = 54 
#         first_max = Data[num] # fm = 69
            
#     elif Data[num] > second_max and Data[num] !=  first_max: # here is you check the num the greater the first max and here it it checking if it greater than secmax
#         third_max =second_max
#         second_max = Data[num]

#     elif Data[num] > third_max and Data[num] != second_max:
#         Data[num] = third_max


# print(third_max)
    




  