import datetime
time=int(input("enter the time in seconds"))
actual_time=datetime.timedelta(seconds=time)
print("the time is",actual_time)