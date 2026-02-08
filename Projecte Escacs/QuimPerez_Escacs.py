# Quim Perez - Escacs
#variables globals
negres = ["[♜]", "[♞]", "[♝]", "[♛]", "[♚]", "[♝]", "[♞]", "[♜]"]
peons_negres = ["[♟]"] *8
peons_blanques = ["[♙]"] *8
blanques = ["[♖]", "[♘]", "[♗]", "[♕]", "[♔]", "[♗]", "[♘]", "[♖]"]
peces_eliminades_blanques = []
peces_eliminades_negres = []
cols = 8
files = 8
tauler = []
w_b = ["Blanques", "Negres"]

#func per iniciar el codi
def main():
    print("Benvingut al joc d'escacs!\nComençarem per escollir el nom dels jugadors.")
    jugadors_llista = jugadors()
    escacs(jugadors_llista)

#fun per gestionar els jugadors
def jugadors():
    print("Blanques")
    jugador_1 = nomJugadors()
    print("Negres")
    jugador_2 = nomJugadors()
    jugadors_llista = [jugador_1, jugador_2]
    return jugadors_llista

# func per generar el tuler
def generacio_tauler():
    tauler.clear()
    for _ in range(files):
        casella = ["[ ]"] * cols
        tauler.append(casella)

    for c in range(cols):
        tauler[0][c] = negres[c]
    for c in range(cols):
        tauler[1][c] = peons_negres[c]
    for c in range(cols):
        tauler[6][c] = peons_blanques[c]
    for c in range(cols):
        tauler[7][c] = blanques[c]

# func per imprimir el tauler
def imprimir_tauler():
    print("    A   B   C   D   E   F   G   H")
    num_fila = 1
    for fila in tauler:
        print(num_fila, end=" ")
        for col in fila:
            print(col, end=" ")
        print(num_fila)
        num_fila += 1
    print("    A   B   C   D   E   F   G   H")
    
    print("\nBlanques eliminades:", end=" ")
    for peca in peces_eliminades_blanques:
        print(peca, end=" ")
    print()
    
    print("Negres eliminades:", end=" ")
    for peca in peces_eliminades_negres:
        print(peca, end=" ")
    print()

# func ppal del joc
def escacs(jugadors_llista):
    print("\n" * 10)
    print("Comença el joc\n")
    generacio_tauler()
    victoria = False
    torn = 0  # 0 = blancs, 1 = negres
    while not victoria:
        print("És el torn de les", w_b[torn])
        imprimir_tauler()
        casella = moviment(torn, jugadors_llista)
        if casella == "ABANDONAR":
            break
        print(f"El jugador {jugadors_llista[torn]} mou la peça a la casella {casella}\n")
        torn = torns(torn)

# no te cap secret
def torns(torn):
    if torn == 0:
        return 1
    else:
        return 0

#func per validar l'entrada de les coordenades
def validar_entrada(missatge):
    try:
        entrada = input(missatge).lower()
        if entrada == "abandonar":
            return "abandonar" 
        col = entrada[0]
        fila = int(entrada[1])
        if len(entrada) == 2 and col in "abcdefgh" and 1 <= fila <= 8:
            return entrada
        print("Format incorrecte. Exemple: A2")
        return validar_entrada(missatge)
    except:
        print("Format incorrecte. Exemple: A2")
        return validar_entrada(missatge)

# func per realitzar el moviment (tortura)
def moviment(torn, jugadors_llista):
    valors_acceptats = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
    cords_seleccio = validar_entrada("Selecciona la peça que vols moure (ex A2): ")
    if cords_seleccio == "abandonar":
        guanyador = jugadors_llista[1-torn]  
        print(f"{guanyador} guanya! {jugadors_llista[torn]} ha abandonat.")
        return "ABANDONAR"
    colu = cords_seleccio[0]
    fila = int(cords_seleccio[1]) -1
    colu = valors_acceptats.index(colu)
    
    if fila < 0 or fila > 7:
        print("Fila fora de rang.")
        return moviment(torn)
    
    if not detectar_moviment(torn, fila, colu):
        return moviment(torn)
    
    peça = tauler[fila][colu]
    
    casella = validar_entrada("Selecciona on vols moure la peça (ex A3): ")
    colu2 = casella[0]
    fila2 = int(casella[1]) -1
    colu2 = valors_acceptats.index(colu2)
    
    if fila2 < 0 or fila2 > 7:
        print("Fila fora de rang.")
        return moviment(torn)
    
    peça_destí = tauler[fila2][colu2]
    
    if peça == "[♙]":
        if not peo_blanc(fila, colu, fila2, colu2):
            print("Moviment de peó blanc il·legal")
            return moviment(torn)
    elif peça == "[♟]":
        if not peo_negre(fila, colu, fila2, colu2):
            print("Moviment de peó negre il·legal")
            return moviment(torn)
    elif peça == "[♘]":
        if not cavall_blanc(fila, colu, fila2, colu2):
            print("Moviment cavall blanc il·legal")
            return moviment(torn)
    elif peça == "[♞]":
        if not cavall_negre(fila, colu, fila2, colu2):
            print("Moviment cavall negre il·legal")
            return moviment(torn)
    elif peça == "[♖]":
        if not torre_blanc(fila, colu, fila2, colu2):
            print("Moviment torre blanca il·legal")
            return moviment(torn, jugadors_llista)
    elif peça == "[♜]":
        if not torre_negra(fila, colu, fila2, colu2):
            print("Moviment torre negra il·legal")
            return moviment(torn, jugadors_llista)
    elif peça == "[♗]":
        if not alfil_blanc(fila, colu, fila2, colu2):
            print("Moviment alfil blanc il·legal")
            return moviment(torn, jugadors_llista)
    elif peça == "[♝]":
        if not alfil_negre(fila, colu, fila2, colu2):
            print("Moviment alfil negre il·legal")
            return moviment(torn, jugadors_llista)
    elif peça == "[♕]":
        if not reina_blanca(fila, colu, fila2, colu2):
            print("Moviment reina blanca il·legal")
            return moviment(torn, jugadors_llista)
    elif peça == "[♛]":
        if not reina_negra(fila, colu, fila2, colu2):
            print("Moviment reina negra ILLEGAL")
            return moviment(torn, jugadors_llista)
    elif peça == "[♔]":
        if not rei_blanc(fila, colu, fila2, colu2):
            print("Moviment rei blanc ILLEGAL")
            return moviment(torn, jugadors_llista)
    elif peça == "[♚]":
        if not rei_negre(fila, colu, fila2, colu2):
            print("Moviment rei negre ILLEGAL")
            return moviment(torn, jugadors_llista)


        
    if peça_destí != "[ ]":
        if torn == 0:
            peces_eliminades_negres.append(peça_destí)
        else:
            peces_eliminades_blanques.append(peça_destí)
    
    tauler[fila2][colu2] = tauler[fila][colu]
    tauler[fila][colu] = "[ ]"
    
    return casella.upper()

#comprobar si la peça seleccionada es valida per al torn
def detectar_moviment(torn, fila, colu):
    if torn == 0:
        if tauler[fila][colu] in blanques or tauler[fila][colu] in peons_blanques:
            print("Peça blanca vàlida")
            return True
        else:
            print("Peça no vàlida per a blancs")
            return False
    else:
        if tauler[fila][colu] in negres or tauler[fila][colu] in peons_negres:
            print("Peça negra vàlida")
            return True
        else:
            print("Peça no vàlida per a negres")
            return False

#func per demanar el nom dels jugadors
def nomJugadors():
    valor = input("Introdueix el nom del jugador: ")
    return valor

#moviment peo blanc
def peo_blanc(fila, col, fila2, col2):
    if col == col2 and fila2 == fila - 1:
        if tauler[fila2][col2] == "[ ]":
            return True
    
    if fila == 6 and col == col2 and fila2 == fila - 2:
        if tauler[fila-1][col] == "[ ]" and tauler[fila2][col2] == "[ ]":
            return True
    
    if fila2 == fila - 1 and abs(col - col2) == 1:
        peça_destí = tauler[fila2][col2]
        if peça_destí in negres or peça_destí in peons_negres:
            return True
    
    return False

#moviment peo negre
def peo_negre(fila, col, fila2, col2):
    if col == col2 and fila2 == fila + 1:
        if tauler[fila2][col2] == "[ ]":
            return True
    
    if fila == 1 and col == col2 and fila2 == fila + 2:
        if tauler[fila+1][col] == "[ ]" and tauler[fila2][col2] == "[ ]":
            return True
    
    if fila2 == fila + 1 and abs(col - col2) == 1:
        peça_destí = tauler[fila2][col2]
        if peça_destí in blanques or peça_destí in peons_blanques:
            return True
    
    return False

#moviment torre blanca
def torre_blanc(fila, col, fila2, col2):
    if fila != fila2 and col != col2:
        return False
    # per a les files
    if fila == fila2:
        pas = 1 if col2 > col else -1
        for c in range(col + pas, col2, pas):
            if tauler[fila][c] != "[ ]":
                return False
        return True
    
    # per a les columnes
    pas = 1 if fila2 > fila else -1
    for f in range(fila + pas, fila2, pas):
        if tauler[f][col] != "[ ]":
            return False
    return True

# moviment torre negra
def torre_negra(fila, col, fila2, col2):
    if fila != fila2 and col != col2:
        return False
    # per a les files
    if fila == fila2:
        pas = 1 if col2 > col else -1
        for c in range(col + pas, col2, pas):
            if tauler[fila][c] != "[ ]":
                return False
        return True
    
    # per a les columnes
    pas = 1 if fila2 > fila else -1
    for f in range(fila + pas, fila2, pas):
        if tauler[f][col] != "[ ]":
            return False
    return True

# moviment cavall blanc
def cavall_blanc(fila, col, fila2, col2):
    deltas = [(-2,-1), (-2,+1), (+2,-1), (+2,+1), 
              (-1,-2), (-1,+2), (+1,-2), (+1,+2)]
    
    for delta_fila, delta_col in deltas:
        if fila + delta_fila == fila2 and col + delta_col == col2:
            return True
    return False

# moviment cavall negre
def cavall_negre(fila, col, fila2, col2):
    deltas = [(-2,-1), (-2,+1), (+2,-1), (+2,+1), 
              (-1,-2), (-1,+2), (+1,-2), (+1,+2)]
    
    for delta_fila, delta_col in deltas:
        if fila + delta_fila == fila2 and col + delta_col == col2:
            return True
    return False

def alfil_blanc(fila, col, fila2, col2):
    if abs(fila - fila2) != abs(col - col2):
        return False
    
    pas_fila = 1 if fila2 > fila else -1
    pas_col = 1 if col2 > col else -1
    
    for i in range(1, abs(fila - fila2)):
        f = fila + i * pas_fila
        c = col + i * pas_col
        if tauler[f][c] != "[ ]":
            return False
    return True

def alfil_negre(fila, col, fila2, col2):
    if abs(fila - fila2) != abs(col - col2):
        return False
    
    pas_fila = 1 if fila2 > fila else -1
    pas_col = 1 if col2 > col else -1
    
    for i in range(1, abs(fila - fila2)):
        f = fila + i * pas_fila
        c = col + i * pas_col
        if tauler[f][c] != "[ ]":
            return False
    return True


def reina_blanca(fila, col, fila2,col2):
    if fila == fila2 or col == col2:
        if fila == fila2:
            pas = 1 if col2 > col else -1
            for c in range(col + pas, col2, pas):
                if tauler[fila][c] != "[ ]":
                    return False
            return True
        
        pas = 1 if fila2 > fila else -1
        for f in range(fila + pas, fila2, pas):
            if tauler[f][col] != "[ ]":
                return False
        return True
    
    if abs(fila - fila2) == abs(col - col2):
        pas_fila = 1 if fila2 > fila else -1
        pas_col = 1 if col2 > col else -1
        for i in range(1, abs(fila - fila2)):
            f = fila + i * pas_fila
            c = col + i * pas_col
            if tauler[f][c] != "[ ]":
                return False
        return True
    
    return False


def reina_negra(fila, col, fila2, col2):
    if fila == fila2 or col == col2:
        if fila == fila2:
            pas = 1 if col2 > col else -1
            for c in range(col + pas, col2, pas):
                if tauler[fila][c] != "[ ]":
                    return False
            return True
        
        pas = 1 if fila2 > fila else -1
        for f in range(fila + pas, fila2, pas):
            if tauler[f][col] != "[ ]":
                return False
        return True
    
    if abs(fila - fila2) == abs(col - col2):
        pas_fila = 1 if fila2 > fila else -1
        pas_col = 1 if col2 > col else -1
        for i in range(1, abs(fila - fila2)):
            f = fila + i * pas_fila
            c = col + i * pas_col
            if tauler[f][c] != "[ ]":
                return False
        return True
    
    return False



def rei_blanc(fila, col, fila2, col2):
    dist_fila = abs(fila - fila2)
    dist_fila_max = 1
    dist_col = abs(col - col2)
    dist_col_max = 1
    
    if dist_fila > dist_fila_max or dist_col > dist_col_max:
        return False
    
    if fila == fila2 and col == col2:
        return False
    
    return True




def rei_negre(fila, col, fila2, col2):
    dist_fila = abs(fila - fila2)
    dist_fila_max = 1
    dist_col = abs(col - col2)
    dist_col_max = 1
    
    if dist_fila > dist_fila_max or dist_col > dist_col_max:
        return False
    
    if fila == fila2 and col == col2:
        return False
    
    return True

# inici del programa
if __name__ == "__main__":
    main()

