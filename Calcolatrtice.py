def somma():
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        print(f"{n1} + {n2} = {n1+n2}")

print("Benvenuto nella nostra colacolatrice")
print("Inserisci l'operazione che vuoi effettuare")

while True:
    scelta = int (input(f"1. Sottrazione\n2. Somma\n0. Per uscirte\n"))

    if scelta == 0:
        break

    elif scelta == 1:

        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        print(f"{n1} - {n2} = {n1-n2}")

    elif scelta == 2:
        
    somma()

    else:
        print("Scelta non corretta")

