# Esercizio spese mensili

mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
spese = [820, 760, 910, 700, 680, 1250, 890, 1420, 730, 770, 800, 1100]
budget = 900

print(f"Mesi sopra il budget di {budget}:")
for mese, spesa in zip(mesi, spese):
    if spesa > budget:
        print(f"  {mese}: {spesa}")

totale = sum(spese)
media = totale / len(spese)

print(f"Totale dell'anno: {totale}")
print(f"Media mensile: {media:.2f}")

print("fine")