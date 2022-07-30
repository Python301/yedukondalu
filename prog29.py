#WAPP to print reverse order of the string
s=input("enter the string:")
print("given string is",s)
reverse=s[::-1]
print(reverse)
print("*"*50)
reverse=" "
for i in range(len(s)):
    reverse=s[i]+reverse
print(reverse)
