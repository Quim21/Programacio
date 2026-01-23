# Quim Perez - Escacs
negres = ["[♜]", "[♞]", "[♝]", "[♛]", "[♚]", "[♝]", "[♞]", "[♜]"]
peons_negres = ["[♟]","[♟]","[♟]","[♟]","[♟]","[♟]","[♟]","[♟]"]
peons_blanques=["[♙]","[♙]","[♙]","[♙]","[♙]","[♙]","[♙]","[♙]"]
blanques=["[♖]","[♘]","[♗]","[♕]","[♔]","[♗]","[♘]","[♖]"]
cols = 8
files = 8
tauler =  []

def main():
    print("Benvingut al joc d'escacs!\nComençarem per escollir el nom dels jugadors.")
    jugadors_llista = jugadors()
    escacs(jugadors_llista)

def jugadors():
    print("Blanques")
    jugador_1 = nomJugadors()
    print("Negres")
    jugador_2 = nomJugadors()
    jugadors_llista = [jugador_1, jugador_2]
    return jugadors_llista

def generacio_tauler():
    for i in range(files):
        casella = ["[ ]"]*cols
        tauler.append(casella)

    for casella in(tauler):
        fila_seleccio = 0
        seleccio = 0
        for col in(casella):
            tauler[fila_seleccio][seleccio] = negres[seleccio]
            seleccio += 1
        seleccio = 0
        fila_seleccio = 1
        for col in(casella):
            tauler[fila_seleccio][seleccio] = peons_negres[seleccio]
            seleccio += 1
        seleccio = 0
        fila_seleccio = 6
        for col in(casella):
            tauler[fila_seleccio][seleccio] = peons_blanques[seleccio]
            seleccio += 1
        seleccio = 0
        fila_seleccio = 7
        for col in(casella):
            tauler[fila_seleccio][seleccio] = blanques[seleccio]
            seleccio += 1

def imprimir_tauler():
    id = 0
    print(" A   B   C   D   E   F   G   H")
    for casella in(tauler):
        id += 1
        for col in(casella):
            print(col,end=" ")
        print(id)

def escacs(jugadors_llista):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("comença el joc\n")
    generacio_tauler()
    victoria = False
    torn = 0 # 0 = blanc, 1 = negre
    while victoria != True:
        imprimir_tauler()
        casella = moviment()
        print(casella)
        print(f"El jugador {jugadors_llista[torn]} mou la peça a la casella {casella}")
        torn = torns(torn)

def torns(torn):
    if torn == 0:
        torn = 1
    else:
        torn = 0
    return torn

def moviment():
    cords_seleccio = input("Selecciona la peça que vols moure (ex A2): ").lower()
    colu = cords_seleccio[0]
    fila = cords_seleccio[1]
    valors_acceptats =["a","b","c","d","e","f","g","h"]
    fila = int(fila) -1
    colu = valors_acceptats.index(colu)

    validar_moviment(0,fila,colu,valors_acceptats)
    casella_seleccio = f"{colu}{fila}"
    casella= input("Selecciona on vols moure la peça (ex A2): ").lower()
    colu2 = casella[0].lower()
    fila2 = casella[1]
    fila2 = int(fila2) -1
    colu2 = valors_acceptats.index(colu2)
    validar_moviment(0,fila2,colu2,valors_acceptats)
    casella = f"{fila2}{colu2}"
    tauler[fila2][colu2] = tauler[fila][colu]
    tauler[fila][colu] = "[ ]"
    return casella

def validar_moviment(torn,fila,colu,valors_acceptats):
    
    if colu not in valors_acceptats:
        print("Columna no vàlida")
        return
    if int(fila) <=0 or int(fila) >=9:
        print("Fila no vàlida")
        return
    
    if torn == 0:
        if tauler[fila][colu] in blanques:
            return True
    else:
        if tauler[fila][colu] in negres:
            return True
    return False

def nomJugadors():
    valor = input("Introdueix el nom del jugador: ")
    return valor

if __name__ == "__main__":
    main()