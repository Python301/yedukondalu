count=0
for i in range(2,10):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        count=count+1
print("prime number count is:",count)
