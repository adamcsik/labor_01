# Beléptető rendszer
def regisztracio():
    sikeres = True
    felhasznalo_email = felhasznalonev()
    felhasznalo_jelszava = jelszo_bekerese()
    i = 1
    while not jelszo_ellenorzese(felhasznalo_jelszava):
        print("Nem egyezik a két jelszó!")
        i += 1
        if i > 3:
            sikeres = False
            break
    if sikeres:
        with open("jelszo.txt", "a", encoding="utf-8") as fajl:
            fajl.write(felhasznalo_email + ";" + felhasznalo_jelszava + "\n")
    return sikeres

def felhasznalonev():
    felhasznalo_email = input("Kérek egy felhasználói nevet (email): ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem megfelelő az email!!!\nKérek egy felhasználói nevet (email): ")
    return felhasznalo_email

def jelszo_bekerese():
    felhasznalo_jelszava = input("Kérek egy jelszót (1,a,A, min 8 hosszú): ")
    rossz_jelszo = True
    while rossz_jelszo:
        rossz_jelszo = False
        if len(felhasznalo_jelszava) < 8:
            rossz_jelszo = True

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isnumeric():
               van += 1
        if van == 0:
            rossz_jelszo = True

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isupper():
                van += 1
        if van == 0:
            rossz_jelszo = True

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].islower():
                van += 1
        if van == 0:
            rossz_jelszo = True

        if rossz_jelszo == True:
            felhasznalo_jelszava = input("Nem megfelelő a jelszó!!!\nKérek egy jelszót (1,a,A, min 8 hosszú): ")
        else:
            rossz_jelszo = False
    return felhasznalo_jelszava

def jelszo_ellenorzese(felhasznalo_jelszava):
    jelszo2 = input("Kérem ismételje meg a jeszót: ")
    if jelszo2 == felhasznalo_jelszava:
        ok_jelszo = True
    else:
        ok_jelszo = False
    return ok_jelszo

def beleptetes():
    pass


# Innen indul a program
if regisztracio():
    beleptetes()
else:
    print("A sikertelen regisztráció miatt, nem történt beléptetés!")
