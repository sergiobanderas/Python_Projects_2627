name = input("Enter your name:")

try:
    age = int(input("Enter your age:"))

    print ("Hello " + name)
    print ("Your age is:" + age)
    #if age greater or equal than 18 print Access Valid
    if age >= 18:
        print ("Access Valid")
    #if age lower than 18 print Acces Invalid
    else:
        print("Access Invalid")
except ValueError:
    print ("Error: Age must be a number")


