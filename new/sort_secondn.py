names = ["sai ram" , "rohit shrama" , "virat kohli"]

# to swap first name as second name vice versa

res = []

for name in names:
    first , second = name.split()

    swapped_name = second,first

    print(sorted(swapped_name))




# Split concept Importance and how it is useful

# for name in names:
#     one,two = name.split()
#     print(one,two)
# name.split() splits the string at whitespace (spaces) by default
# one, two = name.split() unpacks the split result into two variables  
# in the second case we not unpacking
#   
# for name in names:
#     res = name.split()
#     print(res)




# res= sorted(names, reverse=True)

# print(res)

# res = []

# for name in names:
#     s_name=sorted(name.split(" "))
#     res.append(s_name)

# print(sorted(res))

