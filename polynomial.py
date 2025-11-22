############################ program to calculate polynomial function in python we can achieve this using 2 methods;
#Using the NumPy Library
import numpy as np

coef =[]
degree = int(input("enter the degree of the polynomial"))

for i in range (degree+1):
    value = input("f:enter the values ")
    coef.append(value)

    print(np.roots(coef))
#######################
#program to convert from  decimal to binary
#ask the user for input and convert the string input to an integer
dec = int(input("Enter a number to convert to binary:"))
#we use the built-in bin() function
binary_str = bin(dec)

#print the result slicing the string [2:] to remove the leading 'ob'
print(f"Binary number of {dec} is {binary_str[2:]}")

##converting from binary to decimal
# collect input from the user
binary_input= input("Enter a binary number(e.g 1101):")

#convert the binary string to a decimal integer using base = 2

dec_result = int(binary_input,2)

#printing the result

print(f"The decimal value of the binary number {binary_input} is {dec_result}")

### convert from decimal to octal
## collecting binary input from user

binary_input= input("Enter a binary number(e.g 1101):")
#convert the binary string to a decimal integer using base = 2
# inorder to convert from base 2 to octal we need to convert the number to decimal first
dec_result1 = int(binary_input,2)

#now we can convert the integer to Octal (base 8)
 # we use the oct() to convert the decimal to octal(base 8)

 #this oct() function returns a string prefixed with '00', so we slice it [2:]

oct_result = oct(dec_result1)[2:].upper()

#############coverting to hexadecimal base 16

#the hex() function returns a string prefixed with 'ox' so we slice it [2:]

#the  .upper() converts the letters (A-F) TO UPPERCASE FOR STANDARD OUTPUT

hex_result = hex(dec_result)[2:].upper()

# printing our results

print(f"\n converts the results")
print(f"input binary:{binary_input}")
print(f"decimal (base 10): {dec_result}")
print(f"octal (base 8): {oct_result}")
print(f"Hexadecimal (base 16):{hex_result}")


##################### converting from octal to binary

octal_input  = input("enter an octal number (eg 10)")

#convert the octal to decimal(base 10)

oct_to_dec = int(octal_input,8)

################ octal to binary (base2)
#use bin() on the decimal result slicing [2:] to remove

oct_to_bin = bin(oct_to_dec)[2:]


print(f"Result for octal {octal_input}")
print(f"binary base2: {oct_to_bin}")


######converting from hexadecimal base 16

hex_input = input("enter a hexadecim")