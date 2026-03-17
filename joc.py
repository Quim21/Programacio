#Quim Perez Joc presa de decisions
print("Et despertes sol enmig d'un bosc fosc. No saps com vas arribar aquí. L'aire és fred i humit. Al teu voltant, els arbres silben amb el vent. Enfront teu hi han dos camins:")

print("A) Prens el camí de l'esquerra, on veus una tènue llum parpellejant.")
print("B) Prens el camí de la dreta, que està cobert de boira espessa.")

opcio:str = str(input("pren una decisió: "))

if opcio == "A":
    print("\nCamines cap a la llum. Al cap d’uns minuts, arribes a una petita cabana amb una llanterna encesa. Sembla abandonada, però la porta està entreoberta.")
    print("A) Entres a la cabana.")
    print("B) Evites la cabana i segueixes pel sender.")
    opcio:str = str(input("pren una decisió: "))
    
    if opcio == "A":
        print("\nA dins hi ha una xemeneia apagada, una taula amb un mapa i una motxilla")
        print("A) Agafes el mapa i la motxilla.")
        print("B) Surts de la cabana sense tocar res.")
        motxilla:str = str(input("pren una decisió: "))

        if motxilla == "A":
            print(f"\n T’equipes amb la motxilla i decideixes sortir, pero escoltes un crit demanant ajuda")
            motxilla == True
        else:
            print("\n surts de la cabana sense tocar res, pero escoltes un crit demanant ajuda")
        
        print("A) Investigar el crit")
        print("B) Ignorar el crit")
        opcio:str = str(input("Pren una decisió: "))
        if opcio == "B" and motxilla:
            
            print("\n El mapa mostra una sortida del bosc a unes 2 hores al nord. La motxilla té aigua, una llanterna i una corda. Segueixes el mapa, evitant trampes i llops.")
            print("Final Fantastic: Escapes del bosc a trenc d’alba. Sobrevius")
        elif opcio == "B":    
            print("\nDecideixes escapar pero no saps on anar")
            print("Final neutre: No surts mai del bosc")
        else:
            print("\nInvestigues el crit pero es una ombra que t’ataca i et mata")
            print("Final dolent: Mors al bosc.")
    else:
        print("\nSegueixes el sender i arribes a un clar amb un pou al centre. Sents veus provinents del pou.")
        print("A) T’assomes al pou.")
        print("B) L’ignores i continues.")
        opcio:str = str(input("Pren una decisió: "))

        if opcio == "A":
            print("\nUna ombra t’arrossega cap a dins. Crides, però ningú et sent.")
            print("Final dolent: Desapareixes en la foscor.")
        else:
            print("\nTrobes una torre de vigilància abandonada. Des de dalt, veus la sortida del bosc. Hi arribes amb esforç.")
            print("Final bo: Escapes i trobes ajuda.")
else:
    print("\nT’endinses en la boira. La visibilitat és molt baixa. Després d’una estona, veus una figura encaputxada dreta al costat d’un arbre.")
    print("A) T’hi acostes.")
    print("B) T’allunyes lentament.")
    opcio:str = str(input("Pren una decisió: "))

    if opcio == "A":
        print("\nLa figura es gira. No té rostre. En tocar-te, tot es torna negre.")
        print("Final Terrorific: Et converteixes en una altra ombra del bosc.")
    else:
        print("\nEnsopegues amb una arrel i caus. En aixecar-te, trobes un antic cartell que apunta cap a una “Sortida”. El segueixes.")
        print("A) Segueixes el cartell.")
        print("B) L’ignores i corres en una altra direcció.")
        opcio:str = str(input("Pren una decisió: "))
        
        if opcio == "A":
            print("\nArribes a un vell pont penjant. En creuar-lo, arribes a una carretera.")
            print("Final bo: Un cotxe et recull. Escapes del bosc.")
        else:
            print("\nEt perds més en la boira. Després d’hores, caus per l’esgotament i el fred.")
            print("Final neutre: No surts mai del bosc.")