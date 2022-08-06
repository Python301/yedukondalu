#the gien string contains upper and lowercase latters but print only upper case characters
string=input("enter string contains upper and lower case latters:")
upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in string:
    if(i in upper):
        print(i,end=" ")


