def fact(n):
    if (n < 0):
       return
    elif(n == 0 or n == 1) :
        return 1
    else:
        return n * fact(n - 1)
       

n= int(input("Enter a non-negative integer: ") )
print("Factorial of", n, "is", fact(n))


