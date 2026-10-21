from datetime import datetime

today = datetime.now()

exam = datetime(2026,10,28)
diffdays = (exam - today).days

if exam > today:    
    print(f"The exam is in {diffdays} days") 
elif exam == today:
    print("The exam is today")
else:
    print(f"The exam was {abs(diffdays)} ago ")