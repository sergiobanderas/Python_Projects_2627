filename = "students.txt"
with open(filename,"a") as file:
    
    while True:
        name = input("Write a name:").strip()
        file.write(name + "\n")

        while True:
            askQuestion = input("Do you want to add a new student y/n:").lower()
            if askQuestion == "n" or askQuestion == "y":
                break
            else:
                print("please write only y or n")

        if askQuestion == "n":
            break
