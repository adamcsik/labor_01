from tkinter import *

def beleptetes_ablak():
    def ok_gomb_feldolgozasa():
        belepes.destroy()
        pass

    def reg_gomb_feldolgozasa():
        belepes.destroy()
        pass

    belepes = Tk()

    belepes.title("Felhasználó beléptetése")

    felh_nev_cimke = Label(belepes, text="A felhasználó neve (email):")
    felh_jelszo_cimke = Label(belepes, text="Jelszó:")

    felh_nev = Entry(belepes, width=30)
    felh_jelszo = Entry(belepes, width=20)

    gomb_ok = Button(belepes, text="OK", command=ok_gomb_feldolgozasa)
    gomb_reg = Button(belepes, text="Regisztráció", command=reg_gomb_feldolgozasa)

    felh_nev_cimke.grid(row=0, column=0, padx=20, pady=20, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, padx=20, sticky=E)
    felh_nev.grid(row=0, column=1, padx=20, sticky=W)
    felh_jelszo.grid(row=1, column=1, padx=20, sticky=W)
    gomb_ok.grid(row=2, column=0, pady=20)
    gomb_reg.grid(row=2, column=1)

    belepes.mainloop()

def regisztracio_ablak():
    def ok_gomb_kezelese():
        regisztracio.destroy()

    regisztracio = Tk()
    regisztracio.title("Regisztráció")

    reg_felh_cimke = Label(regisztracio, text="A felhasználó neve (email):")
    reg_jelszo_cimke = Label(regisztracio, text="Jelszó:")
    reg_jelszo2_cimke = Label(regisztracio, text="Jelszó ismét:")

    reg_felh = Entry(regisztracio, width=30)
    reg_jelszo = Entry(regisztracio,width=20)
    reg_jelszo2 = Entry(regisztracio,width=20)

    gomb_ok = Button(regisztracio, text="OK", command=ok_gomb_kezelese)

    reg_felh_cimke.grid(row=0, column=0)
    reg_jelszo_cimke.grid(row=1, column=0)
    reg_jelszo2_cimke.grid(row=2, column=0)
    reg_felh.grid(row=0, column=1)
    reg_jelszo.grid(row=1, column=1)
    reg_jelszo2.grid(row=2, column=1)
    gomb_ok.grid(row=3, column=0)

    regisztracio.mainloop()

# beleptetes_ablak()
regisztracio_ablak()