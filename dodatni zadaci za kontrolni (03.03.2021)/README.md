# Dodatni zadaci za kontrolni od 03.03.2021.

*Napomene:*
Validacije prilikom kreiranja objekata nije neophodno implementirati.
Rad sa fajlovima nije neophodno implementirati.
Sistem rukuje samo sa jednom bibliotekom.
Prilikom završetka kontrolnog potrebno je sva 4 fajla zipovati u jedan folder pod nazivom ime_prezime.zip (ime i prezime učenika koji je radio zadatak)

Implementirati sistem koji vodi evidenciju o knjigama u biblioteci.
Sistem je opisan uz pomoć dve klase. Svaka klasa treba da se nalazi u zasebnom modulu (biblioteka.py adresa.py i knjiga.py): 
1. Adresa <br />
	atributi su:
	- naziv_ulica 
	- broj_ulice 
	- grad 
	- drzava 
	<br />
	metode:

	- redefinisana metoda \_\_str_\_()
	
2. Biblioteka <br />
	atributi su:
	- id_biblioteke (jedinstven identifikator)
	- adresa (Adresa)
	- knjige (lista objekta klase Knjiga, knjige koje su kreirane u biblioteci, razdužene i zadužene)

	<br />	
	metode:
	
	- redefinisana metoda \_\_str_\_()
	- dodaj_novu_knjigu(knjiga)
	- redefinisan operator - (  \_\_sub\_\_()    )
	- redefinisan operator + (   \_\_add_\_()    )
	
		
3. Knjiga
	atributi su:
	- id_knjige (jedinstven identifikator)
	- podaci_o_knjizi (ime, prezime autora, naslov knjige) - string
	- clan_koji_je_zaduzio_knjigu (ime, prezime)- string
	- zaduzena (boolean)	
	<br />
	metode:
	
	- redefinisana metoda: \_\_str_\_()
	- zaduzivanje()
	- razduzivanje()
	
		
Implementirati sledeće funkcionalnosti u vidu stavke menija. Meni se nalazi u zasebnom modulu pod nazivom main.py: 

1. Kreiranje biblioteke  - prilikom kreiranje bibilioteke kreira se i adresa gde se bibilioteka nalazi
2. Izlistavanje svih knjiga u bibilioteci.
Pozivom print(biblioteka) treba da se izlistaju sve knjige koji se nalaze u listi knjige u objektu klase Biblioteka. Razdvojiti razdužene i zadužene knjige. 
Neophodno je redefinisati metode \_\_str_\_() u klasama Biblioteka, Adresa i Knjiga tako da se ispišu vrednosti svih atributa koji nisu jedinstveni identifikatori.
\_\_str_\_() metoda jednom kada se redefiniše treba vraća string, i ne poziva se ekspilicitno biblioteka.\_\_str_\_() ili knjiga.\_\_str_\_(). Poziva se implicitno npr. print(biblioteka), print(knjiga), print(adresa), str(biblioteka), str(knjiga), str(adresa).
3. Dodavanje nove knjige u biblioteku
Pozivom naredbe: dodaj_novu_knjigu(knjiga), nova knjiga treba da se doda u bibioteku. Knjiga se dodaje u listu knjiga koja se nalazi u klasi Biblioteka.
Prilikom dodavanja knjige u biblioteku, knjiga se i ujedno kreira. Knjiga prilikom kreiranja je inicijalno razduzena (polje zaduzena je False).
4. Zaduzi knjigu <br />
Pozivom naredbe: biblioteka - knjiga, knjiga koja se nalazi u biblioteci treba da zaduzi. Neophodno je uneti podatke id_knjige (koju želimo da zadužimo) i nakon toga treba uneti ko zadužuje knjigu pozivom knjiga.zaduzi(), gde se popunjavaju polja clan_koji_je_zaduzio_knjigu i zaduzena = True. 
Neophodno je implementirati proveru da li je knjiga već zadužena, ako jeste ne sme se dozovliti zaduživanje knjige. 
5. Razduzi knjigu <br />
Pozivom naredbe: biblioteka + knjiga, knjiga treba da se razduži. Neophodno je uneti podatke id_knjige koju želimo da razdužimo i nakon toga se poziva knjiga.razduzena(), gde se briše polje clan_koji_je_zaduzio_knjigu = None i zaduzena=False. 
Neophodno je implementirati proveru da li je knjiga zadužena, ako nije ne sme se dozovliti razduživanje knjige. 
