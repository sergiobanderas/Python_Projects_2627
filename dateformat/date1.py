from datetime import datetime

myCurrentDate = datetime.now()

print("Current date and time: ", myCurrentDate)

print("Current year: ", myCurrentDate.year)
print("Current month: ", myCurrentDate.month)
print("Current day: ", myCurrentDate.day) 

print("dd/mm/yyyy format: ", myCurrentDate.strftime("%d/%m/%Y"))
print("hh:mm:ss format: ", myCurrentDate.strftime("%H:%M:%S"))

print("timestamp: ", myCurrentDate.timestamp())

myCurrentTimestamp = myCurrentDate.timestamp()

print("Current date and time from timestamp: ", datetime.fromtimestamp(myCurrentTimestamp))

