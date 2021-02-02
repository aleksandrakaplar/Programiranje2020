# Osnovni koncept OOP 

- Enkapsulacija :heavy_check_mark:
- Apstrakcija  :heavy_check_mark:
- Nasleđivanje
- Polimorfizam

## Sakrivanje podataka

Prilikom modelovanja objekata mi definišemo javni (eng. public) prikaz (eng. interface) objekta. Interface se sastoji iz kolekcije atributa i metoda uz pomoć kojih objekti jedne klase mogu da vrše interakciju sa objektom druge klase. Objekti jedne klasa najčešće neće imati pristup svim metodama od objekta druge klase.

Primer iz svako-dnevnog života može da bude računar. Mi uz pomoć tastature i miša zadajemo komande računaru (otvaranje određenih folder-a, aplikacija, paljenje/gašenje računara). Nisu nam bitne informacije npr. šta se dešava ispod haube računara. 

U OOP možemo da ograničimo pristup metodama i atributima. Ovo sprečava da modifikujem podatke na način na koji ne bismo smeli.

### Enkapsulacija (Encapsulation) 

[primer01.py](/v5/primeri/primer01.py)

Enkapsulacija je koncept spajanja relevantnih atributa (promenljivih) i metoda koje rade sa tim atributima na jedno mesto (klasa/objekat). 

#### Privatne metode i atributi 

Zbog principa sakrivanje podataka (eng. information hinding principle), odnosno želje da sprečimo modifikaciju atributa na nevalidan način, trebamo da ograničimo pristup atributima i metodama klasa. Za to se koriste modifikatori pristupa (public, private, protected). U Pythonu, private atributi i metode počinju sa dve donje crte (__), protected sa jednom donjom crtom (_). 
Na slici 1 smo definisali klasu Papagaj koja pored prethodno spomenutih atributa i metoda ima privatnu metodu __generisi_serijski_broj() i privatni atribut __serijski_broj. 
Metoda __generisi_serijski_broj() ne može direktno da se pozove preko objekta koji je tip klase Papagaj. Privatne metode mogu da se pozovu samo unutar same klase. 
Atribut __serijski_broj je privatni atribut koji može da bude izmenjen samo unutar metode klase. 
Ako biste želeli da omogućite izmenu privatnog atributa to može uz pomoć setter metode. 

![slika1](/slike/v5/slika1.png)
Slika 1.

### Apstrakcija (Abstraction) 

[primer02.py](/v5/primeri/primer02.py)

Apstrakcija je proces izvlačenje javnih interface-a od implementacionih detalja. Korisnik zna šta može da radi, ali ne zna kako to radi. 

Na slici 2 smo definisali klasu Papagaj i Kavez. Papagaj ima novu metodu leti. Papagaj vodi računa o spavanju i letenju. Kavez ima novu metodu uleti_u_kavez(papagaj).
Na ovaj način objekat papagaj nema veze sa metodama koje se nalaze u objektu kavez. 

![slika2](/slike/v5/slika2.png)
Slika 2.

### Asocijacija kompozicija i agregacija (Composition and Aggregation)

[primer03.py](/v5/primeri/primer03.py)

#### Asocijacija (has-a)

Asocijacija prestavlja vezu između objekata različitih tipova klasa. Uz pomoć ovakvih veza objekat jedne klase može da izvršava metode objekta iz druge klase. Kompozicija i agregacija su specijalni oblici asocijacije. (Slika 3.)

![slika3](/slike/v5/slika3.png)
Slika 3.

Asocijacija je slaba veza između dva ili više objekata različitih tipova klasa. Objekti su nezavisni jedni od drugih. 
Primer takve veze može da bude primer papagaja i kaveza, ali sa jednom izmenom. U kavezu može da živi više papagaja. Dok jedan papagaj može da živi u jednom ili nijednom kavezu. (Slika 4.) Novi primer predstavlja papagaja koji može da živi i van kaveza (nazavisno od kaveza). Kavez postoji nezavisno od papagaja u oba slučajeva.

![slika4](/slike/v5/slika4.png)
Slika 4.

Asocijacije mogu da budu predstavljena preko UML dijagrama u vidu usmerenih strelica koje mogu da opisuju veze jedan na prema jedan (eng. one-to-one), jedan na prema više (eng. one-to-many) ili više na prema više (eng. many-to-many). Ovo su mogući kardinaliteti koje možemo da zadajemo vezama između objekata.
Primer sa papagajom i kavezom je veza one-to-many. 

#### Agregacija (Aggregation)

Agregacija je specijalni oblik asocijacije gde objekti ražličitih tipova klasa nezavise jedni od drugih. Primer [primer02.py](../primeri/primer02.py), Papagaj i kavez. Uz pomoć UML dijagrama veza agregacije je prestavljena kao otvoren dijamant. Dijamant pokazuje na kontajnter klasu. (Slika 5.)

![slika5](/slike/v5/slika5.png)
Slika 5.

#### Kompozicija (Composition) 

Kompozicija označava da su objekti dve ili više različitih klasa zavisni jedan od drugog. Primer, Papagaj i Jaje. Jaje ne može da nastane bez Papagaja. Ako Papagaj ne postoji, nema ni jajeta. Uz pomoć UML dijagrama veza kompozicija je prestavljena kao zatvoreni dijamant. Dijamant pokazuje na kontajnter klasu. (Slika 6.)

![slika6](/slike/v5/slika6.png)
Slika 6.


