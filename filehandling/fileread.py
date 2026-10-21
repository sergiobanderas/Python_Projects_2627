filename = "students.csv"

#return if student exist in the students file
def studentExist(studentName, studentSurname):
    return True

with open(filename,"r") as file:
    for line in file:
        student = line.strip().split(",")
        print(student[1])

name = input("write name:")
surname = input("write surname:")

if studentExist(name, surname):
    print("Student exist")
else: 
    print("Student doesnt exist")




