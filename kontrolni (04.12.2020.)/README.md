# Kontrolni 

Zadaci trebaju da rade za sve test primere.
Funkcionalnosti moraju da se nalaze u zasebnim funkcijama.
Promenljive i funkcije moraju da imaju nazive koje opisuju šta se tačno nalazi kao vrednost promeniljive tj. šta tačno funkcija izvršava.
Možete da koristite ponuđene vrednosti kao test primere. Podaci se direktno čitaju iz postojećih txt fajlova.

## 1. Zadatak ##

U programskom jeziku Pyhton implementirati program koji služi za analizu pripreme atletičara za maraton. Datoteka sa podacima je data u sledećem formatu:

	ime_atleticara|dan_u_nedelji|predjeno_metara

Sadržaj txt fajla atleticari.txt:

	Marko|Ponedeljak|5400
	Pera|Ponedeljak|11200
	Pera|Utorak|6400
	Nikola|Utorak|12000
	Marko|Sreda|7300
	Pera|Cetvrtak|11300
	Nikola|Cetvrtak|11100
	Marko|Petak|8000

Na početku programa korisnik unosi ime atletičara iz konzole, nakon čega se na ekranu ispisuje:
- Grupa A - dan u nedelji u kome je atletičar prešao najveću udaljenost i ispisuje se pređena udaljenost za taj dan.
- Grupa B - dan u nedelji u kome je atletičar prešao najmanju udaljenost i ispisuje se pređena udaljenost za taj dan.
- Grupa C - ukupan broj pređenih metara u nedelji za unetog atletičara

*Napomena:* Podaci o svim atletičarima se posmatraju u istoj nedelji. Svaki atletičar može da istrči više dana u istoj nedelji. Svaki red u datoteci predstavlja podatak koliko je posmatrani atletičar prešao tog dana.

## 2. Zadatak ##

U Python programskom jeziku implementirati aplikaciju koja služi kao pomoć pri praćenju sportskih aktivnosti. Odnosno koliko brzo sportista pretrči određenu etapu. Datoteka je data u obliku:

	sportista|vreme_u_sekundama|razdaljina_u_metrima
	
Sadržaj txt fajla sportisti.txt:
	
	Marko|15|100
	Pera|18|120
	Nikola|16|130
	Sima|15|200
	Zoran|13|200

Nakon pokretanja programa:
- Grupa D - unosi ime sportiste, nakon čega se na ekranu brzina kretanja sportiste.
- Grupa E - unosi se naredba maksimum, nakon čega se na ekranu ispisuje najbrži sportista (sportista koji ima najveću brzinu kretanja razdaljina_u_metrima/vreme_u_sekundama)
- Grupa F - unosi se naredba minimuim, nakon čega se na ekranu ispisuje najsporiji sportista (sportista koji ima najmanju brzinu kretanja razdaljina_u_metrima/vreme_u_sekundama)

*Napomena:* Jedan sportista može imati jedan zapis u datoteci.
	
## 3. Zadatak ##

Taksi udruženje vodi evidenciju o vožnjama. Informacije se prikupljaju sa tablet računara opremljenog GPS prijemnikom koji se nalazi u svakom vozilu i beleže u datoteku koja se nalazi na serverskom računaru. Svaki red u datoteci predstavlja jednu vožnju. Format reda je:

	<komunalni_broj_vozila>|<vreme_dolaska>|<trajanje_vožnje>|<pređeni_put>

gde je:

	<komunalni_broj_vozila> - jedinstveni identifikator svakog vozila sastavljen od tri do četiri cifre
	<vreme_dolaska> - vreme u minutima od prihvatanja vožnje do dolaska na polaznu adresu
	<trajanje_vožnje> - vreme u minutima od polaska do stizanja na odredište
	<pređeni_put> - put u km koje je vozilo prešlo od početka vožnje do stizanja na cilj

Napisati program u programskom jeziku Python koji učitava datoteku u zadatom obliku, potom:

- Grupa G - korisnik unosi komunalni_broj_vozila i ispisuje prosečno trajanje vožnje traženog vozila (suma svih trajanje_vožnje/ukupan_broj_voznji za dato vozilo)
- Grupa H - na ekranu se ispisuje ukupni pređeni put svakog vozila
- Grupa I - korisnik unosi komunalni_broj_vozila i ispisuje se vrednost najbrže vožnje zadatog vozila (maksimalna vrednost brzine kretanja vozila pređeni_put/trajanje_vožnje)
- Grupa J - korisnik unosi komunalni_broj_vozila i ispisuje se vrednost najsporije vožnje zadatog vozila (minimalna vrednost brzine kretanja vozila pređeni_put/trajanje_vožnje)
- Grupa K - korisnik unosi komandu u konzoli najbrza_vozila i ispisuju se sva vozila koja imaju najbrže vreme dolaska vozila na polazište (minimalna vrednost vreme_dolaska vozila)
- Grupa L - korisnik unosi komandu u konzoli najsporija_vozila i ispisuje se sva vozila koja imaju najsporije vreme dolaska vozila na polazište (maksimalna vrednost vreme_dolaska vozila)

Sadržaj txt fajla voznje.txt:

	5482|3|8|6
	1236|4|10|5
	5482|1|12|6
	3833|6|4|5
	5482|1|22|30
	1236|3|6|4
	1236|6|4|5
	
*Napomena:* Jedno vozilo može imati više zapisa u datoteci.