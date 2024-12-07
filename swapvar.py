
#using temp variables
a = 10
b = 5

c = a
a = b  #5
b = c  # 10




# without using temporary vairables

a , b = b, a
print(a,b)

