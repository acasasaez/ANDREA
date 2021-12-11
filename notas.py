alumnos = [["ID"], 
    ["Nota 1"],
    ["Nota 2"],
    ["Nota final"]]
a1= alumnos [0]
a2= alumnos [1]
a3= alumnos [2]
print("ALUMNOS A EVALUAR")
a = int(input())
def al ():
    global alumnos
    alumnos [0] = alumnos.append(int(input("ID")))
    alumnos [1] = alumnos.append(int(input("Nota 1")))
    alumnos [2] = alumnos.append(int(input("Nota 2")))

def notas ():
    global alumnos
    for i in range (a1,a2):
        for j in range (alumnos):
            if alumnos [1][j] > 40 and alumnos [2][j]>40:
        
                if (alumnos [2] - alumnos[3]) <= 3:
                    if ((int(alumnos [2][j]) + int(alumnos[3][j]))/2) == 1:  
                        alumnos [3][j] = alumnos.append(((int(alumnos [2][j]) + int(alumnos[3][j]))/2)+4 )
                    if ((int(alumnos [2][j]) + int(alumnos[3][j]))/2) == 2:  
                        alumnos [3][j] = alumnos.append(((int(alumnos [2][j]) + int( alumnos[3][j]))/2)+3) 
                    if ((int(alumnos [2][j]) + int(alumnos[3][j]))/2) == 3:  
                        alumnos [3][j] = alumnos.append(((int(alumnos [2][j]) + int(alumnos[3][j]))/2)+2) 
                    if ((int(alumnos [2][j]) + int(alumnos[3][j]))/2) == 4:  
                        alumnos [3][j] = alumnos.append((int((alumnos [2][j]) + int(alumnos[3][j]))/2)+1) 
        else:
            alumnos [3][j]=alumnos.append((alumnos [2][j] + alumnos[3][j]//2) )
    else:
        alumnos[3][j] = "suspenso"

while a != alumnos[0]:
    al()
    notas()
print(alumnos)




             