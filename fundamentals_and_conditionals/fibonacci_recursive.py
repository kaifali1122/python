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



