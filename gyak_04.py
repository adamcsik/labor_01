# számológép
def adatkeres(tipus):
    valasz = ""
    if tipus == "sz":
        valasz = input("Kérem az első számot: ")
        while not valasz.isnumeric():
            print("Rossz érték!!!!")
            valasz= input("Kérem az első számot: ")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Milyen művelet legyen (+,-,*,/): ")
        while valasz not in ["+", "-", "*", "/"]:
            print("Nem jó a műveleti jel!!!")
            valasz = input("Milyen művelet legyen (+,-,*,/): ")
    return valasz
def szamolas():
    eredmeny = 0
    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    elif muvelet == "/":
        eredmeny = szam1 / szam2
    return eredmeny

# programindítás
print("Számológép")
szam1 = adatkeres("sz")
muvelet = adatkeres("m")
szam2 = adatkeres("sz")
eredmenye = szamolas()

print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("_".rjust(50, "_"))
print(str(eredmenye).rjust(50))
