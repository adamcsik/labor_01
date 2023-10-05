# Beléptető rendszer
def regisztracio():
    sikeres = True
    felhasznalonev()
    jelszo_bekerese()
    i = 1
    while not jelszo_ellenorzese():
        print("Nem egyezik a két jelszó!")
        i += 1
        if i > 3:
            sikeres = False
            break
    return sikeres

def felhasznalonev():
    felhasznalo_email = input("Kérek egy felhasználói nevet (email): ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem megfelelő az email!!!\nKérek egy felhasználói nevet (email): ")

def jelszo_bekerese():
    felhasznalo_jelszava = input("Kérek egy jelszót (1,a,A, min 8 hosszú): ")
    ok_jelszo = True
    while ok_jelszo:
        if len(felhasznalo_jelszava) < 8:
            ok_jelszo = False
        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isnumeric():
               van +=1
        if van == 0:
            ok_jelszo =False
        if ok_jelszo == False:
            felhasznalo_jelszava = input("Nem megfelelő a jelszó!!!\nKérek egy jelszót (1,a,A, min 8 hosszú): ")
        else:
            ok_jelszo = False


def jelszo_ellenorzese():
    pass
    ok_jelszo = True
    return ok_jelszo
def beleptetes():
    pass


# Innen indul a program
felhasznalo_email = ""
felhasznalo_jelszava = ""
jelszo_bekerese()
if regisztracio():
    beleptetes()
else:
    print("A sikertelen regisztráció miatt, nem történt beléptetés!")
