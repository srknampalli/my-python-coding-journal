n = int(input("check n is prime or not"))
def prime():
    if n < 2:
        return "number is not prime"
    
    for i in range(2 , int(n**0.5)+1):
        if n % i == 0:
            return "Number is not prime"
    return "num is prime"
            
 
    
res = prime()

print(res)

