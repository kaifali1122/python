num = int(input("Enter Number: "))
temp=num

l= len(str(temp))

tem = 0
while num>0 :
    s= num%10
    num=num//10
    tem = tem+s**l

print (temp , tem)    
if temp==tem:
    print(temp, " is Armstrong")    
else:
    print(temp, " is not a armstron")    