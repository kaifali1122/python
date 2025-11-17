num = int(input("Enter number : "))
sign = -1 if num < 0 else 1 # handle negetive sign
num = abs(num) # making +ve
new=0


while num > 0:
    s=num%10
    num=num//10
    new=new*10 +s

print(sign*new)    