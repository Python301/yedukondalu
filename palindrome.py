#Palindrome program

str1 = input("Enter string: ")
rstr1 = ""
for i in range(len(str1)):
    rstr1=str1[i]+rstr1
print("Reverse of string: ", rstr1)
if str1==rstr1:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
