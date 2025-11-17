#Comandes d'un restaurant amb match case- Quim Perez



nom_client = ""
nom_producte = ""
preu_unitari = 0.0
quantitat = 0
tiquet = ""
format = 10
preu_total = 0.0
iva = 0.21
total_amb_iva = 0.0
iva_total = 0.0

def menu():
    print(f"_____________________________\n\n --- Cantina Escola Pia ---\n_____________________________\n1. Crea una nova comanda\n2. Actualitzar comanda anterior\n3. veure ultima comanda\n4. Sortir")
    opcio_menu = ""
    while opcio_menu != "4":
        try:
            opcio_menu = input(f"Tria una opcio: ")
            if (opcio_menu == "2" or opcio_menu == "3") and tiquet == "":
                raise ValueError("\nNo hi ha cap comanda per actualitzar o veure.")
        except ValueError as e:
            print(e)
            menu()
        match opcio_menu:
            case "1":
                crear_comanda()
            case "2":
                actualitzar_comanda()
            case "3":
                visualitzar_ultima_comanda()
            case "4":
                print("Sortint...")
                break

def crear_comanda():
    global nom_client, nom_producte, preu_unitari, quantitat, tiquet, format, total_amb_iva, iva, preu_total
    print(f"______________________________________________\n============ 	NOVA COMANDA ============\n______________________________________________\n")
    repetir = False
    tiquet = ""
    preu_total = 0.0
    preu_unitari = 0.0
    iva_total = 0.0
    total_amb_iva = 0.0
    nom_client = input(f"Introdueix el nom del client: ")
    tiquet += f"Client: {nom_client}\nProductes | preu U. | quantitat|\n ------------------------------------------\n"
    
    
    while not repetir:
        nom_producte = input(f"Introdueix el nom del producte: ")
        tiquet += f"{nom_producte:<10}| "
        try:
            preu_unitari = float(input(f"Introdueix el preu unitari: "))
        except ValueError:
            print("Error: Si us plau, introdueix un valor numèric per al preu unitari.")
            crear_comanda()
        else:
            tiquet += f"{preu_unitari:>8.2f}|"
        try:
            quantitat = int(input(f"Introdueix la quantitat: "))
        except ValueError:
            print("Error: Si us plau, introdueix un valor enter per a la quantitat.")
            crear_comanda()
        else:
            tiquet += f"{quantitat:>10}|\n"
        try:
            repetir = input(f"Vols afegir un altre producte a la comanda? (S/N): ").lower()
        except ValueError:
            print("Error: Si us plau, introdueix 'S' per sí o 'N' per no.")
            continue
        preu_total += preu_unitari * quantitat
        iva_total = preu_total * iva
        total_amb_iva = preu_total + iva_total    
        if repetir == "s":
            repetir = False
        else:
            print(f"S'està processant la comanda")
            print("__________________________________________\n========== TIQUET DE LA COMANDA ==========\n__________________________________________\n")
            print(tiquet)
            print(f"__________________________________________\n============ 	TOTAL ============\n__________________________________________\n")
            print(f"Subtotal:                   {preu_total:>8.2f}€")
            print(f"IVA (21%):                  {iva_total:>8.2f}€")
            print(f"Total amb IVA:              {total_amb_iva:>8.2f}€")
            print("__________________________________________")
            print("\n")
            menu()

def actualitzar_comanda():
    global nom_client, nom_producte, preu_unitari, quantitat, tiquet, format, total_amb_iva, iva, preu_total
    print(f"______________________________________________\n========== 	ACTUALITZAR COMANDA ==========\n______________________________________________\n")
    while not repetir:
        nom_producte = input(f"Introdueix el nom del producte: ")
        tiquet += f"{nom_producte:<10}| "
        try:
            preu_unitari = float(input(f"Introdueix el preu unitari: "))
        except ValueError:
            print("Error: Si us plau, introdueix un valor numèric per al preu unitari.")
            crear_comanda()
        else:
            tiquet += f"{preu_unitari:>8.2f}|"
        try:
            quantitat = int(input(f"Introdueix la quantitat: "))
        except ValueError:
            print("Error: Si us plau, introdueix un valor enter per a la quantitat.")
            crear_comanda()
        else:
            tiquet += f"{quantitat:>10}|\n"
        try:
            repetir = input(f"Vols afegir un altre producte a la comanda? (S/N): ").lower()
        except ValueError:
            print("Error: Si us plau, introdueix 'S' per sí o 'N' per no.")
            continue
        preu_total += preu_unitari * quantitat
        iva_total = preu_total * iva
        total_amb_iva = preu_total + iva_total 
        if repetir == "s":
            repetir = False
        else:
            print(f"S'està processant la comanda")
            print("______________________________________________\n========== 	TIQUET DE LA COMANDA ACTUALITZADA ===========\n______________________________________________\n")
            print(tiquet)
            print(f"______________________________________________\n============ 	TOTAL ============\n______________________________________________\n")
            print(f"Subtotal: {preu_total:>8.2f}€")
            print(f"IVA (21%): {iva_total:>8.2f}€")
            print(f"Total amb IVA: {total_amb_iva:>8.2f}€")
            print("______________________________________________")
            menu()

def visualitzar_ultima_comanda():
    global tiquet, iva, total_amb_iva, preu_total, iva_total
    preu_total += preu_unitari * quantitat
    iva_total = preu_total * iva
    total_amb_iva = preu_total + iva_total 
    sortir = "n"
    while sortir != "s":
        print(f"______________________________________________\n============ 	ULTIMA COMANDA ============\n______________________________________________\n")
        print(tiquet)
        print(f"______________________________________________\n============ 	TOTAL ============\n______________________________________________\n")
        print(f"Subtotal: {preu_total:>8.2f}€")
        print(f"IVA (21%): {iva_total:>8.2f}€")
        print(f"Total amb IVA: {total_amb_iva:>8.2f}€")
        print("______________________________________________")
        sortir = input(f"Vols tornar al menu principal? (S/N): ").lower()
        if sortir == "s":
            menu()

menu()