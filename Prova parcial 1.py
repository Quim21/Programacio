#Quim perez
import random
def menu():
    print("Menu de opcions: \n1. Exercici 1: Taules de multiplicar\n2. Exercici 2: Joc de cartes\n3. Exercici 3: Paraula aleatoria\n4. Sortir")
    opcio_menu = input("Tria una opció: ")
    match opcio_menu:
        case "1":
            TaulesDeMultiplicar()
        case "2":
            JocDeCartes()
        case "3":
            ParaulaAleatoria()
        case "4":
            print("Sortint...")

def TaulesDeMultiplicar():
    print("--Taules de multiplicar--\nQue vols fer:\n1. Veure taula de multiplicar (1-10)\n2. Veure totes les taules de multiplicar\n3. Tornar al menu")
    opcio_menu = input("Introdueix una opció: ")
    match opcio_menu:
        case "1":
            print("De quin numero vols veure la taula de multiplicar?: ")
            opcio_taula = llegirEnter()
            
            num = 0
            for i in range(10):
                num += 1
                for j in range(1):
                    resultat = opcio_taula * num
                    print(f"{opcio_taula} * {num} = {resultat}")
            sortir = input("Vols tornar? (s/n): ").lower
            if sortir == "s":
                TaulesDeMultiplicar()

        case "2":
            print("-- Totes les taules de multiplicar --")
            num_taula = 0
            for i in range(10):
                num_taula += 1
                num = 0
                for j in range(10):
                    num += 1
                    resultat = num_taula * num
                    print(f"{num_taula} * {num} = {resultat}")
                print()
            TaulesDeMultiplicar()

        case "3":
            menu()

def JocDeCartes():
    print("Benvingut al joc de les cartes!")

    primera_carta = random.randint(1,12)
    segona_carta = random.randint(1,12)
    intent = 3
    print("S'han generat dues cartes aleatòries!")
    print(segona_carta, primera_carta)
    while intent != 0:
        pista = input("\nQuina pista vols?\n1. Valor de la suma o resta (50/50)\n2. Valor de la multiplicació.\n3. Comprovar carta alta.\n4. Comprovar seqüència de cartes.\nTria una opció: ")
        match pista:
            case "1":
                suma_resta = random.randint(1,2)
                if suma_resta == 1:
                    suma = sumar(primera_carta, segona_carta)
                    print(suma)
                elif suma_resta == 2:
                    resta = restar(primera_carta, segona_carta)
                    print(resta)
                
            case "2":
                multiplicar(primera_carta, segona_carta)
            case "3":
                carta_alta(primera_carta,segona_carta)
            case "4":
                sequencia_carta(primera_carta,segona_carta)

        print("\nQuines creus que es la primera carta?: ")
        resposta_primera_carta = llegirEnter()
        print("I la segona?")
        resposta_segona_carta = llegirEnter()
        if resposta_primera_carta == primera_carta and resposta_segona_carta == segona_carta:
            print(f"\nEnhorabona! Has guanyat!\nLa combinació era {primera_carta} i {segona_carta}")
            menu()
        else:
            intent -= 1
            print(f"\nNo has encertat! tens {intent} restants!")
    print("\nNo has encertat en cap dels intents.")
    print(f"La combinació era {primera_carta} i {segona_carta}")
    menu()
#--- Metodes de la funció Joc de cartes ---        
def sumar(n,m):
    suma = n + m
    return suma
def restar(n,m):
    resta = n - m
    return resta
def multiplicar(n,m):
    multiplicacio = n * m
    print(multiplicacio)
def carta_alta(n,m):
    if n <= 10 and m <= 10:
        print("Cap de les dues cartes és superior a 10")
    if n <= 10 or m <= 10:
        print("Almenys una carta és superior a 10")
def sequencia_carta(n,m):
    if n == m:
        print("les dues cartes són iguals")
    elif n - 1 == m or n + 1 == m:
        print("Les dues cartes són consecutives")
    else:
        print("Les dues cartes no són consecutives")
#--- Metodes de la funció Joc de cartes ---        

def ParaulaAleatoria():
    text = llegirCaracter()
    comptarParaules(text)
    pass

def comptarParaules(n):
    print("Paraules: ")
    paraules = 0
    for i in n:
        print("-", end=" ")
        print(i)
        if i == " ":
            paraules += 1
            print()




        
def trobarParaules():
    pass

def llegirEnter():
    try:
        valor = int(input("Introdueix un numero: "))
        return valor
    except:
        print("Has d'introduir un numero enter")
        return llegirEnter()   
def llegirCaracter():
    try:
        valor = str(input("Introdueix el text: "))
        return valor
    except:
        print("Has d'introduir una cadena de text")
        return llegirCaracter()



if __name__ == "__main__":
    menu()
