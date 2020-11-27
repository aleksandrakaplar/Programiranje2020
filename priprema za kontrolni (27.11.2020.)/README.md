# Priprema za kontrolni zadatak

Zadaci trebaju da rade za sve test primere.
Funkcionalnosti moraju da se nalaze u zasebnim funkcijama. (Npr. ucitaj_knjige_u_recnik(), pretraga_po_autoru(), broj_reackija(), ...)
Promenljive, funkcije moraju da imaju nazive koje opisuju šta se tačno nalazi kao vrednost promeniljive tj. šta tačno funkcija izvršava.
Samo za prvi zadatak je neophodno upisati podatke u rečnik potom izvršiti pretragu, za drugi i treći zadatak podaci se ne upisuju u rečnik.

## 1. Zadatak 

U biblioteci su podaci o knjigama sačuvani u sledećem formatu:

Svaka knjiga je opisana sa šifrom, autorom, naslovom i godinom izdanja. Podaci su razdovojeni delimiterom |. 
Knjige učitati u rečnik pre pretrage. Ključ je šifra knjige, vrednost je string ostalih podataka razdvojeni delimiterom |. 
*Napomena*: Knjiga ima samo jednog autora. Jedinstven identifikator svake knjige je šifra knjige. Više knjiga mogu da imaju istog autora, isti naslov i da budu iste godine izdane.

Primer fajla sa podacima o knjigama je:
		
	1|Jane Austen|Pride and Prejudice|1813
	2|Daniel Defoe|Robinson Crusoe|1719
	3|J. K. Rowling|Fantastic Beasts and Where to Find Them|2001
	4|J. K. Rowling|Harry Potter and the Philosopher's Stone|1997
	
Primer rečnika:
	
	{
		"1": "Jane Austen|Pride and Prejudice|1813", 
		"2": "Daniel Defoe|Robinson Crusoe|1719", 
		"3": "J. K. Rowling|Fantastic Beasts and Where to Find Them|2001", 
		"4": "J. K. Rowling|Harry Potter and the Philosopher's Stone|1997"
	}
ili 

	{
		"1": ["Jane Austen", "Pride and Prejudice", "1813\n"], 
		"2": ["Daniel Defoe", "Robinson Crusoe", "1719\n"], 
		"3": ["J. K. Rowling", "Fantastic Beasts and Where to Find Them", "2001\n"], 
		"4": ["J. K. Rowling" ,"Harry Potter and the Philosopher's Stone", "1997\n"]
	}
Napisati Python program koji pronalazi sve knjige za zadatog autora.
	Primer:
	
	Find books by author >>> J. K. Rowling	
	J. K. Rowling|Fantastic Beasts and Where to Find Them|2001 
	J. K. Rowling|Harry Potter and the Philosopher's Stone|1997
	
	Find books by author >>> Leo Tolstoy
	There are no books by this author.
	
	Find books by author >>> Jane Austen	
	Jane Austen|Pride and Prejudice|1813
	
## 2. Zadatak 

U programskom jeziku Python implementirati program koji služi za analizu aktivnosti korisnika na društvenim mrežama. Datoteka sa podacima je data u sledećem formatu:

	korisničko_ime|broj_komentara|broj_reakcija 

Primer fajla sa podacima: 

	Marko|15|100
	Pera|18|120
	Pera|13|120
	Nikola|16|130
	Pera|13|120
	Marko|112|13
	
Na početku programa korisnik unosi korisničko ime nakon čega se na ekranu ispisuje ukupan broj reakcija korisnika.

*Napomena*: Jedan korisnik može imati više zapisa u datoteci.

Primer:

	Return number of reactions for user >>> Marko 
	Total number of reactions >>> 113
	
	Return number of reactions for user >>> Laza 
	Total number of reactions >>> 0
	
	Return number of reactions for user >>> Nikola 
	Total number of reactions >>> 130
	
## 3. Zadatak 

U programskom jeziku Pyhton implementirati program koji služi za pronalaženje letova dužih od zadate vrednosti. Datoteka sa podacima o letovima je data u sledećem formatu:

	Beograd|Vasington|7623
	Helsinki|Beograd|2308
	Abu Dabi|Beograd|3779
	Beograd|Cikago|8033

Na početku programa korisnik unosi minimalnu razdaljinu nakon čega se na ekranu ispisuju svi letovi duži od toga jedan za drugim.

Primer: 

	Minimal flight distance >>> 5000
	Flights
	Beograd|Vasington|7623
	Beograd|Cikago|8033
	
	Minimal flight distance >>> 9000
	Flights
	No flights