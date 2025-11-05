def fab(n):
    if n<0:
        print("Invalid")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(n):
            print(a)
            a,b=b,a+b
            
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def print_fib_series(n):
    for i in range(n):
        print(fib(i), end=" ")

num = int(input("Enter number of terms: "))

print(fib(num-1))

print_fib_series(num)

    
    
# fab(num)
