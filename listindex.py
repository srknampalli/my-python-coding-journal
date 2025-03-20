list1 = [23, 78, 45, 12, 89, 67, 34, 90, 56, 77]


#indexed_list = [(value, index) for index, value in enumerate(list1)]

indexed_list = [(value,index)for index, value in enumerate(list1)]

#print(indexed_list)

sorted_list = sorted(indexed_list, key=lambda x: x[0], reverse=True)

#print(sorted_list)

top_4 =[index for value,index in sorted_list[-4:]]

print(top_4)

for t in top_4:
    print(t)


# enu = enumerate(list1)

# print(enu)

# enu_list = list(enu)
# print(enu_list)


# res = sorted(list1)

# res1 = res[-4:]



