#enter the string and also create the new string contains without vowels
str=input("enter the string:")
string=str.lower()
vowels=["a","e","i","o","u"]
for i in string:
    if(i in vowels):
        continue
    else:
        print(i,end="")
