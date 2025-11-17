arr=list(map(int, input("Enter list here : ").split()))
print("using sum method : ", sum(arr))

n=len(arr)
sum=0

for i in range(n):
    sum = sum+arr[ i ]

print("using without method", sum)