num = int(input("Enter Number: "))
temp=num
count=0
while num>0:
    num=num//10
    count+=1


print(" count of ", temp," is ",count)     
    