#to converts seconds into [hr:min:sec]
sec=int(input("enter tatal no of seconds:"))
hours=sec//3600
remaining_sec=sec%3600
minutes=remaining_sec//60
seconds=remaining_sec%60
print(hours,minutes,seconds,sep=":")
