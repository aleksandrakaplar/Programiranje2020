# Kontrolni 03.03.2021.
*Napomene:*
Validacije prilikom kreiranja objekata nije neophodno implementirati.
Rad sa fajlovima takođe nije neophodno implementirati.
Sistem rukuje samo sa jednom poštom.
Prilikom završetka kontrolnog potrebno je sva tri fajla zipovati u jedan folder pod nazivom ime_prezime_grupa.zip (ime i prezime učenika koji je radio zadatak, i grupa koja vam je dodeljena za kontrolni zadatak)

Implementirati sistem koji vodi evidenciju o poštanskim pošiljkama u pošti.
Sistem je opisan uz pomoć dve klase. Svaka klasa treba da se nalazi u zasebnom modulu (posta.py i paket.py): 
1. Posta 
	atributi su:
		- id_poste (jedinstven identifikator)
		- adresa (ulica, broj, mesto)
		- paketi (lista objekta klase Paket)
		
	metode:
		- redefinisana metoda \_\_str_\_()
		- redefinisan operator + (   \_\_add_\_()    )
		
	#### Grupa 1
	- redefinisan operator - (  \_\_sub\_\_()    )
	#### Grupa 2
	- modifikacija_paketa(broj_paketa)
	#### Grupa 3
	- pretraga_paketa_po_atributu(naziv_atributa_paketa)
		
2. Paket
	atributi su:
		- broj_paketa
		- primaoc (ime, prezime, ulica, broj i mesto stanovanja) - string
		- posiljalac (ime, prezime, ulica, broj i mesto stanovanja)- string
		- preporuceno (boolean)
		- tezina_paketa
		- posta (posta u kojoj se nalazi paket)
	metode:
		- redefinisana metoda: \_\_str_\_()
	#### Grupa 4
	- redefinisana metoda - (  \_\_gt\_\_()   )
	#### Grupa 5
	- redefinisana metoda - (  _\_lt\_\_()   )
		
Implementirati sledeće funkcionalnosti u vidu stavke menija. Meni se nalazi u zasebnom modulu pod nazivom main.py: 

1. Kreiranje pošte 
2. Dodavanje paketa u poštu
Pozivom naredbe: posta + paket, paket treba da se doda u poštu. Paket se dodaje u listu paketi koja se nalazi u klasi Posta.
Prilikom dodavanja paket u poštu, paket se i ujedno kreira.
3. Izlistavanje svih paketa u pošti
Pozivom print(posta) treba da se izlistaju svi paketi koji se nalaze u listi paketi u objektu klase Posta. 
Neophodno je redefinisati metode \_\_str_\_() u klasama Posta i Paket tako da se ispišu vrednosti svih atributa koji nisu jedinstveni identifikatori.
\_\_str_\_() metoda jednom kada se redefiniše treba vraća string, i ne poziva se ekspilicitno posta.\_\_str_\_() ili paket.\_\_str_\_(). Poziva se implicitno npr. print(posta), print(paket), str(posta), str(paket).

Sledeće funkcionalnosti variraju u zavisnosti od grupe koja vam je dodeljenja za kontrolni zadatak:
		
## Grupa 1

4. Uklanjanje paketa iz pošte
Pozivom naredbe: posta - paket, paket treba da se ukloni iz pošte. 
Paket koji želite da uklonite tražite po broj_paketa jedinstvenom identifikatoru.
Implementirati validaciju prilikom unosa broj_paketa, ako ne postoji paket sa zadatom vrednošću broj_paketa ispisati poruku: "Ne postoji paket sa zadatom vrednost {zadata_vred_br_paketa}" u suprotnom ukloniti paket i ispisati poruku: "Primalac {primalac_paketa} je uspesno primio paket od {posiljalac_paketa}."
Vrednosti koje se nalaže unutar vitičastih zagrada su vrednosti atributa objekta klase Paket, tj. podaci o paketu koji se uspešno poslao.

## Grupa 2 

5. Modifikacija paketa koji se nalazi u posti 
Pozivom naredbe posta.modifikuj_paket(broj_paketa) prosleđuje se broj_paketa (jedinstveni identifikator) paketa koji želimo da izmenimo. 
Nije neophodno implementirati validaciju prilikom unosa vrednosti broj_paketa. Omogućiti korisniku da menja samo podatke o primaocu i/ili posiljaocu. Nije neophodno implementirati validaciju prilikom unosa vrednosti svih atributa. Omogućiti korisniku da preskoči unos nove vrednosti za određeni atribut. Nakon uspešne izmene ispisati koji su se svi podaci promenili, npr. ako su se menjale vrednosti za primaoca i posiljaoca ispis će biti: "Izmenjeni su atributi: primaoc posiljalac " ili ako se samo promenila vrednost primaoca: "Izmenjeni su atributi: primaoc". Izmenjen paket treba da se nalazi u list paketi u objektu klase Posta.

## Grupa 3 

6. Pretraga paketa u posti na osnovu zadatog atributa
Potrebno je dozvoliti pretragu samo po atributima:
- broj_paketa
- primaoc
- posiljaoc
Implementirati validaciju prilikom unosa naziv_atributa_paketa, ako se unese nedovoljena vrednost ispiše se poruka: "Dozvoljena je pretraga po sledecim kriterijumima: broj_paketa, primaoc i posiljaoc"

Pozivom naredbe posta.pretraga_paketa_po_atributu(naziv_atributa_paketa) prosleđuje se naziv atributa po kojem se pretraga vrši. Nije neophodno implementirati višestruku pretragu (pretragu po više kriterijuma). Na osnovu zadate vrednosti naziv_atributa_paketa pretraživaće se lista paketi koja se nalazi u objektu klase Posta. 

Npr. korisnik odabere da vrši pretragu po broj_paketa, potom mora da unese vrednost po kojoj će se paketi pretražiti. Svi paketi koji *sadrže* (ne strogo jednako) zadatu vrednost treba da se izlistaju. Ako ne postoji paket sa zadatom vrednošću ispisaće se "Ne postoji ni jedan paket sa zadatom vrednost: {zadatak_vred}".

## Grupa 4 

7. Sortiranje paketa u pošti po rastućoj vrednosti težine paketa
Potrebno je redefinisati metodu greater than (  _\_gt\_\_()  )
Poziv paket1 > paket2 poziva se metoda _\_gt\_\_() gde je nephodno implementirati logiku kada je paket1 veći od paket2 tj.
	if self.tezina > paket.tezina:
		return True
	return False

paket1 > paket2 prvi operand paket1 je self parametar, drugi operand je drugi parametar (po defaultu se zove other)
Logiku za sortiranje smo pokazali u primeru bubble_sort.py.

Ako ne postoji trenutno ni jedan paket u posti ispisati poruku: "Trenutno nema paketa u posti!"

## Grupa 5 

7. Sortiranje paketa u pošti po opadajućoj vrednosti težine paketa
Potrebno je redefinisati metodu less than (  _\_lt\_\_()  )
Poziv paket1 < paket2 poziva se metoda _\_lt\_\_() gde je nephodno implementirati logiku kada je paket1 veći od paket2 tj.
	if self.tezina < paket.tezina:
		return True
	return False

paket1 > paket2 prvi operand paket1 je self parametar, drugi operand je drugi parametar (po defaultu se zove other)
Logiku za sortiranje smo pokazali u primeru bubble_sort.py.

Ako ne postoji trenutno ni jedan paket u posti ispisati poruku: "Trenutno nema paketa u posti!"
