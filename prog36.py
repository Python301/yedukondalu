# Program to calculate the factors of the number
num = int(input("enter number:"))
if num > 0:
    for i in range(2, num):
        if (num % i) == 0:
            print(i,",",num//i,"is the factors of",num)
    else:
        pass
else:
    print(num, "invalid input")
