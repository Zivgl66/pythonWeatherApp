def Fibonacci_iterative(n):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1
    if n == 0:
        return 0
    else:
        while count < n:
            count += 1
            num1, num2 = num2, next_number
            next_number = num1 + num2
    return num2
    
    
# recursive:
def Fibonacci_recursive(n):
    # if n < 0:
    #     print("Incorrect input")
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)
    

print(Fibonacci_iterative(3))
print(Fibonacci_recursive(3))