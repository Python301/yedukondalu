#calculate total restarent bill (tip+tax)
amount=int(input("enter the amount :"))
#tip is 18%
tip=amount*0.18
#tax is 16%
tax=amount*0.16
total_bill=amount+tip+tax
print("tip is {},tax is {},Totalbill is {}".format(tip,tax,total_bill))
