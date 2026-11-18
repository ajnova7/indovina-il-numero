"""Gioco: indovina il numero."""

import random


def gioca():
    numero_segreto = random.randint(1, 100)
    tentativi = 0

    print("Ho pensato un numero tra 1 e 100. Prova a indovinarlo!")

    while True:
        risposta = input("Il tuo tentativo: ")
        if not risposta.isdigit():
            print("Inserisci un numero intero valido.")
            continue

        tentativo = int(risposta)
        tentativi += 1

        if tentativo < numero_segreto:
            print("Troppo basso!")
        elif tentativo > numero_segreto:
            print("Troppo alto!")
        else:
            print(f"Bravo! Hai indovinato {numero_segreto} in {tentativi} tentativi.")
            break


if __name__ == "__main__":
    gioca()
