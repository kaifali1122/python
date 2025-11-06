num = int(input("Enter Number: "))
temp=num
count=0
sum=0
while num>0:
    s= num%10 
    num=num//10
    count+=1
    sum = sum +s 

print("Sum of ", temp," is ", sum, " & count of ", temp," is ",count)     
    