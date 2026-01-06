import os
from google import genai

variable_name = "GEMINI_API_KEY"
api_key_value = os.getenv(variable_name)


if not api_key_value:
    print("Error: No s'ha trobat la clau GEMINI_API_KEY a les variables d'entorn.")
    print("Tanca el programa i revisa la configuració de la clau.")
    exit(1)

client = genai.Client(api_key=api_key_value)

MODEL_NAME = "gemini-2.5-flash"

ROL_SISTEMA = (
    "Ets una eina que només genera llistes de Python amb dades de prova. "
    "Sempre has de respondre únicament amb una llista d'una sola dimensió "
    "en format Python vàlid, sense cap text extra."
)

sets_de_dades = []


def llegir_enter(missatge="Introdueix un valor: "):
    while True:
        try:
            return int(input(missatge))
        except ValueError:
            print("Has d'introduir un número enter.")


def menu():
    while True:
        print("------------------------------")
        print("  Generador de Sets de Dades")
        print("------------------------------")
        print("1. Generar un nou set de dades")
        print("2. Visualitzar un o tots els sets de dades")
        print("3. Esborrar un o tots els sets de dades")
        print("4. Sortir")

        opcio_menu = llegir_enter("Tria una opció: ")

        if opcio_menu == 1:
            crear_nou_set()
        elif opcio_menu == 2:
            menu_visualitzar()
        elif opcio_menu == 3:
            menu_esborrar()
        elif opcio_menu == 4:
            print("Tancant el programa. Fins aviat!")
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")


def construir_prompt():
    print("------------------------------")
    print("    Generació d’un nou set   ")
    print("------------------------------")

    nom_set = input("Introdueix un nom per al set de dades: ")

    print("Quin tipus de dada vols que sigui?")
    print("1 - Enters")
    print("2 - Decimals")
    print("3 - Text")
    tipus_opcio = llegir_enter("Tipus de dada: ")

    if tipus_opcio == 1:
        tipus = "números enters"
    elif tipus_opcio == 2:
        tipus = "números decimals"
    else:
        tipus = "text"

    quantitat = llegir_enter("Quants elements vols? ")

    descripcio = input("Quines dades necessites que et generi?\n> ")

    instruccio = (
        ROL_SISTEMA
        + " "
        + f"Genera exactament {quantitat} elements que siguin {tipus}. "
        + f"Les dades han d'estar relacionades amb: {descripcio}. "
        + "Recorda, respon nomes amb una llista de Python d'una dimensió, "
        + "per exemple: [1, 2, 3] o [\"gos\", \"gat\"]. No afegeixis cap explicació."
    )

    return nom_set, instruccio


def generar_llista_amb_gemini(prompt: str):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
    except Exception as e:
        print("Error de connexió o de clau amb l'API:", e)
        return None

    try:
        text = response.text.strip()
    except Exception:
        print("La resposta de la IA no conté text.")
        return None

    print("Resposta de la IA:", text)

    try:
        data = eval(text)
        if not isinstance(data, list):
            raise ValueError("La resposta no és una llista.")
        return data
    except Exception as e:
        print("Error interpretant la llista:", e)
        return None


def crear_nou_set():
    nom_set, prompt = construir_prompt()

    print("\nGenerant dades... si us plau, espera.\n")
    values = generar_llista_amb_gemini(prompt)

    if values is None:
        print("No s'ha pogut crear el set perquè la llista no és vàlida.")
        return

    nou_set = {"name": nom_set, "values": values}
    sets_de_dades.append(nou_set)

    print(f'Set "{nom_set}" guardat correctament!')
    print(f"Dades: {values}")
    print(f"Nombre d'elements: {len(values)}\n")


def menu_visualitzar():
    if not sets_de_dades:
        print("No hi ha sets guardats.")
        return

    print("------------------------------")
    print("  Visualitzar Sets de Dades")
    print("------------------------------")
    print("1 - Visualitzar un set concret")
    print("2 - Visualitzar tots els sets")

    opcio = llegir_enter("Opció: ")

    if opcio == 1:
        visualitzar_un_set()
    elif opcio == 2:
        visualitzar_tots_els_sets()
    else:
        print("Opció no vàlida.")


def visualitzar_tots_els_sets():
    if not sets_de_dades:
        print("No hi ha sets guardats.")
        return

    print("\nSets guardats:")
    for s in sets_de_dades:
        print(f"- {s['name']}: {s['values']} ({len(s['values'])} elements)")
    print()


def visualitzar_un_set():
    if not sets_de_dades:
        print("No hi ha sets guardats.")
        return

    print("\nSets disponibles:")
    for s in sets_de_dades:
        print(f"- {s['name']}")

    nom = input("Quin vols visualitzar? ")
    trobat = False
    for s in sets_de_dades:
        if s["name"] == nom:
            print(f"\nSet: {s['name']}")
            print(f"Dades: {s['values']}")
            print(f"Nombre d'elements: {len(s['values'])}\n")
            trobat = True
            break

    if not trobat:
        print("No s'ha trobat cap set amb aquest nom.\n")


def menu_esborrar():
    if not sets_de_dades:
        print("No hi ha sets guardats per esborrar.")
        return

    print("------------------------------")
    print("  Esborrar Sets de Dades")
    print("------------------------------")
    print("1 - Esborrar un set concret")
    print("2 - Esborrar tots els sets")

    opcio = llegir_enter("Opció: ")

    if opcio == 1:
        esborrar_un_set()
    elif opcio == 2:
        esborrar_tots_els_sets()
    else:
        print("Opció no vàlida.")


def esborrar_un_set():
    if not sets_de_dades:
        print("No hi ha sets guardats.")
        return

    print("\nSets disponibles:")
    for s in sets_de_dades:
        print(f"- {s['name']}")

    nom = input("Quin vols esborrar? ")
    for i, s in enumerate(sets_de_dades):
        if s["name"] == nom:
            del sets_de_dades[i]
            print(f'Set "{nom}" esborrat correctament.\n')
            return

    print("No s'ha trobat cap set amb aquest nom.\n")


def esborrar_tots_els_sets():
    sets_de_dades.clear()
    print("Tots els sets han estat esborrats.\n")


if __name__ == "__main__":
    menu()
