#To convert the decimal numbers into roman numbers range upto 50
x=int(input("enter the number:"))
num=[1,4,5,9,10]
roman=["I","IV","V","IX","X"]
i=4
roman_num=""
while x!=0:
    if num[i]<=x:
        roman_num +=roman[i]
        x=x-num[i]
    else:
        i=i-1
print(roman_num)
