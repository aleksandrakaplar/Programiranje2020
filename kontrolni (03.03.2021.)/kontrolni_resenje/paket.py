import random as rnd


class Paket:

    def __init__(self, primaoc, posiljaoc, preporuceno, tezina_paketa, posta):
        self.broj_paketa = rnd.randint(1, 1000)
        self.primaoc = primaoc
        self.posiljaoc = posiljaoc
        self.preporuceno = preporuceno
        self.tezina_paketa = tezina_paketa
        self.posta = posta

    def __str__(self):
        result = f"Paket salje {self.posiljaoc}, a paket prima {self.primaoc}.\n" \
                 f"Tezina paketa je {self.tezina_paketa}.\n" \
                 f"Paket se salje preporuceno? {self.preporuceno}.\n" \
                 f"Paket se nalazi u posti.\n"
        return result

    def __lt__(self, other):
        if self.tezina_paketa < other.tezina_paketa:
            return True
        return False

    def __gt__(self, other):
        if self.tezina_paketa > other.tezina_paketa:
            return True
        return False
