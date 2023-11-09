class Jelszo:
    jelszo = ""

    def __init__(self, jelszo):
        self.jelszo = jelszo

    def jelszo_bekerese(self):
        pass

    def jelszo_ellenorzese(self):
        pass

    def jelszo_generalasa(self, hossz, nagybetu, kisbetu, szam):
        import string
        import random
        karakterek = ""
        if nagybetu:
            karakterek = karakterek + string.ascii_uppercase
        if kisbetu:
            karakterek = karakterek + string.ascii_lowercase
        if szam:
            karakterek = karakterek + string.digits
        jelszo = ""
        for _ in range(hossz):
            jelszo = jelszo + karakterek[random.randint(0, len(karakterek) - 1)]
        self.jelszo = jelszo
        return

class Felhasznalo(Jelszo):
    email = ""
    def __init__(self, email, jelszo):
        super().__init__(jelszo)
        self.email = email

"""fhsz = Felhasznalo()

fhsz.jelszo
fhsz.email
fhsz.jelszo_generalasa()"""














