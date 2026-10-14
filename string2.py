name = "John"
surname = "Smith"
fullname = surname + ", " + name

txt = f"The Alan Turing student is {surname} , {name}"

print(fullname)
print(name,surname)
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

name2 = " pepito "
#capitalize()
name2 = name2.strip().capitalize()

#Pepito
print(name2)

txtToSearch = "CPIFP"
txt = "this school name is CPIFP Alan Turing"
position = txt.find("CPIFP")
if position!=-1:
    schoolname1 =txt [position:] 
    print(schoolname1) #CPIFP AlanTuring
    schoolname = txt[position:position+len(txtToSearch)]
    print(schoolname) #CPIFP