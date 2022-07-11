#calculate charge of library
days=int(input("enter how many days to carry a book:"))
if(days<=5):
    charge=days*2
    print("the charge of the book is",charge)
elif(days<=10):
    charge=days*3
    print("the charge of the book is",charge)
elif(days<=15):
    charge=days*4
    print("the charge of the book is",charge)
else:
    charge=days*5
    print("the charge of the book is",charge)
print("Thanks for using this program")
