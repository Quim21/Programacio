import random
def main():
    sortir = False
    while sortir != True:
        opcio_menu = int(input("Introdueix quin exercici vols executar: "))
        match opcio_menu:
            case 1:
                Exercici1() #Generació informe botiga
            case 2:
                Exercici2() # Salva els pops!
            case 3:
                print("Sortint...") #sortida
                sortir == True
# INICI EXERCICI 1
def despeses_metode():
    mesos = ["Gener","Febrer","Març","Abril","Maig","Juny","Juliol","Agost","Septembre","octubre","Novembre","Decembre"]
    despeses_llista = []
    for i in range(len(mesos)):
        #despeses = llegirDouble(f"Introdueix les despeses del mes de {mesos[i]}: ")
        despeses_llista.append(random.randint(1,100))
    return despeses_llista

def guanys_metode():
    mesos = ["Gener","Febrer","Març","Abril","Maig","Juny","Juliol","Agost","Septembre","octubre","Novembre","Decembre"]
    guanys_llista = []
    
    for i in range(len(mesos)):
        #guanys = llegirDouble(f"Introdueix els guanys del mes de {mesos[i]}: ")
        guanys_llista.append(random.randint(1,100))
    return guanys_llista

def mitjana_despeses(despeses):
    suma = 0
    for n in despeses:
        suma += n
    mitjana_despeses = suma / len(despeses)
    return mitjana_despeses

def mitjana_guanys(guanys):
    suma = 0
    for n in guanys:
        suma += n
    mitjana_guanys = suma / len(guanys)
    return mitjana_guanys

def metode_sobre_mitjana_desp(despeses,mitjana_desp):
    sobre_mitjana_despeses = []
    for j in despeses:
        if j > mitjana_desp:
            sobre_mitjana_despeses.append(j)
    return sobre_mitjana_despeses

def metode_sobre_mitjana_guanys(guanys,mitjana_g):
    sobre_mitjana_guanys = []
    for c in guanys:
        if c > mitjana_g:
            sobre_mitjana_guanys.append(c)
    return sobre_mitjana_guanys
def calcular_benefici(despeses,guanys):
    beneficis = []
    for i in range(12):
        suma = despeses[i] - guanys[i]
        beneficis.append(suma)
    return beneficis

def Exercici1():
    despeses = despeses_metode()
    guanys = guanys_metode()
    print("Despeses: ", despeses)
    print("Guanys: ", guanys)
    mitjana_desp = mitjana_despeses(despeses)
    mitjana_g = mitjana_guanys(guanys)
    print("La mitjana de les despeses es: ", mitjana_desp)
    print("La mitjana dels guanys es:", mitjana_g)
    sobre_mitjana_despeses = metode_sobre_mitjana_desp(despeses,mitjana_desp)
    sobre_mitjana_guanys = metode_sobre_mitjana_guanys(guanys,mitjana_g)
    print("Per sobre de la mitjana: ", sobre_mitjana_despeses)
    print("Per sobre de la mitjana: ", sobre_mitjana_guanys)
    benefici = calcular_benefici(despeses, guanys)
    print("Els beneficis de l'any son: ",benefici)
# FI EXERCICI 1
#----------------
# INICI EXERCICI 2
def Exercici2():
    oficina = crearTauler()
    joc(oficina)
def crearTauler():
    taula = []
    files = 4
    llocs = 5
    for i in range(files):
        fila = []
        for j in range(llocs):
            fila.append(random.randint(1,3))
        taula.append(fila)
    return taula

def mostrarTauler(oficina):
    for fila in oficina:
        for col in fila:
            print(col, end=" ")
        print()

def incident1(oficina):
    incident_burocratic_fila = random.randint(0,3)
    incident_burocratic_col = random.randint(0,4)
    oficina[incident_burocratic_fila][incident_burocratic_col] = oficina[incident_burocratic_fila][incident_burocratic_col] - 1

    return oficina

def cafe(oficina):
    cafe = llegirCadenaText("Has d'enviar cafe a una fila o a una columna... (fila +0,5 o columna +1): ")
    if cafe == "fila":
        fila = llegirEnter("A quina fila vols enviar el cafe?: ")
        cafe_fila(fila,oficina)
    elif cafe == "columna":
        col = llegirEnter("A quina columna vols enviar el cafe?: ")
        cafe_col(col,oficina)

def cafe_fila(fila,oficina):
    for i in range(len(oficina[fila])):
        oficina[fila][i] = oficina[fila][i] + 0.5
    return oficina

def cafe_col(col, oficina):
    for i in range(len(oficina)):
        oficina[i][col] = oficina[i][col] + 1
    return oficina

def pops_morts_metode(oficina):
    pops_morts = 0
    for i in range(len(oficina)):
        for j in range(len(oficina[i])):
            if oficina[i][j] <= 0:
                pops_morts += 1
    return pops_morts

def percentatge_metode(oficina,pops_morts):
    percentatge_1= pops_morts * (4*5) / 100
    print(percentatge_1)
    return percentatge_1

def joc(oficina):
    torn = 0
    while torn != 5:
        mostrarTauler(oficina)
        print("Incident burocratic!\n")
        incident1(oficina)
        mostrarTauler(oficina)
        cafe(oficina)
        torn += 1
    pops_morts = pops_morts_metode(oficina)
    print(f"Han mort {pops_morts} pops")
    percentatge = percentatge_metode(oficina, pops_morts)
    if percentatge >= 70:
        print("Has guanyat!")
    else:
        print("Has tingut un col·lapse administratiu galactic")
 

        


#FI EXERCICI 2
#------------------
#EXTRA
def llegirEnter(text):
    try:
        n = int(input(text))
        return n
    except:
        print("Format de la entrada incorrecta, ha de ser un numero Enter")
    
def llegirDouble(text):
    try:
        n = float(input(text))
        if n is float:
            return n
    except:
        print("Format de la entrada incorrecta, ha de ser un numero decimal")
    

def llegirCadenaText(text):
    try:
        n = str(input(text)).lower()
        if n == "fila" or n == "columna":
            return n
    except:
        print("Text incorrecte")

if __name__ == "__main__":
    main()
