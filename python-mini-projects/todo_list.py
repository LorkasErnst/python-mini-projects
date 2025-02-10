# Einfache To-Do-Liste

def todo_liste():
    aufgaben = []
    while True:
        print("\n1: Aufgabe hinzufügen  2: Aufgabe entfernen  3: Liste anzeigen  4: Beenden")
        auswahl = input("Auswahl: ")
        
        if auswahl == "1":
            aufgabe = input("Neue Aufgabe: ")
            aufgaben.append(aufgabe)
        elif auswahl == "2":
            try:
                index = int(input("Aufgabennummer zum Entfernen: ")) - 1
                if 0 <= index < len(aufgaben):
                    aufgaben.pop(index)
                else:
                    print("Ungültige Nummer.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")
        elif auswahl == "3":
            print("\nTo-Do Liste:")
            for i, aufgabe in enumerate(aufgaben, 1):
                print(f"{i}. {aufgabe}")
        elif auswahl == "4":
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    todo_liste()