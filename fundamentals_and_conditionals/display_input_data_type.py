value = input("Enter: ")

# check for integer
if value.lstrip('-').isdigit():
    value = int(value)

# check for float
elif value.replace('.', '', 1).lstrip('-').isdigit():
    value = float(value)

print("Value:", value)
print("Type:", type(value))