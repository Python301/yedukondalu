string=input("enter the string:")
reverse=" "
for i in range(len(string)):
    reverse=string[i]+reverse
print(reverse)
if(string==reverse):
    print("Given string is palindrom")
else:
    print("given string is not a palindrom")
