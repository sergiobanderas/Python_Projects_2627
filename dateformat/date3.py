from datetime import datetime

hourNow = datetime.now()
hourExam = datetime(2026,10,21,12,30,00)

diffHours = hourExam - hourNow

totalMinutes = int(diffHours.total_seconds() // 60)
hours = totalMinutes //60
minutes = totalMinutes % 60 

print(f'The exam is in {hours} hour and {minutes} min')


