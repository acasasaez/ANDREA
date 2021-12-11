lucia= 0
carl= 0
a =[0,1,2]
b=[0,1,2]
def claridad ():
    a =[0,1,2]
    b=[0,1,2]
    global lucia
    global carl
    a [0] =int(input("Introduzca la Putuación de Lucía"))
    b [0]= int(input("Introduzca la Putuación de Carlitos"))
    if a[0]<0 or a[0]>100 or b[0]<0 or b[0]>100:
        print("Las puntuaciones asignadas deven estar entre 0 y 100, inclusive")
    else:
        if a[0] > b[0]:
            lucia += 1
            print ("Lucía tiene", lucia, "puntos")
            print ("Carlitos tiene", carl, "puntos" )
        if a[0]< b[0]:
            carl += 1
            print ("Lucía tiene", lucia, "puntos")
            print ("Carlitos tiene", carl, "puntos" )    
        if a[0] == b[0]:
            carl = carl
            lucia=lucia
            print ("Lucía tiene", lucia, "puntos")
            print ("Carlitos tiene", carl, "puntos" )    

def originalidad ():
    a =[0,1,2]
    b=[0,1,2]
    global lucia
    global carl
    a [1] =int(input("Introduzca la Putuación de Lucía"))
    b [1]= int(input("Introduzca la Putuación de Carlitos"))
    if a[1]<0 or a[1]>100 or b[1]<0 or b[1]>100:
        print("Las puntuaciones asignadas deven estar entre 0 y 100, inclusive")
    else:
        if a[1] > b[1]:
            lucia += 1
            print ("Lucía tiene", lucia, "puntos")
            print ("Carlitos tiene", carl, "puntos" )
        if a[1]< b[1]:
            carl += 1
            print ("Lucía tiene", lucia, "puntos")
            print ("Carlitos tiene", carl, "puntos" )    
        if a[1] == b[1]:
            carl = carl
            lucia=lucia
        print ("Lucía tiene", lucia, "puntos")
        print ("Carlitos tiene", carl, "puntos" ) 

def dificultad ():
    a =[0,1,2]
    b=[0,1,2]
    global lucia
    global carl
    a [2] =int(input("Introduzca la Putuación de Lucía"))
    b [2]= int(input("Introduzca la Putuación de Carlitos"))
    if a[2]<0 or a[2]>100 or b[2]<0 or b[2]>100:
        print("Las puntuaciones asignadas deven estar entre 0 y 100, inclusive")
    else:
        if a[2] > b[2]:
            lucia += 1
            print ("Lucía tiene", lucia, "puntos")
            print ("Carlitos tiene", carl, "puntos" )
        if a[0]< b[0]:
            carl += 1
            print ("Lucía tiene", lucia, "puntos")
            print ("Carlitos tiene", carl, "puntos" )    
        if a[2] == b[2]:
            carl = carl
            lucia=lucia
        print ("Lucía tiene", lucia, "puntos")
        print ("Carlitos tiene", carl, "puntos" ) 
print ("PUNTUACIONES") 
print("CLARIDAD")
claridad ()
print("ORIGINALIDAD")
originalidad()
print("DIFICULTAD")
dificultad()
if lucia > carl:
    print ("El trabajo de Lucía ha ganado")
elif lucia < carl:
    print ("El trabajo de Carlitos ha ganado")
else:
    print("EMPATE")
