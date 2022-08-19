#how many day in a month and month contains 3 latters
month=input("enter month name:")
if(month=="jan" or "mar" or "may" or "jul" or "agu" or "oct" or "dec"):
    print("this month contains 31 days",month)
elif(month=="apl" or "jun" or "sep" or "nov"):
    print("this month contains 30 days",month)
elif(month=="feb"):
    print("28 days")
else:
    print("invalid")
