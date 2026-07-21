# num1 = 11
# num2 = num1

# print("Before num2 value is updated:")
# print("num1:", num1)
# print("num2:", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

# num2 = 22

# print("\nAfter num2 value is updated:")
# print("num1:", num1)
# print("num2:", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

# integers consistently point to the same place in memory. also dictionaries


dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter the value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# after value for dict2 has been updated, both dict1 and dict2 values have both been updated
# dictonaries can change