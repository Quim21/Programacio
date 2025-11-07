opcio:str = "e"

while opcio != "d":
    print("\n----- Menu -----")
    print("a) Introduir dades")
    print("b) Modificar dades")
    print("c) Visualitzar dades")
    print("d) Sortir")

    opcio:str = str(input("Selecciona un opció: "))

    if opcio == "a":
        try:
            nom:str = input("Introdueix el teu nom: ")
            cognom1:str = input("Introdueix el teu cognom: ")
            cognom2:str = input("Introdueix el teu segon cognom: ")

            if nom == "" or cognom1 == "" or cognom2 == "":
                raise ValueError("Error: Aquest camp no pot quedar buit")

        except Exception as e:
            print(e)
        try: 
            edat = int(input("Introdueix la teva edat: ")) 

            if edat <= 0 or edat >> 120:
                raise ValueError("Error: L'edat ha de ser un enter positiu ≤ 120")
        except Exception as e:
            print(e)
        try:
            pes:float = float(input("Introdueix el teu pes en kg: "))

            if pes >= 400 or pes <= 0:
                raise ValueError("Error: El pes ha de ser un decimal positiu raonable.")
        except Exception as e:
            print(e)
        try:
            alcada:float = float(input("Introdueix la teva alçada en metres (Ex: 1.80): "))
            
            if alcada <= 0.5 or alcada >= 2.5:
                raise ValueError("Error: L'alçada ha de ser un decimal positiu entre 0.5 i 2.5 metres.")
        except Exception as e:
            print(e)
        print(f"Perfecte {nom}, emmagatzem les dades")
    if opcio == "b":
        print(f"Quina opció vols modificar?\n 1.Nom: {nom}\n 2.Cognom: {cognom1}\n 3.Segon Cognom: {cognom2}\n 4.Edat: {edat}\n 5.Pes: {pes}kg\n 6.Alçada: {alcada}m")
        modificacio:int = int(input("Introdueix un numero: "))
        if modificacio == 1:
            nom = input("Introdueix el teu nom: ")
        if modificacio == 2:
            cognom1 = input("Introdueix el teu cognom: ")
        if modificacio == 3:
            cognom2 = input("Introdueix el teu segon cognom: ")
        if modificacio == 4:
            edat = input("Introdueix la teva edat: ")
        if modificacio == 5:
            pes = input("Introdueix el teu pes: ")
        if modificacio == 6:
            alcada = input("Introdueix la teva alçada: ")
    if opcio == "c":
        calculimc:float = pes / (alcada ** 2)
        if calculimc <= 18.5:
            imc:str = "baix"
        if calculimc <= 24.9:
            imc:str = "normal"
        if calculimc <= 29.9:
            imc:str = "sobrepès"
        if  calculimc >= 30:
            imc:str = "obesitat"
        fcmax:int = 220 - edat
        zona_inf:int = round(fcmax * 0.50)
        zona_sup:int = round(fcmax * 0.80)
        aiguaml:int = pes * 35
        litres:int = aiguaml / 1000
        naixament:int = 2025 - edat
        print(f"Hola, {nom} {cognom1} {cognom2}\n Edat: {edat} anys | pes: {pes:.2f}kg | alçada: {alcada:.2f}m\n IMC: {calculimc:.2f} {imc}\n freqüenca cardiaca màxima estimada: {fcmax}bpm\n Zona FC objectiu {zona_inf}-{zona_sup}bpm\n Aigua recomanada {litres} L/dia\n Any de naixement aproximat: {naixament}")