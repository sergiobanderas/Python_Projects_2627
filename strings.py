fruit = "banana"
print(fruit[0])

for x in fruit:
    print(x,end="-")

print("")
print(fruit[3:6]) #ana
print(fruit[:3]) #ban
print(fruit[3:]) #ana

print(fruit[-4:-2])

fruit = fruit.upper()
print(fruit)
print(fruit.lower())
print(fruit)

hello = "   HellHo World!  "
hello = hello.strip() #delete whitespace beggining or end
print(hello)

print(hello.replace("H","K"))

nombres="oscar,miguel,jose carlos,carmen"
nombresArray = nombres.split(",")

for nombre in nombresArray:
    print(nombre)

print(nombresArray[-1])