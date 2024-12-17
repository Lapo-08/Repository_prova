import Calcolatrtice as clc

while True:
    scelta = int (input(f"1. Sottrazione\n2. Somma\n0. Per uscirte\n"))

    if scelta == 0:
        break

    elif scelta == 1:
        clc.sottrazione()
        
    elif scelta == 2:    
        clc.somma()
    else:
        print("Scelta non corretta")
