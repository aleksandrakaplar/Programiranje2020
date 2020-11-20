# zadatak 01
def akronim():
    s = input("Unesite recenicu: ")
    s = s.title()
    splitovano = s.split()
    akr = ""
    for i in splitovano:
        akr = akr + i[0]
    print(akr)


# zadatak 02
def ponavljanje():
    first = input("Unesite prvi string: ")
    second = input("Unesite drugi string: ")
    print(first[:3] * 2 + second[-3:])


# zadatak 03
def registrovanje_korisnika():
    while True:
        username = input("Unesite korisnicko ime: ")
        password = input("Unestie lozinka: ")

        with open("korisnici.txt", "a") as f:
            f.write(username + "|" + password + "\n")

        print("=========================== RESTART")
        kraj = input("Kraj? (y/n)")
        if kraj == "y":
            break


# zadatak 04
def ucitavanje_korisnika():
    with open("korisnici.txt", "r") as f:
        for linija in f.readlines():
            delovi = linija.split("|")
            ime = delovi[0]
            # rstrip ako se ne prosledi parametar po defaultu uklanja se razmak
            prezime = delovi[1].rstrip()

            print("Korisnicko ime:", ime)
            print("Prezime: ", prezime)
            print()


if __name__ == '__main__':
    akronim()
    ponavljanje()
    registrovanje_korisnika()
    ucitavanje_korisnika()
