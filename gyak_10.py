import sqlite3

kapcsolat = None
ab = None

def ab_letrehozas():
    global kapcsolat, ab
    kapcsolat = sqlite3.connect("dolgozok.db")
    ab = kapcsolat.cursor()
    ab.execute('CREATE TABLE IF NOT EXISTS dolgozok (email TEXT, jelszo TEXT)')

def ab_regisztracio(email, jelszo):
    global kapcsolat, ab
    ab.execute('INSERT INTO dolgozok VALUES (?, ?)', (email, jelszo))
    kapcsolat.commit()

def ab_jelszokereses(email):
    jelszo = ""
    ab.execute('SELECT * FROM dolgozok')
    dolgozok = ab.fetchall()
    for dolgozo in dolgozok:
        if dolgozo[0] == email:
            jelszo = dolgozo[1]
    return jelszo

def ab_lezaras():
    if kapcsolat and ab:
        ab.close()
        kapcsolat.close()