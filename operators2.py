colors = "red,blue,yellow,green,black,purple,white,brown"
#convert the list of colors in a colors Array
colorsArray = colors.split(",")

#position of the array
index = 1
#loop the Array
for color in colorsArray:
    if index % 2 == 0:
        print (color + ":EVEN")
    else:
        print (color + ":ODD")

    index += 1