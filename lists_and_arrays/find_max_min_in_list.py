num= list(map(int, input("enter list ").split()))
# without max function
max=0
for i in range(1, len(num)):
    if num[i]> max:
        max=num[i]
print(max)       
 
# with max function
# print(max(num))