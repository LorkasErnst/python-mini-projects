# Kalenderanzeige
import calendar

def kalender():
    try:
        jahr = int(input("Jahr eingeben: "))
        monat = int(input("Monat eingeben (1-12): "))
        print(calendar.month(jahr, monat))
    except ValueError:
        print("Bitte eine gültige Jahreszahl und Monatsnummer eingeben.")

if __name__ == "__main__":
    kalender()
