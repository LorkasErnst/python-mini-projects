# Meine kleine virtuelle Kaffeemaschine

def kaffeekochen():
    zutaten = {"Wasser": 500, "Milch": 300, "Kaffee": 100}
    menü = {"Espresso": {"Wasser": 50, "Kaffee": 20},
            "Cappuccino": {"Wasser": 50, "Milch": 50, "Kaffee": 20},
            "Latte": {"Wasser": 50, "Milch": 100, "Kaffee": 20}}
    
    while True:
        print("Verfügbare Getränke:", ", ".join(menü.keys()))
        auswahl = input("Was möchtest du trinken? (oder 'exit' zum Beenden): ")
        if auswahl.lower() == "exit":
            break
        
        if auswahl in menü:
            rezept = menü[auswahl]
            if all(zutaten[z] >= rezept.get(z, 0) for z in zutaten):
                for zutat in rezept:
                    zutaten[zutat] -= rezept[zutat]
                print(f"Hier ist dein {auswahl}!")
            else:
                print("Nicht genug Zutaten. Bitte nachfüllen!")
        else:
            print("Getränk nicht verfügbar.")

if __name__ == "__main__":
    kaffeekochen()