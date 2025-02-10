# Einfacher Taschenrechner

def rechner():
    print("Willkommen zum Taschenrechner!")
    while True:
        try:
            zahl1 = float(input("Erste Zahl: "))
            op = input("Operator (+, -, *, /): ")
            zahl2 = float(input("Zweite Zahl: "))
            if op == "+":
                print("Ergebnis:", zahl1 + zahl2)
            elif op == "-":
                print("Ergebnis:", zahl1 - zahl2)
            elif op == "*":
                print("Ergebnis:", zahl1 * zahl2)
            elif op == "/":
                if zahl2 == 0:
                    print("Fehler: Division durch Null!")
                else:
                    print("Ergebnis:", zahl1 / zahl2)
            else:
                print("Ungültiger Operator.")
        except ValueError:
            print("Bitte gültige Zahlen eingeben.")

if __name__ == "__main__":
    rechner()