import random

# Spielbrett drucken
def zeige_spielfeld(spielfeld):
    for reihe in spielfeld:
        print(" | ".join(reihe))
    print("-" * 9)

# Prüft, ob ein Spieler gewonnen hat
def gewinner_prüfen(spielfeld):
    for reihe in spielfeld:
        if reihe[0] == reihe[1] == reihe[2] and reihe[0] != " ":
            return reihe[0]
    
    for spalte in range(3):
        if spielfeld[0][spalte] == spielfeld[1][spalte] == spielfeld[2][spalte] and spielfeld[0][spalte] != " ":
            return spielfeld[0][spalte]

    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] and spielfeld[0][0] != " ":
        return spielfeld[0][0]
    if spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] and spielfeld[0][2] != " ":
        return spielfeld[0][2]

    return None

# Minimax-KI optimieren
def minimax(spielfeld, tiefe, maximiert):
    ergebnis = gewinner_prüfen(spielfeld)
    if ergebnis == "O":
        return 1
    elif ergebnis == "X":
        return -1
    elif all(spielfeld[r][c] != " " for r in range(3) for c in range(3)):
        return 0

    if maximiert:
        bester_wert = -float("inf")
        for r in range(3):
            for c in range(3):
                if spielfeld[r][c] == " ":
                    spielfeld[r][c] = "O"
                    wert = minimax(spielfeld, tiefe + 1, False)
                    spielfeld[r][c] = " "
                    bester_wert = max(bester_wert, wert)
        return bester_wert
    else:
        bester_wert = float("inf")
        for r in range(3):
            for c in range(3):
                if spielfeld[r][c] == " ":
                    spielfeld[r][c] = "X"
                    wert = minimax(spielfeld, tiefe + 1, True)
                    spielfeld[r][c] = " "
                    bester_wert = min(bester_wert, wert)
        return bester_wert

# Spiel starten
def tictactoe():
    print("Willkommen zu meinem Tic-Tac-Toe!")
    spielfeld = [[" " for _ in range(3)] for _ in range(3)]
    spieler = "X"

    while True:
        zeige_spielfeld(spielfeld)

        if spieler == "O":
            print("Die KI ist dran...")
            zug = (random.randint(0, 2), random.randint(0, 2))
            print(f"KI wählt: {zug[0] + 1}, {zug[1] + 1}")
        else:
            zug = input(f"Spieler {spieler}, gib deinen Zug ein (Zeile Spalte): ").split()
            zug = (int(zug[0]) - 1, int(zug[1]) - 1)

        if spielfeld[zug[0]][zug[1]] == " ":
            spielfeld[zug[0]][zug[1]] = spieler
        else:
            print("Das Feld ist schon belegt! Versuch es nochmal.")
            continue

        gewinner = gewinner_prüfen(spielfeld)
        if gewinner:
            zeige_spielfeld(spielfeld)
            print(f"Spieler {gewinner} gewinnt! ")
            break

        spieler = "O" if spieler == "X" else "X"

if __name__ == "__main__":
    tictactoe()
