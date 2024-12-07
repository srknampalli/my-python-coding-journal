#create dictionary
# employees = [("Alice", 50000), ("Bob", 60000), ("Charlie", 55000)]


# #dictemp = {name:sal for name,sal in enumerate(employees)}
# dictemp = {sal:name for name,sal in employees}
# print(dictemp)

# count the numbers of the words given
# import re
# from collections import Counter
# text = "hello world hello python"
#li = text.split(" ")
# op = len(li)
# print(dict(op))
# # print(li)
# uli = set(li)
# # print(uli)
# # for ele in uli:
# # print(ele, li.count(ele))
#dictf = {ele: li.count(ele) for ele in set(li)}
#dictf = {ele:len(ele) for ele in li}
#print(li)
# dict = {li.count(uli):value for key,value in enumerate(li) }
# print(dict)
#-------------------------------------------------
# 2 TWO
# each character count
# dictf = {ele:text.count(ele) for ele in sorted(text)}
# print(dictf)


#---------------------------------------------------

# 3 Three

# Filter Expensive Products
# You are given a dictionary of products and their prices
# Create a new dictionary containing only products priced above $500.

products = {"laptop": 1200, "phone": 800, "tablet": 400, "monitor": 200}


res_dict =   {key:value for key,value in products.items() if value > 500 }


print(res_dict)