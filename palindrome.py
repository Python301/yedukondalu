#Given string is palindrom or not
name=input("enter the string:")
string=name[::-1]
if(name==string):
    print("Given name is palindrom:",name)
else:
    print("Given name is not a palindrom:",name)
