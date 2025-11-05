st= input("Enter: ")
count= 0
for char in st.lower():
    if char in "aeiou":
        count +=1
print(count , " Vowels in ", st)         