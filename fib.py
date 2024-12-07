num1 = 0 
num2 = 1
sum = 0 # 
num = int(input("enter number"))
print(sum,end = " ")
for i in range(0,num):
    
    num1 = num2 # 1
    num2 = sum # 0
    sum = num1+num2 # 
    print(sum, end = " ") 

    #print(sum,end= " ") #  

## fib series with recursion

# first two terms 0 ,1 , and remaning obtained by precedding two terms and nth terms sum of (n-1)th term and (n-2)th term    1 - 1st  , 2 - 2nd ,3  ,5 , 8
#fibonacci(0)=0,fibonacci(1)=1,fibonacci(2)=1,fibonacci(3)=2,fibonacci(4)=3,fibonacci(5)=5
#fibonacci(5), the result is indeed 5, but if you are printing the series up to the 5th term, you will see 6 numbers. This is because the series starts from  fibonacci(0) not fibonacci(1)
# def fib(i):
#     if(i <= 1):
#         return i
#     else:
#         return fib(i-1) + fib(i-2)
    
# num = int(input("enter num"))
# for i in range(0,num+1):
#     print(fib(i))

    













