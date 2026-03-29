# Quim Perez - Joc RPG amb herencia
import random
class joc:
    #metode constructor per inicialitzar la llista de personatges
    def __init__(self):
        self.personatges = []
        self.armes_disponibles = [
            arma("Espasa", "cos a cos", 12, 0),
            arma("Arc curt", "distància", 8, 0),
            arma("Bastó de fusta", "màgia", 4, 10),
            arma("Daga", "cos a cos", 6, 0)
        ]

    #metode per imprimir el menu
    def menu(self):
        print("----- Joc RPG -----")
        print("1. Jugar")
        print("2. Crear un personatge")
        print("3. Mostrar personatges")
        print("4. Sortir")
    
    #metode per executar el menu
    def executar(self):
        opcio = 0
        while opcio != 4:
            self.menu()
            opcio = self.try_menu()
            match opcio:
                case 1:
                    self.jugar()
                case 2:
                    self.crear_personatge()
                case 3:
                    self.mostrar_personatges()
                case 4:
                    print("Sortint...")
                    break

    def crear_personatge(self):
        print("-- Crear personatge --\n")
        nom = input("Introdueix el nom del personatge: ")
        raça = self.try_raça()
        edat = int(input(f"Introdueix la edat de {nom}: "))
        print("Aquest es el teu personatge: ")
        print("nom: ", nom)
        print("raça: ", raça)
        print("edat: ", edat)
        input("prem enter per continuar: ")
        força, destresa, constitucio, inteligencia, saviesa, carisma = self.sistema_punts()
        final = input("Si estàs satisfet amb els teus atributs, prem enter per continuar o introdueix 'reset' per reiniciar els punts: ").lower()
        if final == "reset":
            self.sistema_punts()
        else:
            print("Personatge creat amb èxit!")
            if raça == "humà":
                self.personatges.append(Huma(nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma))
            elif raça == "elf":
                self.personatges.append(Elf(nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma))
            elif raça == "orc":
                self.personatges.append(Orc(nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma))
            elif raça == "nan":
                self.personatges.append(Nan(nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma))

    def sistema_punts(self):
        print("\n\n\n\n\n\n\n\n\n\n\n")
        punts = 30
        força = 5
        destresa = 5
        constitucio = 5
        inteligencia = 5
        saviesa = 5
        carisma = 5
        atributs = [força,destresa,constitucio,inteligencia,saviesa,carisma]

        while punts != 0:
            print(f"== Atributs ==\n1. Força: {força}\n2. Destresa: {destresa}\n3. Constitució: {constitucio}\n4. Intel·ligència: {inteligencia}\n5. Saviesa: {saviesa}\n6. Carisma: {carisma}")
            print(f"tens {punts} punts ")
            seleccio_atribut = self.llegir_enter("Introdueix a quin atribut vols aplicar els punts (1-6): ")
            aplicar_punts = self.llegir_enter("Introdueix quants punts vols utilitzar: ")
            if aplicar_punts > punts:
                print("quantitat insuficient de punts!")
                continue
            if seleccio_atribut == 1:
                if força + aplicar_punts <= 20:
                    força += aplicar_punts
                    punts -= aplicar_punts
                else:
                    print("No pot superar els 20 punts!")
            elif seleccio_atribut == 2:
                if destresa + aplicar_punts <= 20:
                    destresa += aplicar_punts
                    punts -= aplicar_punts
                else:
                    print("No pot superar els 20 punts!")
                    
            elif seleccio_atribut == 3:
                if constitucio + aplicar_punts <= 20:
                    constitucio += aplicar_punts
                    punts -= aplicar_punts
                else:
                    print("No pot superar els 20 punts!")
                    
            elif seleccio_atribut == 4:
                if inteligencia + aplicar_punts <= 20:
                    inteligencia += aplicar_punts
                    punts -= aplicar_punts
                else:
                    print("No pot superar els 20 punts!")
                    
            elif seleccio_atribut == 5:
                if saviesa + aplicar_punts <= 20:
                    saviesa += aplicar_punts
                    punts -= aplicar_punts
                else:
                    print("No pot superar els 20 punts!")
                    
            elif seleccio_atribut == 6:
                if carisma + aplicar_punts <= 20:
                    carisma += aplicar_punts
                    punts -= aplicar_punts
                else:
                    print("No pot superar els 20 punts!")
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Atributs finals:")
        print(f"== Atributs ==\n1. Força: {força}\n2. Destresa: {destresa}\n3. Constitució: {constitucio}\n4. Intel·ligència: {inteligencia}\n5. Saviesa: {saviesa}\n6. Carisma: {carisma}")
        return força, destresa, constitucio, inteligencia, saviesa, carisma
        
    def llegir_enter(self,text):
        while True:
            try:
                valor = int(input(text))
                return valor                
            except ValueError:
                print("Has de escriure un numero enter")
        
    def try_raça(self):
        raçes = ["elf", "orc", "nan", "humà"]
        while True:
            try:
                raça = input("Introdueix la raça del personatge (Elf, Orc, Nan, Humà ): ").lower()
                if raça in raçes:
                    return raça
                else:
                    raise ValueError
            except ValueError:
                print("Aquesta raça no es valida. Selecciona una valida")

    def try_menu(self):
        s = 1
        while True:
            try:
                opcio = int(input("Escull una opció: "))
                if opcio < 1 or opcio > 4:
                    raise ValueError
                return opcio
            except ValueError:
                print("Has d'introduir un número valid entre 1 i 4\n")

    def mostrar_personatges(self):
        if len(self.personatges) == 0:
            print("No hi ha personatges creats")
        else:
            i = 0
            print("\n-- Llista de personatges --\n")
            for p in self.personatges:
                i += 1
                print(f"- Personatge {i} -")
                print(f"Nom: {p.nom}\nRaça: {p.raça}\nEdat: {p.edat}")
                print(f"Vida: {p.vida_maxima}\nMana: {p.mana_maxim}")
                print(f"\nForça: {p.força}\nDestresa: {p.destresa}\nConstitució: {p.constitucio}\nIntel·ligència: {p.inteligencia}\nSaviesa: {p.saviesa}\nCarisma: {p.carisma}\n")

    def jugar(self):
        opcio = 0
        while opcio != 3:
            print("\n-- MENÚ JOC --")
            print("1. Jugar PvP")
            print("2. Equipar arma")
            print("3. Tornar al menú principal")
            opcio = self.try_menu()
            match opcio:
                case 1:
                    if len(self.personatges) == 0:
                        print("No tens personatges per jugar!")
                        input("Prem enter...")
                        return
                    elif len(self.personatges) < 2:
                        print("Necessites com a mínim 2 personatges per fer PvP!")
                        input("Prem enter...")
                        return
        
                    print("\n-- SELECCIONA PRIMER PERSONATGE --")
                    numero_p1 = 1
                    for p in self.personatges:
                        arma_info = p.arma_actual()
                        print(f"{numero_p1}. {p.nom} - {arma_info}")
                        numero_p1 += 1
                    
                    numero_jugador1 = self.llegir_enter("Tria primer personatge: ")
                    if numero_jugador1 < 1 or numero_jugador1 > len(self.personatges):
                        print("Personatge invàlid!")
                        return
                    
                    jugador1 = self.personatges[numero_jugador1 - 1]

                    print("\n-- SELECCIONA SEGON PERSONATGE --")
                    numero_p2 = 1
                    i = 0
                    for p in self.personatges:
                        if i + 1 != numero_jugador1:
                            arma_info = p.arma_actual()
                            print(f"{numero_p2}. {p.nom} - {arma_info}")
                            numero_p2 += 1
                        i += 1
                    
                    numero_jugador2 = self.llegir_enter("Tria segon personatge: ")
                    if numero_jugador2 < 1 or numero_jugador2 > len(self.personatges) - 1:
                        print("Personatge invàlid!")
                        return
                    
                    comptador = 0
                    i = 0
                    for p in self.personatges:
                        if i + 1 != numero_jugador1:
                            comptador += 1
                            if comptador == numero_jugador2:
                                jugador2 = p
                                break
                        i += 1
                    
                    jugador1.vida = jugador1.vida_maxima
                    jugador1.mana = jugador1.mana_maxim
                    jugador2.vida = jugador2.vida_maxima
                    jugador2.mana = jugador2.mana_maxim
                    
                    print(f"\n== COMENÇA LA BATALLA ==")
                    print(f"{jugador1.nom} vs {jugador2.nom}")
                    input("Prem enter per començar...")
                    
                    torn = 1
                    defensa_activa = [False, False]
                    
                    while jugador1.vida > 0 and jugador2.vida > 0:
                        if torn == 1:
                            actual = jugador1
                            enemic = jugador2
                            idx_actual = 0
                            idx_defensa = 0
                        else:
                            actual = jugador2
                            enemic = jugador1
                            idx_actual = 1
                            idx_defensa = 1
                        
                        print(f"\n-- TORN DE {actual.nom} --")
                        print(f"{actual.nom} - Vida: {actual.vida}/{actual.vida_maxima}, Mana: {actual.mana}/{actual.mana_maxim}")
                        print(f"{enemic.nom} - Vida: {enemic.vida}/{enemic.vida_maxima}, Mana: {enemic.mana}/{enemic.mana_maxim}")
                        
                        print("\n1. Atacar")
                        print("2. Regenerar vida")
                        print("3. Regenerar maná")
                        print("4. Esquivar")
                        print("5. Defensar-se")
                        print("6. Usar habilitat")
                        
                        accio = self.llegir_enter("Tria una acció: ")
                        
                        match accio:
                            case 1:
                                prob_esquivar = (enemic.destresa - 5) * 3.33
                                esquiva = random.randint(1, 100) <= prob_esquivar
                                
                                if esquiva:
                                    print(f"{enemic.nom} esquiva l'atac!")
                                else:
                                    dany = actual.calcular_dany()
                                    
                                    if defensa_activa[1 - idx_actual]:
                                        dany = actual.aplicar_defensa(dany)
                                        defensa_activa[1 - idx_actual] = False
                                    
                                    enemic.vida -= dany
                                    if enemic.vida < 0:
                                        enemic.vida = 0
                                    print(f"{actual.nom} fa {dany} de dany a {enemic.nom}!")
                            
                            case 2:
                                regeneracio = actual.regenerar_vida()
                                print(f"{actual.nom} regenera {regeneracio} de vida (ara: {actual.vida}/{actual.vida_maxima})")
                            
                            case 3:
                                regeneracio_mana = actual.regenerar_mana()
                                print(f"{actual.nom} regenera {regeneracio_mana} de maná (ara: {actual.mana}/{actual.mana_maxim})")
                            
                            case 4:
                                print(f"{actual.nom} es prepara per esquivar el proper atac!")
                                defensa_activa[idx_defensa] = True
                            
                            case 5:
                                print(f"{actual.nom} es posa a defensar-se (mitad dany proper)!")
                                defensa_activa[idx_defensa] = True
                            
                            case 6:
                                if len(actual.habilitats) == 0:
                                    print("No tens habilitats disponibles!")
                                else:
                                    print("\n-- HABILITATS --")
                                    for idx, hab in enumerate(actual.habilitats):
                                        print(f"{idx + 1}. {hab.nom} - Cost: {hab.cost_mana} maná")
                                    
                                    num_hab = self.llegir_enter("Tria habilitat: ")
                                    if num_hab < 1 or num_hab > len(actual.habilitats):
                                        print("Habilitat invàlida!")
                                    else:
                                        hab_seleccionada = actual.habilitats[num_hab - 1]
                                        if actual.mana < hab_seleccionada.cost_mana:
                                            print("No tens prou maná!")
                                        else:
                                            actual.mana -= hab_seleccionada.cost_mana
                                            resultat = hab_seleccionada.usar(actual, enemic)
                                            print(resultat)
                            
                            case _:
                                print("Acció invàlida! Torn perdut.")
                        
                        if actual.vida <= 0 or enemic.vida <= 0:
                            break
                        
                        torn = 3 - torn
                    
                    if jugador1.vida <= 0:
                        guanyador = jugador2
                    else:
                        guanyador = jugador1
                    
                    print(f"\n{guanyador.nom} HA VENÇUT!")
                    print(f"Final - {jugador1.nom}: {jugador1.vida}/{jugador1.vida_maxima}")
                    print(f"Final - {jugador2.nom}: {jugador2.vida}/{jugador2.vida_maxima}")
                    input("Prem enter per continuar...")
                case 2:
                    self.equipar_arma()
                case 3:
                    break
                    
    def equipar_arma(self):
        if len(self.personatges) == 0:
            print("No tens personatges!")
            input("Prem enter...")
            return
        print("\n-- PERSONATGES --")
        numero_p = 1
        for p in self.personatges:
            arma_info = p.arma_actual()
            print(f"{numero_p}. {p.nom} - {arma_info}")
            numero_p += 1

        numero_personatge = self.llegir_enter("Tria personatge: ")
        if numero_personatge < 1 or numero_personatge > len(self.personatges):
            print("Personatge invàlid!")
            return

        personatge = self.personatges[numero_personatge - 1]

        print("\n-- ARMES DISPONIBLES --")
        numero_a = 1
        for a in self.armes_disponibles:
            print(f"{numero_a}. {a.nom} (tipus: {a.tipus}, dany: {a.dany}, màgia: {a.magia})")
            numero_a += 1

        numero_arma = self.llegir_enter("Tria arma: ")
        if numero_arma < 1 or numero_arma > len(self.armes_disponibles):
            print("Arma invàlida!")
            return

        arma_escollida = self.armes_disponibles[numero_arma - 1]
        personatge.equipar_arma(arma_escollida)
        
        input("Prem enter per continuar...")
        
class Personatge:
    #definim el metode constructor
    def __init__(self, nom, raça, edat, força, destresa, constitucio, inteligencia, saviesa, carisma):
        self.nom = nom
        self.raça = raça
        self.edat = edat
        self.força = força
        self.destresa = destresa
        self.constitucio = constitucio
        self.inteligencia = inteligencia
        self.saviesa = saviesa
        self.carisma = carisma
        self.aplicar_modificadors_racials()
        self.set_vida_maxima()
        self.vida = self.vida_maxima
        self.set_mana_maxim()
        self.mana = self.mana_maxim
        self.armes = []
        self.arma_equipada = None
        self.habilitats = []
        self.afegir_habilitats_inicials()
    
    def aplicar_modificadors_racials(self):
        pass
    
    def afegir_habilitats_inicials(self):
        pass
        
    def equipar_arma(self, arma):
        if arma.magia > 0 and self.inteligencia < 10:
            print(f"No pots equipar {arma.nom}! Necessites intel·ligència >= 10 per armes màgiques")
            return
        self.arma_equipada = arma
        if arma not in self.armes:
            self.armes.append(arma)
        print(f"Has equipat {arma.nom}")
    
    def arma_actual(self):
        if self.arma_equipada:
            return f"{self.arma_equipada.nom} (dany: {self.arma_equipada.dany})"
        return "Cap arma equipada"

    def calcular_dany(self):
        if self.arma_equipada is None:
            dany = self.força
        elif self.arma_equipada.magia == 0:
            dany = int(self.força * (1 + self.arma_equipada.dany / 100))
        else:
            dany = int(self.arma_equipada.dany * self.inteligencia / 100)
        return dany
    
    def aplicar_defensa(self, dany):
        return int(dany / 2)
    
    def regenerar_vida(self):
        regeneracio = self.constitucio * 3
        self.vida = min(self.vida_maxima, self.vida + regeneracio)
        return regeneracio
    
    def regenerar_mana(self):
        regeneracio = self.inteligencia * 2
        self.mana = min(self.mana_maxim, self.mana + regeneracio)
        return regeneracio

    def get_nom(self):
        return self.nom
    
    def get_raça(self):
        return self.raça
    
    def get_edat(self):
        return self.edat
    
    def get_força(self):
        return self.força
    
    def get_destresa(self):
        return self.destresa
    
    def get_constitucio(self):
        return self.constitucio
    
    def get_inteligencia(self):
        return self.inteligencia
    
    def get_saviesa(self):
        return self.saviesa
    
    def get_carisma(self):
        return self.carisma
    
    def get_vida(self):
        return self.vida

    def get_vida_maxima(self):
    
        return self.vida_maxima

    def get_mana_maxim(self):
        return self.mana_maxim

    def set_nom(self, nom):
        self.nom = nom

    def set_raça(self, raça):
        self.raça = raça
    
    def set_edat(self,edat):
        self.edat = edat
    
    def set_força(self,força):
        self.força = força
    
    def set_destresa(self,destresa):
        self.destresa = destresa
    
    def set_constitucio(self,constitucio):
        self.constitucio = constitucio
        self.set_vida_maxima()
    
    def set_inteligencia(self,inteligencia):
        self.inteligencia = inteligencia
    
    def set_saviesa(self,saviesa):
        self.saviesa = saviesa
    
    def set_vida_maxima(self):
        self.vida_maxima = self.constitucio * 50
    
    def set_mana_maxim(self):
        self.mana_maxim = self.inteligencia * 30

class Huma(Personatge):
    def __init__(self, nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma):
        super().__init__(nom, "humà", edat, força, destresa, constitucio, inteligencia, saviesa, carisma)
    
    def aplicar_modificadors_racials(self):
        self.força = min(20, self.força + 1)
        self.destresa = min(20, self.destresa + 1)
        self.constitucio = min(20, self.constitucio + 1)
        self.inteligencia = min(20, self.inteligencia + 1)
        self.saviesa = min(20, self.saviesa + 1)
        self.carisma = min(20, self.carisma + 1)
    
    def afegir_habilitats_inicials(self):
        self.habilitats.append(Habilitat("Adaptació", 10, "humà"))

class Elf(Personatge):
    def __init__(self, nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma):
        super().__init__(nom, "elf", edat, força, destresa, constitucio, inteligencia, saviesa, carisma)
    
    def aplicar_modificadors_racials(self):
        self.destresa = min(20, self.destresa + 2)
        self.inteligencia = min(20, self.inteligencia + 2)
    
    def regenerar_mana(self):
        regeneracio = self.inteligencia * 3
        self.mana = min(self.mana_maxim, self.mana + regeneracio)
        return regeneracio
    
    def afegir_habilitats_inicials(self):
        self.habilitats.append(Habilitat("Màgia Arcana", 15, "elf"))

class Orc(Personatge):
    def __init__(self, nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma):
        super().__init__(nom, "orc", edat, força, destresa, constitucio, inteligencia, saviesa, carisma)
    
    def aplicar_modificadors_racials(self):
        self.força = min(20, self.força + 3)
        self.constitucio = min(20, self.constitucio + 1)
    
    def equipar_arma(self, arma):
        if arma.magia > 0:
            print(f"Els orcs no poden equipar armes màgiques!")
            return
        self.arma_equipada = arma
        if arma not in self.armes:
            self.armes.append(arma)
        print(f"Has equipat {arma.nom}")
    
    def calcular_dany(self):
        dany_base = super().calcular_dany()
        dany_final = int(dany_base * 1.10)
        return dany_final
    
    def afegir_habilitats_inicials(self):
        self.habilitats.append(Habilitat("Fúria de Batalla", 20, "orc"))

class Nan(Personatge):
    def __init__(self, nom, edat, força, destresa, constitucio, inteligencia, saviesa, carisma):
        super().__init__(nom, "nan", edat, força, destresa, constitucio, inteligencia, saviesa, carisma)
    
    def aplicar_modificadors_racials(self):
        self.constitucio = min(20, self.constitucio + 4)
        self.destresa = max(5, self.destresa - 1)
    
    def aplicar_defensa(self, dany):
        return int(dany * 0.375)
    
    def regenerar_vida(self):
        regeneracio = self.constitucio * 4
        self.vida = min(self.vida_maxima, self.vida + regeneracio)
        return regeneracio
    
    def afegir_habilitats_inicials(self):
        self.habilitats.append(Habilitat("Resistència de Pedra", 12, "nan"))
     
class arma:
    def __init__(self, nom, tipus, dany, magia):
        self.nom = nom
        self.tipus = tipus
        self.dany = dany
        self.magia = magia

    def get_nom(self):
        return self.nom
    
    def get_tipus(self):
        return self.tipus
    
    def get_dany(self):
        return self.dany
    
    def get_magia(self):
        return self.magia
    
    def set_nom(self, nom):
        self.nom = nom

    def set_tipus(self, tipus):
        self.tipus = tipus

    def set_dany(self, dany):
        self.dany = dany

    def set_magia(self, magia):
        self.magia = magia
    

class Habilitat:
    def __init__(self, nom, cost_mana, tipus):
        self.nom = nom
        self.cost_mana = cost_mana
        self.tipus = tipus
    
    def usar(self, atacant, defensor):
        if self.tipus == "humà":
            cura = int(atacant.constitucio * 2)
            atacant.vida = min(atacant.vida_maxima, atacant.vida + cura)
            return f"{atacant.nom} usa {self.nom} i recupera {cura} de vida!"
        
        elif self.tipus == "elf":
            dany = int(atacant.inteligencia * 1.5)
            defensor.vida -= dany
            if defensor.vida < 0:
                defensor.vida = 0
            return f"{atacant.nom} usa {self.nom} i fa {dany} de dany màgic a {defensor.nom}!"
        
        elif self.tipus == "orc":
            dany = int(atacant.força * 2)
            defensor.vida -= dany
            if defensor.vida < 0:
                defensor.vida = 0
            return f"{atacant.nom} usa {self.nom} i fa {dany} de dany brutal a {defensor.nom}!"
        
        elif self.tipus == "nan":
            defensa_temporal = int(atacant.constitucio * 2)
            return f"{atacant.nom} usa {self.nom} i augmenta temporalment la seva defensa!"
        
        return f"{atacant.nom} usa {self.nom}!"

if __name__ == "__main__":
    j = joc()
    j.executar()

