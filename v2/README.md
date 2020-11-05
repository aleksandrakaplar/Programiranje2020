## Rad sa fajlovima 

Prilikom pokretanja programa sve što se izvršava u programu se privremeno čuva u RAM memoriji. Ova memorija se delocira prilikom zaustavljanja programa i/ili gašenja računara. Podatke trajno čuvamo uz pomoć fajlova. Fajlovi su imenovane lokacije koje se nalaze na hard disku i koristimo ih da skladištimo informacije. Fajlovi mogu da sadrže bilo koji tip podataka. 

Fajl možemo da posmatramo kao višelinijski string koji se nalazi na disku. Specijalni karakter '\n' se koristi da se označi kraj svake linije u fajlu.

Fajl mora prvo da se otvori kako bismo mogli da čitamo/pišemo podatke iz/u fajl. Kada završimo sa čitanjem/pisanjem neophodno je da zatvorimo fajl. Nakon zatvaranja fajla svi resursi koji su bili vezani za fajl su oslodođeni. 

Napomena: Ponekad izmene koje načinimo unutar fajl objekta u programu neće biti vidljiva unutar fizičkog fajla na disku sve dok ne zatvorimo fajl programski.

Redosled izvršavanja operacije prilikom rada sa fajlom:

1. Otvaranje fajla 
2. Čitanje/Pisanje iz/u fajl
3. Zatvaranje fajla

## Rad sa skupom 

Skup je ugrađen tipa podatka u Pythonu. Skup je neuređena kolecija koja ne sadrži duplikate. Uz pomoć skupova možete da proverite postojanje elementa u skupu i da otklonite duplikate. Skupovi podržavaju matematičke operacije kao što je unija, presek, razlika i simetrična razlika.

## Rad sa rečnikom 

Rečnik je ugrađen tip podatka u Pythonu. Rečnik je kolekcija koja je neuređena, promenljiva i indeksirana. Rečnik se navodi sa vitičastim zagradama i imaju  parove ključ-vrednost. 

### Primer01 ###
1. Čitanje i pisanje sadržaja txt fajla
2. Čitanje i pisanje sadržaja binarnog fajla

### Primer02 ###
1. Rad sa skupom

### Primer03 
1. Rad sa rečnikom  

# Zadaci 
1. Napisati program koji kao rezultat vraća broj ponavljanja karaktera u fajlu. Karakter se unosi iz konzole.
2. Napisati program koji čuva listu podataka u fajl. Podaci su odvojeni sa delimiterom.
3. Napisati zadatak koji iščitava podatke iz prethodnog zadatka i upisuje ih u listu.
4. Omogućiti perzistenciju (čuvanje) podataka u tekstualnu datoteku. Proširiti zadatak 1 iz prethodne nedelje tako da se lista elemenata iščitava iz fajla, nakon svih operacija (dodavanje, modifikacija, brisanje) izmene se čuvaju u fajl.

# Domaci 

1. Napiši program koji formira akronim za zadatu frazu. Akronim se sastoji od kapitalizovanih prvih slova reči u frazi. Na primer RAM je akronim za frazu „random access memory“. 

        Primer izvršavanja programa:
        unesite frazu: random access memory
        akronim za unetu frazu je: RAM

2. Napisati program koji od korisnika traži da unese dva stringa i formira novi string koji se sastoji od dva puta ponovljena prva tri karaktera iz prvog stringa i poslednja tri karaktera prethodnog stringa.

		Primer izvršavanja programa:
		
		unesite prvi string: abcdef
		unesite drugi string: ghijkl 
		abcabcjkl

3. Napisati program za registrovanje korisnika. Program treba da omogući korisniku da unese korisničko ime i lozinku. Informacije o korisniku čuvaju se u tekstualnom fajlu.

		Primer izvršavanja programa:
		korisnicko ime: pera
		lozinka: peric 
		>>> =========================== RESTART
		korisnicko ime: jova
		lozinka: jovic
		
		Fajl korisnici.txt treba da sadrži sledeće podatke:
		
		pera|peric 
		jova|jovic
		steva|stevic
		
4. Napisati program koji učitava iz tekstualnog fajla korisnička i mena i ispisuje ih. Za fajl korisnici.txt iz prethodnog zadatka nakon uzvršavanja programa treba da bude prikazano:
		
		korisnicko ime: pera
		lozinka: peric
		
		korisnicko ime: jova
		lozinka: jovic

