# Quim Perez - La oca
import random
def menu():
    # Menú principal, aqui donarem la opció de jugar (line 15), llegir instruccións (Line 137) o sortir
    print("= = = = LA OCA = = = =")
    print("1. Jugar\n2. Com jugar\n3. Sortir")
    opcio_menu = int(input("Tria una opció: "))
    match opcio_menu:
        case 1:
            jugar()
        case 2:
            instruccions()
        case 3:
            print("Sortint...")
def jugar():
    global guanyar, aux_pou
    torn = 0
    print("= = Jugar = =")
    #primer de tot preguntem el numero de jugadors, variable que utilitzarem mes endevant
    resposta = ""
    while resposta != "s":
        print("Introdueix el numero de jugadors (2-4)")
        num_jugadors = LlegirEnter()
        if num_jugadors < 2 or num_jugadors > 4:
            print("El nombre de jugadors ha de ser entre 2 i 4.")
        #confirmem
        print(f"El numero de jugadors és: {num_jugadors}. És correcte? (S/N)")
        resposta = LlegirCaracter()
    #preguntem el nom de cada jugador i els afegim a una llista
    noms_jugadors = []
    for i in range(num_jugadors):
        print(f"Jugador {i+1}, introdueix el teu nom")
        nom = LlegirCaracter()
        noms_jugadors.append(nom)
    #confirmem els noms
    print("Els jugadors són:")
    for nom in noms_jugadors:
        print(f"- {nom}")
    print("Comença el joc!")
    caselles = [0] * num_jugadors
    primer_torn = [True] * num_jugadors
    penalitzacio = [0] * num_jugadors

    #aqui comença el joc (la tortura)
    while not guanyar:
        #-- Gestió de penalitzacions per torns perduts --
        #si el jugador té penalització, es resta un torn i es passa al següent jugador
        if penalitzacio[torn] > 0:
            penalitzacio[torn] -= 1
            # Si el jugador que estava al pou ja ha complert la seva penalització, surt del pou
            if penalitzacio[torn] == 0 and aux_pou == torn:
                aux_pou = None
            torn = torns(torn, num_jugadors, 0, caselles, noms_jugadors)
            continue
        #-- Torn normal de joc --
        print(f"\nTorn de {noms_jugadors[torn]}. Prem Enter per tirar els daus.")
        input()
        # Tirada dels daus
        dau1 = random.randint(1,6)
        # Si el jugador està a la casella 60 o més, només es tira un dau
        dau2 = 0
        if caselles[torn] <= 60:
            dau2 = random.randint(1,6)
        #suma dels daus i avançament de caselles
        suma_daus = dau1 + dau2
        caselles[torn] += suma_daus
        print(f"S'han tirat els daus: {dau1} i {dau2}, suma: {suma_daus}")
        #-- Gestió de caselles especials --
        # Caselles especials del primer torn
        if primer_torn[torn] == True:
            casella_primer_torn(caselles, torn, noms_jugadors, dau1, dau2, primer_torn)
        elif caselles[torn] in oca:
            casella_oca(caselles, torn, noms_jugadors)
            continue
        # Caselles especials pont
        elif caselles[torn] in pont:
            casella_pont(caselles, torn, noms_jugadors)
            continue
        # Caselles especials fonda
        elif caselles[torn] in fonda:
            casella_fonda(noms_jugadors, torn, penalitzacio)
            continue
        # Caselles especials pou
        elif caselles[torn] in pou:
            casella_pou(noms_jugadors, torn, penalitzacio)
            continue
        # Caselles especials laberint
        elif caselles[torn] in laberint:
            # retrocedeix a la casella 39
            casella_laberint(noms_jugadors, torn, caselles)
            continue
        # Caselles especials presó
        elif caselles[torn] in preso:
            casella_preso(noms_jugadors, torn, penalitzacio)
            continue
        # Caselles especials mort
        elif caselles[torn] in mort:
            # torna a la casella 1
            casella_mort(noms_jugadors, torn, caselles)
            continue
        # Comprovació de victòria
        elif caselles[torn] == 63:
            casella_victoria(noms_jugadors, torn)
            continue
        # rebotament de la casella 63
        elif caselles[torn] > 63:
            casella_rebotament(noms_jugadors, torn, caselles)
            continue
        # Un cop ha jugat el primer torn, marquem que ja no és el primer torn
        primer_torn[torn] = False
        # Final del torn, passem al següent jugador
        torn = torns(torn, num_jugadors, suma_daus, caselles, noms_jugadors)
def casella_oca(caselles, torn, noms_jugadors):
# Caselles especials oca
    # Troba la següent casella d'oca i avança-hi
    num_oca = oca.index(caselles[torn])
    # Assegura que no es surti de l'índex de la llista
    if num_oca < len(oca) - 1:
        num_oca = oca[num_oca + 1] - caselles[torn]
    print(f"{noms_jugadors[torn]} ha caigut en una casella d'oca! Avança a la següent oca.")
    # estableix el total de caselles el numero d'oca corresponent
    caselles[torn] += num_oca
    print(f"caselles actuals: {caselles[torn]}")
def casella_pont(caselles, torn, noms_jugadors):
    print("De puente a puente y tiro porque me lleva la corriente.")
    print(f"{noms_jugadors[torn]} ha caigut en una casella de pont! Avança a la casella 12.")
    # estableix el total de caselles a la casella 12
    caselles[torn] = 12
    print(f"caselles actuals: {caselles[torn]}")
def casella_fonda(noms_jugadors, torn, penalitzacio):
    print(f"{noms_jugadors[torn]} ha caigut en una casella de fonda! Perds un torn.")
    #afegim la penalització
    penalitzacio[torn] = 1
def casella_pou(noms_jugadors, torn, penalitzacio):
    global aux_pou
    # penalització de 2 torns o fins que un altre jugador caigui aquí
    print(f"{noms_jugadors[torn]} ha caigut en una casella de pou! Espera fins que un altre jugador caigui aquí per sortir o perds 2 torns") 
    penalitzacio[torn] = 2
    # variable auxiliar per controlar quin jugador està al pou
    if  aux_pou == None:
        aux_pou = torn
    else:
        print(f"{noms_jugadors[aux_pou]} surt del pou!")
        penalitzacio[aux_pou] = 0
        aux_pou = None
def casella_laberint(noms_jugadors, torn, caselles):
    print(f"{noms_jugadors[torn]} ha caigut en una casella de laberint! Retrocedeix a la casella 39.")
    caselles[torn] = 39
def casella_preso(noms_jugadors, torn, penalitzacio):
# penalització de 3 torns
    print(f"{noms_jugadors[torn]} ha caigut en una casella de presó! Perds 3 torns.")
    penalitzacio[torn] = 3
def casella_mort(noms_jugadors, torn, caselles):
    print(f"{noms_jugadors[torn]} ha caigut en una casella de mort! Torna a la casella 1.")
    caselles[torn] = 1
def casella_rebotament(noms_jugadors, torn, caselles):
    # Nova variable per calcular el rebotament
    excedent = caselles[torn] - 63
    caselles[torn] = 63 - excedent
    print(f"{noms_jugadors[torn]} ha superat la casella 63! Retrocedeix a la casella {caselles[torn]}.")
def casella_victoria(noms_jugadors, torn):
    print(f"Enhorabona, {noms_jugadors[torn]}! Has arribat a la casella 63 i has guanyat la partida!")
    global guanyar
    guanyar = True
def casella_primer_torn(caselles, torn, noms_jugadors, dau1, dau2, primer_torn):
    #condicions especials per al primer torn
    if dau1 == 3 and dau2 == 6 or dau1 == 6 and dau2 == 3:
        print(f"De dado a dado y tiro porque me ha tocado.\n{noms_jugadors[torn]} avança a la casella 26")
        caselles[torn] = 26
        print(f"caselles actuals: {caselles[torn]}")
    elif dau1 == 4 and dau2 == 5 or dau1 == 5 and dau2 == 4:
        print(f"De dado a dado y tiro porque me ha tocado.\n{noms_jugadors[torn]} avança a la casella 53")
        caselles[torn] = 53
        print(f"caselles actuals: {caselles[torn]}")
    primer_torn[torn] = False
# Funció per gestionar el canvi de torn
def torns(torn, num_jugadors, suma_daus, caselles, noms_jugadors):
    print(f"{noms_jugadors[torn]} avança {suma_daus} caselles.") 
    print(f"caselles actuals: {caselles[torn]}")
    # Canvi de torn. Si s'arriba al final de la llista de jugadors, es torna al primer
    torn += 1
    if torn >= num_jugadors:
        torn = 0
    return torn

def instruccions():
    # no té cap secret
    print("- - - Com jugar - - -")
    print("El joc de l'oca consisteix en un tauler amb 63 caselles en forma d’espiral que s’han de recórrer. Es podrà jugar amb 2-4 jugadors. Es juga amb dos daus. La suma del valor dels daus és el nombre de caselles que s’han d’avançar. El primer a arribar a la casella 63 guanya. Hi ha caselles que tenen unes regles concretes i d’altres que no en tenen cap. A partir de la casella 60 només es fa servir un dau\n\nDisfruteu el joc!")
    return menu()

# Funcions de lectura segura d'enter i caràcter
def LlegirEnter():
    # Gestió d'errors en la lectura d'un enter, fins que l'usuari introdueixi un valor correcte, es torna a cridar la funció
    try:
        valor = int(input("Introdueix un valor: "))
        return valor
    except:
        print("Has d'introduir un numero enter")
        return LlegirEnter()     

def LlegirCaracter():
    # Gestió d'errors en la lectura d'un caracter, fins que l'usuari introdueixi un valor correcte, es torna a cridar la funció
    try:
        valor = str(input("Introdueix un text: "))
        return valor
    except:
        print("Has d'introduir un text")
        return LlegirCaracter()
# Punt d'entrada del programa
#definim les caselles especials i iniciem les variables necessaries per al joc
oca = [5,9,14,18,23,27,32,36,41,45,50,54,59]
pont  = [6,12]
fonda = [19]
pou   = [31]
laberint = [42]
preso = [52]
mort = [58]
aux_pou = None
guanyar = False
if __name__ == "__main__":
    menu()