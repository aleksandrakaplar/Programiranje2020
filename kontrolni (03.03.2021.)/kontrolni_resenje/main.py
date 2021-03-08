from kontrolni_resenje.paket import Paket
from kontrolni_resenje.posta import Posta


def kreiranje_poste():
    adresa = input("Unesite adresu poste:")
    global posta
    posta = Posta(adresa)


def dodavanje_paketa():
    primaoc = input("Unesite ime, prezime, adresu stanovanja primaoca:")
    posiljaoc = input("Unesite ime, prezime, adresu stanovanja posiljaoc:")
    preporuceno = input("Unesite (Da ili Ne) da li se posiljka salje preporuceno ili ne:")
    if preporuceno == "Da":
        preporuceno = True
    else:
        preporuceno = False
    tezina_paketa = float(input("Unesite tezinu paketa"))

    paket = Paket(primaoc, posiljaoc, preporuceno, tezina_paketa, posta)
    posta + paket

    print("Paket je uspesno ostavljen u posti!")


def paketi_u_posti():
    print(posta)


def paketa_po_broju_paketa(br_paketa, paketi):
    for paket in posta.paketi:
        if paket.broj_paketa == br_paketa:
            return paket
    return None


def uklanjanje_paketa_iz_poste():
    broj_paketa_za_brisanje = input("Unesite broj_paketa koji zelite da uklonite:")
    paket = paketa_po_broju_paketa(broj_paketa_za_brisanje)
    if paket is None:
        print(f"Ne postoji paket sa zadatom vrednost {broj_paketa_za_brisanje}")
        return
    posta - paket
    print(f"Primalac {paket.primaoc} je uspesno primio paket od {paket.posiljaoc}.")


def modifikacija_paketa():
    broj_paketa_za_brisanje = input("Unesite broj_paketa koji zelite da uklonite:")
    paket = paketa_po_broju_paketa(broj_paketa_za_brisanje)
    if paket is None:
        print(f"Ne postoji paket sa zadatom vrednost {broj_paketa_za_brisanje}")
        return
    posta.modifikacija_paketa(paket)


def pretraga_po_atributima():
    atribut = input("Unesite po kom atributu zelite da pretrazite pakete:")
    if atribut not in ["broj_paketa", "primaoc", "posiljaoc"]:
        print("Dozvoljena je pretraga po sledecim kriterijumima: broj_paketa, primaoc i posiljaoc")
        return
    posta.pretraga_paketa_po_atributu(atribut)


def sortiranje_paketa_po_rastuce_poretku():
    nova_lista_paketa = posta.paketi.copy()
    swaps = 1
    while swaps != 0:
        swaps = 0
        for i in range(len(nova_lista_paketa)-1):
            if nova_lista_paketa[i] > nova_lista_paketa[i+1]:
                temp = nova_lista_paketa[i]
                nova_lista_paketa[i] = nova_lista_paketa[i+1]
                nova_lista_paketa[i+1] = temp
                swaps += 1

    for paket in nova_lista_paketa:
        print(paket)


def sortiranje_paketa_po_opadajucem_poretku():
    nova_lista_paketa = posta.paketi.copy()
    swaps = 1
    while swaps != 0:
        swaps = 0
        for i in range(len(nova_lista_paketa) - 1):
            if nova_lista_paketa[i] < nova_lista_paketa[i + 1]:
                temp = nova_lista_paketa[i]
                nova_lista_paketa[i] = nova_lista_paketa[i + 1]
                nova_lista_paketa[i + 1] = temp
                swaps += 1

    for paket in nova_lista_paketa:
        print(paket)


if __name__ == "__main__":
    while True:
        print("1. Kreiranje poste \n"
              "2. Dodavanje paketa u postu \n"
              "3. Izlistavanje svih paketa u posti\n"
              "4. Uklanjanje paketa iz poste\n"
              "5. Modifikacija paketa koji se nalazi u posti \n"
              "6. Pretraga paketa u posti na osnovu zadatog atributa \n"
              "7. Sortiranje paketa u posti po opadajucoj vrednosti tezine paketa\n"
              "8. Sortiranje paketa u posti po rastucoj vrednosti tezine paketa\n"
              "8. Kraj programa")
        opcija = input("Odaberite opciju")

        if opcija == "1":
            kreiranje_poste()
        elif opcija == "2":
            dodavanje_paketa()
        elif opcija == "3":
            paketi_u_posti()
        elif opcija == "4":
            uklanjanje_paketa_iz_poste()
        elif opcija == "5":
            modifikacija_paketa()
        elif opcija == "6":
            pretraga_po_atributima()
        elif opcija == "7":
            sortiranje_paketa_po_opadajucem_poretku()
        elif opcija == "8":
            sortiranje_paketa_po_rastuce_poretku()
        elif opcija == "9":
            print("Kraj programa")
        else:
            print("Izabrali ste opciju koja ne postoji!")
