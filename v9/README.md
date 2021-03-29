# Crtanje 

## Pokretanje slike  

Primer: [MovingImages](/v9/MovingImages)

Pokretna slika se sastoji iz više slika eng. frames. Više slika prikazanih u sekvenci daju nam iluziju animacije, tj. objekti na slici deluju da se kreću. 
Prilikom prikaza animacije u jednoj iteraciji while petlje mi prikazujemo jedan frame. 
<br /> 
Dobra praksa je da svaki oblik koji treba da se prikaže na canvasu bude definisan u zasebnoj metodi. Razlog za ovo je preglednost koda i olakšano održavanje koda. Ako iz nekog razlog prozor u kojem su oblici bili prikazi treba da promeni veličinu, lakše je oblike skalirati u novi prozor ako je svaki predmet u posebnoj funkciji.  
<br />
Prilikom definisanja kretanja predmeta voditi računa da se svi oblici od kojih se posmatrani predmet sastoji isto moraju pomerati. 
<br />
Na kretanje utičemo tako što menjamo koordinate tj. parametre koji opisuju oblik.
Npr. Pravougaonik:

- menjamo koordinate x i y:
	- x - osa predmet se pomera levo (ukoliko umanjujemo vrednost x), i desno (ukoliko povećavamo vrednost x)
	- y - osa predmet se pomera gore (ukoliko umanjujemo vrednost y), i na dole (ukoliko povećavamo vrednost y)
	- width, height - možemo da utičemo na veličinu pravougaonika 

Prilikom kretanja predmeta može da se desi da je potrebno da vodimo računa da predmet ostane u dimenzijama prozora u kojem predmet prikazujemo. Da predmet ostane u granicama prozora treba da se poštuju restrikcije:
- duž x - ose: x_predmeta > x_min i x_predmeta < x_max, gde su x_min = 0 i x_max maksimalna širina prozora 
- duž y - ose: y_predmeta > y_min i y_predmeta < y_max, gde su y_min = 0 i y_max maksimalna visina prozora 

Prilikom kretanja predmeta može da se desi da dođe do sudara (kolizije) dva ili više predmeta. Imamo nekoliko slučajeva za razmatranje (pretpostavka je da su predmeti pravougaonog oblika):
- Ukoliko jedan predmet miruje a drugi se kreće
	- U zavisnosti gde se nalaze oba predmeta imamo:
		- predmet koji stoji je sa leve strane kanvasa, predmet koji se kreće je sa desne strane kanvasa (predmeti se kreću po x-osi): x_pred_krece > x_pred_miruje + širina_pred_miruje
		- predmet koji stoji je sa desne strane kanvasa, predmet koji se kreće je sa leve strane kanvasa (predmeti se kreću po x-osi): x_pred_krece + širina_pred_krece < x_pred_miruje 
		- itd.
- Ukoliko se oba kreću po x-osi ista je provera

Slične su provere ukoliko se predmet kreće po y-osi. Kombinacija ove dve provere mora da se implementira ukoliko se predmet kreće dijagonalno. 
<br />
Provera se vrši u svakom frame-u!	

### Clock 

Pozivom clock = pygame.time.Clock() kreiramo klasu koja predstavlja sat uz pomoć kojeg možemo da pratimo vreme u našoj igri. Koristi se za definisanje frame-ova koji se prikazuju u sekundi (fps). Prosečan čovek može da vidi 30 frame-ova u sekundi.
<br />
Metoda clock.tick(framerate=0) definiše na kraju beskonačne petlje tj. na kraju svakog frame-a. Izračunaće koliko je milisekundi prošlo od prethodnog poziva. Ukoliko prosledimo opcioni argument framerate (brzina frejmova), funkcija se odlaže kako bi igra usporila za zadati broj tikova u sekundi.

## Zadatak za vežbu 

1. Proširiti primer MovingImages tako da brod plovi do stene i kada udari u stenu potone. Slika 1.
2. Proširiti primer tako da se i oblak kreće. Slika 2.

<br />

![slika1](/slike/v9/boat_collision.gif)

Slika 1.

![slika2](/slike/v9/boat_collision_with_cloud.gif)

Slika 2.