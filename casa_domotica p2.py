#Quim Perez
import time #l'utilitzaré per el bucle de temps
import random
minuts_totals = 0
minuts = 00
hora = 00
dormitori = "el dormitori"
cuina = "la Cuina"
lavabo = "el Lavabo"
sala = "la Sala"
pati_frontal = "el pati frontal"
pati_traser = "el pati traser"
jardi = "el jardi"
dies = 1
finalitzar = 0
#--- menu ---
def menu():
    print(f"\n{hora}:{minuts}\n\n\n--- Menu ---\n Selecciona la aplicació que vols simular:")
    print("1. Control de llums\n2. Control de temperatura\n3. Control d'aspersors\n4. Configuració\n5. Sortir")
    
    opcio_app:int = int(input("Selecciona una opció: "))
    if opcio_app == 1:
        llums()
    if opcio_app == 2:
        temp()
    if opcio_app == 3:
        aspersors()
    if opcio_app == 4:
        conf()
    if opcio_app == 5:
        print("Tancant sistema...")
#---Final Menu ---

#-- Llums --
def llums():
    global dies
    global finalitzar
    global dormitori
    global cuina
    global lavabo
    global sala
    global minuts
    global minuts_totals    
    global hora
    sortir = 0
    while sortir == 0:
        hora_s = ""
        minuts_s = ""
        minuts += 1
        aleatori = random.randint(1, 100)
        altre_aleatori = random.randint(1, 100)
        time.sleep(0.01) #controla la veolicitat (1 segon = 1 hora)
        if minuts == 60:
            minuts = 00
            hora += 1
        if minuts < 10:
            minuts_s = "0"+ str(minuts)
        else:
            minuts_s = str(minuts)
        if hora == 24:
            hora = 00
            finalitzar += 1
        if hora < 10:
            hora_s = "0"+ str(hora)
        else:
            hora_s = str(hora)
        print(f"{hora_s}:{minuts_s}")

        if aleatori == altre_aleatori:
            sala_aleatori = random.choice([sala, cuina, dormitori, lavabo])
            print(f"\n{hora_s}:{minuts_s} la llum de {sala_aleatori} ha sigut encesa/apagada ")
            time.sleep(0.5)

        if finalitzar == dies:
            menu()
#-- Final llums --

#-- Configuració -- 
def conf():
    global dies
    dies = int(input(f"Quants dies ha de durar la simulació?: "))
    menu()
#-- final configuració --

#-- temperatura --
def temp():
    global dies
    global finalitzar
    global dormitori
    global cuina
    global lavabo
    global sala
    global minuts
    global minuts_totals    
    global hora
    sortir = 0
    while sortir == 0:
        hora_s = ""
        minuts_s = ""
        minuts += 1
        aleatori = random.randint(0, 40)
        time.sleep(0.01) #controla la veolicitat (1 segon = 1 hora)
        if minuts == 60:
            minuts = 00
            hora += 1
        if minuts < 10:
            minuts_s = "0"+ str(minuts)
        else:
            minuts_s = str(minuts)
        if hora == 24:
            hora = 00
            finalitzar += 1
        if hora < 10:
            hora_s = "0"+ str(hora)
        else:
            hora_s = str(hora)
        print(f"{hora_s}:{minuts_s}")
        if aleatori <= 15:
            sala_aleatori = random.choice([sala, cuina, dormitori, lavabo])
            print(f"\n{hora_s}:{minuts_s} la temperatura de {sala_aleatori} es mes baixa de la habitual, encenem la calefacció ")
            time.sleep(0.1)
        if aleatori >= 15:
            sala_aleatori = random.choice([sala, cuina, dormitori, lavabo])
            print(f"\n{hora_s}:{minuts_s} la temperatura de {sala_aleatori} es mes alta de la habitual, encenem l'aire acondicionat ")
            time.sleep(0.1)

        if finalitzar == dies:
            menu()
#-- Final temperatura --

#-- Aspersors -- 
def aspersors():
    global dies
    global finalitzar
    global pati_traser
    global jardi
    global pati_frontal
    global minuts
    global minuts_totals    
    global hora
    sortir = 0
    while sortir == 0:
        hora_s = ""
        minuts_s = ""
        minuts += 1
        aleatori = random.randint(0, 200)
        time.sleep(0.01) #controla la veolicitat (1 segon = 1 hora)
        if minuts == 60:
            minuts = 00
            hora += 1
        if minuts < 10:
            minuts_s = "0"+ str(minuts)
        else:
            minuts_s = str(minuts)
        if hora == 24:
            hora = 00
            finalitzar += 1
        if hora < 10:
            hora_s = "0"+ str(hora)
        else:
            hora_s = str(hora)
        print(f"{hora_s}:{minuts_s}")
        if aleatori == 1:
            sala_aleatori = random.choice([pati_traser, pati_frontal, jardi])
            print(f"\n{hora_s}:{minuts_s} ha arribat l'hora de regar {sala_aleatori}, l'aspersor ha sigut activat")
            time.sleep(0.5)
        if finalitzar == dies:
            menu()
#-- Final aspersors
menu()

