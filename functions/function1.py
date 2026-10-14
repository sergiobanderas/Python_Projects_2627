#print hola in console
def hola():
    print("hola")

def adios(name):
    return "adios" +  name

def ageControl(number):
    if number>=18:
        return True
    else:
        return False

def minMaxCheck(min,max):
    if min < max:
        return True
    else: 
        return False

def writeNumber(text):
    while True:
        try:
            number = int(input(text).strip())
            return number
        except ValueError:
            print("Error! you must write a number")


#ask min and max correct number
#check if min is lower than max
#return a list [min,max]
#if not ask again
def inputMinMax():
    while True:
        min = writeNumber("Write a min number: ")
        max = writeNumber("Write a max number: ")
        if minMaxCheck(min,max):
            return [min,max]
        else:
            print("Error! min must be lower than max")
    
