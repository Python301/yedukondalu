count=0
for year in range(1999,2022):
    if(year%4==0 and year%100!=0 or year%400==0):
        print(year)
        count=count+1
print(count)
    

