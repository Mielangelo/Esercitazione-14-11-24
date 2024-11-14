#CALCOLARE IL PERIMETRO DELLE FIGURE (quadrato, cerchio, rettangolo)

def quadrato(lato):                                                                   # Perimetro Quadrato = lato * 4
    return 4 * lato  

def cerchio(raggio):                                                                  # perimetro (circonferenza) del cerchio = 2 * P greco * raggio
    pi = 3.14
    return 2 * pi * raggio

def rettangolo(lunghezza, larghezza):                                                 # perimetro rettangolo = 2 * (lunghezza + larghezza)
    return 2 * (lunghezza + larghezza)

print("Calcolo del perimetro di una figura geometrica: ")  
print("1. Quadrato ⬜")
print("2. Cerchio ⚪")
print("3. Rettangolo █")

scelta = input("Scegli una figura (1/2/3): ")                                          # Richiesta di scelta all'utente

if scelta == "1":
        lato = float(input("Inseriaci la lunghezza del lato del quadrato: "))
        print("✅ Il perimetro del quadrato è ✅:", quadrato(lato))                    # Risultato 1
elif scelta == "2":
        raggio = float(input("Inserisci il raggio del cerchio: "))
        print("✅ Il perimetro (circonferenza) del cerchio è ✅: ", cerchio(raggio))   # Risultato 2
elif scelta == "3":
        lunghezza = float(input("Inserisci la lunghezza del rettangolo: "))
        larghezza = float(input("Inserisci la larghezza del rettangolo: "))
        print("✅ Il perimetro del rettangolo è ✅:", rettangolo(lunghezza, larghezza)) # Risultato 3
else:
        print("❌ Scelta non valida. Riprova ❌")                                       # Risultato 4
