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
            

num = int(input("Enter number of terms: "))



    
    
fab(num)
