num = int(input("Enter Number: "))
temp=num
tem = 0
while num>0 :
    s= num%10
    num=num//10
    tem = tem*10+s
    
print (tem)
if tem==temp:
    print(temp, " is palindromg")    
else:
    print(temp, " is not a palindrom")    


# using direct method 
    
# if (temp==int(str(temp)[::-1])):
#     print(temp, " is palindromg")    
# else:
#     print(temp, " is not a palindrom")    