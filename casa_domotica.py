#Quim Perez
menjador = True
cuina = True
dormitori = True
lavabo = True

temp_menjador = 20
temp_cuina = 20
temp_dormitori = 20
temp_lavabo = 20

pati_frontal = False
jardi = False
pati_traser = False
#menu principal
def menu():
    print("\n--- Menu ---\n Selecciona la aplicació que vols obrir:")
    print("1. Control de llums\n2. Control de temperatura\n3. Control d'aspersors\n4. Control de cámeres\n5. Sortir")
#-- Inici llum --
def menu_llums():
    print("--- Llums ---\n Selecciona una opció")
    print("1. Seleccionar una habitació\n2. Apagar/encendre totes les llums\n3. Veure el estat de les llums actuals\n4. Sortir")
    opcio_llums:int = int(input("Selecciona una opció: "))

    if opcio_llums == 1:
        nom_llum:str = str(input(f"-- Sales disponibles --\n(Menjador / Cuina / Dormitori / Lavabo)\nQuina llum vols apagar/encendre?: ")).lower()
        controlar_llum_manual(nom_llum)
        menu_llums()
    if opcio_llums == 2:
        print("l'estat de totes les llums ha canviat")
        totes_llums()
        menu_llums()
    if opcio_llums == 3:
        estat_llums()
        menu_llums()
    if opcio_llums == 4:
        app()

def controlar_llum_manual(nom_llum):
    global menjador, cuina, dormitori, lavabo
    if nom_llum == "menjador":
        menjador = not menjador
    elif nom_llum == "cuina":
        cuina = not cuina
    elif nom_llum == "dormitori":
        dormitori = not dormitori
    elif nom_llum == "lavabo":
        lavabo = not lavabo
    return menjador, cuina, dormitori, lavabo

def totes_llums():
    global menjador, cuina, dormitori, lavabo
    menjador = not menjador
    cuina = not cuina
    dormitori = not dormitori
    lavabo = not lavabo
    return menjador, cuina, dormitori, lavabo
    menu_llums()

def estat_llums():
    print(f"-- Estat actual --\n Menjador: {menjador}\n Cuina: {cuina}\n Dormitori: {dormitori}\n lavabo: {lavabo} ")
#-- Final Llum --
#-- Inici Temperatura --
def menu_temp():
    print("--- Temperatura ---\n Selecciona una opció")
    print("1. Seleccionar una habitació\n2. baixar/pujar la temperatura de totes les habitacions\n3. Veure temperatura actual\n4. Sortir")
    opcio_temp:int = int(input("Selecciona una opció: "))

    if opcio_temp == 1:
        nom_temp:str = str(input(f"-- Sales disponibles --\n(Menjador / Cuina / Dormitori / Lavabo)\nEn quina sala vols baixar/pujar la temperatura?: ")).lower()
        controlar_temp_manual(nom_temp)
        menu_temp()
    if opcio_temp == 2:
        totes_temp()
        menu_temp()
    if opcio_temp == 3:
        estat_temp()
        menu_temp()
    if opcio_temp == 4:
        app()

def controlar_temp_manual(nom_temp):
    global temp_menjador, temp_cuina, temp_dormitori, temp_lavabo
    if nom_temp == "menjador":
        try:
            temp_menjador = int(input("Introdueix la temperatura que vols (Límits: 15º - 30º): "))
            if temp_menjador < 15 or temp_menjador > 30:
                raise ValueError("La temperatura ha d'estar entre 15º i 30º.")
        except ValueError as e:
            print(f"\nError: {e}. Torna-ho a provar.\n")
    if nom_temp == "cuina":
        try:
            temp_cuina = int(input("Introdueix la temperatura que vols (Límits: 15º - 30º): "))
            if temp_cuina < 15 or temp_cuina > 30:
                raise ValueError("La temperatura ha d'estar entre 15º i 30º.")
        except ValueError as e:
            print(f"\nError: {e}. Torna-ho a provar.\n")
    if nom_temp == "dormitori":
        try:
            temp_dormitori = int(input("Introdueix la temperatura que vols (Límits: 15º - 30º): "))
            if temp_dormitori < 15 or temp_dormitori > 30:
                raise ValueError("La temperatura ha d'estar entre 15º i 30º.")
        except ValueError as e:
            print(f"\nError: {e}. Torna-ho a provar.\n")
    if nom_temp == "lavabo":
        try:
            temp_lavabo = int(input("Introdueix la temperatura que vols (Límits: 15º - 30º): "))
            if temp_lavabo < 15 or temp_lavabo > 30:
                raise ValueError("La temperatura ha d'estar entre 15º i 30º.")
        except ValueError as e:
            print(f"\nError: {e}. Torna-ho a provar.\n")
    return temp_cuina, temp_menjador, temp_dormitori, temp_lavabo

def totes_temp():
    global temp_cuina, temp_menjador, temp_dormitori, temp_lavabo
    try:
        temp_global = int(input("Introdueix la temperatura que vols (Límits: 15º - 30º): "))
        if temp_global < 15 or temp_global > 30:
            raise ValueError("La temperatura ha d'estar entre 15º i 30º.")
    except ValueError as e:
            print(f"\nError: {e}. Torna-ho a provar.\n")
    temp_lavabo = temp_global
    temp_menjador = temp_global
    temp_dormitori = temp_global
    temp_cuina = temp_global
    return temp_cuina, temp_menjador, temp_dormitori, temp_lavabo, temp_global

def estat_temp():
    global temp_cuina, temp_menjador, temp_dormitori, temp_lavabo
    print(f"-- Estat actual --\n Menjador: {temp_menjador}ºC\n Cuina: {temp_cuina}ºC\n Dormitori: {temp_dormitori}ºC\n lavabo: {temp_lavabo}ºC")
#-- Final Temperatura --
#-- Inici Aspersors --
def menu_aspersor():
    print("--- Aspersors ---\n Selecciona una opció")
    print("1. Seleccionar una zona\n2. Activar/desactivar tots els aspersors\n3. estat actuals dels aspersors\n4. Sortir")
    opcio_asp:int = int(input("Selecciona una opció: "))

    if opcio_asp == 1:
        nom_zona:str = str(input(f"-- Sales disponibles --\n(pati frontal / jardi / pati traser)\nEn quina zona vols Activar/Desactivar l'asepersor?: ")).lower()
        controlar_asp_manual(nom_zona)
        menu_aspersor()
    if opcio_asp == 2:
        totes_asp()
        menu_aspersor()
    if opcio_asp == 3:
        estat_asp()
        menu_aspersor()
    if opcio_asp == 4:
        app()

def controlar_asp_manual(nom_zona):
    global pati_frontal, pati_traser, jardi
    if nom_zona == "pati frontal":
        pati_frontal = not pati_frontal
    if nom_zona == "pati traser":
        pati_traser = not pati_traser
    if nom_zona == "jardi":
        jardi = not jardi

def totes_asp():
    global pati_frontal, pati_traser, jardi
    pati_frontal = not pati_frontal
    pati_traser = not pati_traser
    jardi = not jardi

def estat_asp():
    global pati_traser, pati_frontal, jardi
    print(f"-- Estat actual --\n Pati frontal: {pati_frontal}\n Pati traser: {pati_traser}\n Jardi: {jardi}\n")
#-- Final Aspersors -- 
#-- Inici cámares --
#- Credencials -
def credencials_cameres():
    print("Per accedir a aquesta aplicació primer has d'iniciar sessió")
    user:str = str(input("Usuari: "))
    passwd:str = str(input("Contrasenya: "))
    if user == "Admin" and passwd == "12345":
        print("Benvingut/da al sistema.")
        menu_cameres()
    else:
        print("Usuari o contrasenya incorrecta, torna a probar-ho")
        app()

def menu_cameres():
    print("\n1. Veure una cámara\n2. veure totes les cámares\n3. Veure Grabacions\n4. Sortir")
    opcio_cam:int = int(input("Selecciona una opció: "))

    if opcio_cam == 1:
        nom_cam:str = str(input(f"-- Cámares disponibles --\n(Menjador / Cuina / Dormitori / Lavabo)\nEn quina cámara et vols connectar?: ")).lower()
        visualitzar_cam_manual(nom_cam)
        menu_cameres()
    if opcio_cam == 2:
        visualitzar_totes_cams()
        menu_cameres()
    if opcio_cam == 3:
        nom_cam:str = str(input(f"-- Cámares disponibles --\n(Menjador / Cuina / Dormitori / Lavabo)\nEn quina cámara et vols connectar?: ")).lower()
        grabacions(nom_cam)
        menu_cameres()
    if opcio_cam == 4:
        app()

def visualitzar_cam_manual(nom_cam):
    #En aquesta part volia mostrar un dibuix ASCII pero es deformaba, he optat per nomes mostrar text
    global menjador, cuina, dormitori, lavabo
    Menjador_sortida = 2
    dormitori_sortida = 2
    cuina_sortida = 2
    lavabo_sortida = 2
    if nom_cam == "menjador":
        while Menjador_sortida == 2:
            print(f"\n\n\n\n\n\n\ncam1 'Menjador'")
            Menjador_sortida:int = int(input("1. Sortir: "))
        menu_cameres()
    elif nom_cam == "cuina":
        while cuina_sortida == 2:
            print(f"\n\n\n\n\n\n\ncam2 'Cuina'")
            cuina_sortida:int = int(input("1. Sortir: "))
        menu_cameres()
    elif nom_cam == "dormitori":
        while dormitori_sortida == 2:
            print(f"\n\n\n\n\n\n\ncam3 'Dormitori'")
            dormitori_sortida:int = int(input("1. Sortir: "))
        menu_cameres()
    elif nom_cam == "lavabo":
        while lavabo_sortida == 2:
            print(f"\n\n\n\n\n\n\ncam4 'Lavabo'")
            lavabo_sortida:int = int(input("1. Sortir: "))
        menu_cameres()

def visualitzar_totes_cams():
    sortida = 2
    while sortida == 2:
        print(f"\n\n\n\n\n\n\nCám 1. Menjador / Cám 2. Cuina / Cám 3. Dormitori / Cám 4. Lavabo")
        sortida:int = int(input("1. Sortir: "))
    menu_cameres()

def grabacions(nom_cam):
    Menjador_sortida = 2
    dormitori_sortida = 2
    cuina_sortida = 2
    lavabo_sortida = 2
    dia:int = int(input("Introdueix un dia del mes (01 - 30): "))
    mes:int = int(input("Introdueix el mes de l'any (01 - 12: ): "))
    any:int = int(input("Introdueix l'any (2000 - 2025: )"))
    if nom_cam == "menjador":
        while Menjador_sortida == 2:
            print(f"\n\n\n\n\n\n {dia}-{mes}-{any} \ncam1 'Menjador'")
            Menjador_sortida:int = int(input("1. Sortir: "))
        menu_cameres()
    elif nom_cam == "cuina":
        while cuina_sortida == 2:
            print(f"\n\n\n\n\n\n {dia}-{mes}-{any} \ncam2 'Cuina'")
            cuina_sortida:int = int(input("1. Sortir: "))
        menu_cameres()
    elif nom_cam == "dormitori":
        while dormitori_sortida == 2:
            print(f"\n\n\n\n\n\n {dia}-{mes}-{any}\ncam3 'Dormitori'")
            dormitori_sortida:int = int(input("1. Sortir: "))
        menu_cameres()
    elif nom_cam == "lavabo":
        while lavabo_sortida == 2:
            print(f"\n\n\n\n\n\n {dia}-{mes}-{any}\ncam4 'Lavabo'")
            lavabo_sortida:int = int(input("1. Sortir: "))
        menu_cameres()

def app():
    menu()
    opcio_app:int = int(input("Selecciona una opció: "))
    if opcio_app == 1:
        menu_llums()
    if opcio_app == 2:
        menu_temp()
    if opcio_app == 3:
        menu_aspersor()
    if opcio_app == 4:
        credencials_cameres()
    if opcio_app == 5:
        print("Tancant sistema...")

app()