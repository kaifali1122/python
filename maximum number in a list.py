num= list(map(int, input("enter list ").split()))
# print(max(num))
max=0
for i in range(1, len(num)):
    if num[i]> max:
        max=num[i]
print(max)        