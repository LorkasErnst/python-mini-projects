import random
import string

def passwort_generieren():
    try:
        länge = int(input("Passwortlänge: "))
        zeichen = string.ascii_letters + string.digits + string.punctuation
        passwort = "".join(random.choice(zeichen) for _ in range(länge))
        print("Generiertes Passwort:", passwort)
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")

if __name__ == "__main__":
    passwort_generieren()