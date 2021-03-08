import random as rnd


class Posta:

    def __init__(self, adresa):
        self.id_poste = rnd.randint(1, 10000)
        self.adresa = adresa
        self.paketi = []

    def __str__(self):
        result = f"Posta se nalazi na adresi {self.adresa}\n" \
                 f"Lista paketa je"
        for paket in self.paketi:
            result += str(paket)

        return result

    def __add__(self, other):
        self.paketi.append(other)

    def __sub__(self, other):
        self.paketi.remove(other)

    def indeks_paketa(self, broj_paketa):
        for i in range(len(self.paketi - 1)):
            if self.paketi[i].broj_paketa == broj_paketa:
                return i

        return -1

    def modifikacija_paketa(self, paket):
        nov_primaoc = input("Unesite novog primaoca paketa").strip()
        nov_posiljaoc = input("Unesite novog primaoca paketa").strip()

        result = "Izmenjeni atributi: "

        if nov_primaoc:
            paket.primaoc = nov_primaoc
            result += "primaoc "
        if nov_posiljaoc:
           paket.posiljaoc = nov_posiljaoc
           result += "posiljaoc "

        index_paketa = self.indeks_paketa(paket.broj_paketa)
        self.paketi[index_paketa] = paket

        print(result)

    def pretraga_paketa_po_atributu(self, naziv_atributa_paketa):
        postoji = False
        pretraga = input("Unesite vrednost za pretraga:")
        if naziv_atributa_paketa == "broj_paketa":
            for paket in self.paketi:
                if pretraga in paket.broj_paketa:
                    postoji = True
                    print(paket)
        elif naziv_atributa_paketa == "primaoc":
            for paket in self.paketi:
                if pretraga in paket.broj_paketa:
                    postoji = True
                    print(paket)
        elif naziv_atributa_paketa == "posiljaoc":
            for paket in self.paketi:
                if pretraga in paket.broj_paketa:
                    postoji = True
                    print(paket)

        if not postoji:
            print(f"Ne postoji ni jedan paket sa zadatom vrednost: {pretraga}")