def main():
    ukoly = []  # sem se budou ukládat úkoly ve formátu {"nazev": "...", "popis": "..."}

    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ")
        print()  # prázdný řádek pro lepší čitelnost

        if volba == "1":
            # Přidání nového úkolu
            nazev = input("Zadejte název úkolu: ")
            popis = input("Zadejte popis úkolu: ")
            ukoly.append({"nazev": nazev, "popis": popis})
            print(f"Úkol '{nazev}' byl přidán.")
            print()

        elif volba == "2":
            # Zobrazení všech úkolů
            if ukoly:
                print("Seznam úkolů:")
                for i, ukol in enumerate(ukoly, start=1):
                    print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
            else:
                print("Žádné úkoly zatím nejsou.")
            print()

        elif volba == "3":
            # Odstranění úkolu
            if ukoly:
                print("Seznam úkolů:")
                for i, ukol in enumerate(ukoly, start=1):
                    print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
                cislo = input("Zadejte číslo úkolu, který chcete odstranit: ")

                if cislo.isdigit():
                    cislo = int(cislo)
                    if 1 <= cislo <= len(ukoly):
                        smazany_ukol = ukoly.pop(cislo - 1)
                        print(f"Úkol '{smazany_ukol['nazev']}' byl odstraněn.")
                    else:
                        print("Neplatné číslo úkolu.")
                else:
                    print("Neplatná volba.")
            else:
                print("Žádné úkoly k odstranění.")
            print()

        elif volba == "4":
            print("Konec programu.")
            break

        else:
            print("Neplatná volba, zkuste to znovu.\n")


if __name__ == "__main__":
    main()
