## Objektno orijentisano programiranje ##

Do sada smo radili proceduralno programiranje. Program se izvršavao sekvencijalno (linija po liniju). 
Objektno orijentisano programiranje (oop) nam omogućava da definišemo strukturu programa tako da svojstva i ponašanja grupišemo na nivou jednog objekta. 
Objekat je osnovni pojam u OOP uz pomoć koga prikazujemo podatke u programu i pored toga definišemo strukturu programa.

Osnovni principi objektnog orijentisanog programiranja (OOP):
1. Enkapsulacija
2. Apstrakcija
3. Nasleđivanje 
4. Polimorfizam

### Objekti i klase ###

Uz pomoć klasa mi opisujemo objekte. Klasu posmatramo kao "blueprint" po kojem kreiramo objekat. Objekat je instanca klase. Program prilikom izvršavanja radi sa objektima. Klasa je apstrakcija da predstavimo koje podatke skladištimo i koje operacije izvršavamo nad objektima određenog tipa.

Na slici 1 uz pomoć UML (Unified Modeling Langauge) dijagrama smo prikazali 4 klase: patka, jezero, papagaj, kavez. Linije između objekata posmatramo kao veze. Trenutno posmatrana veza je asocijacija. 
Na slici 2 je dat detaljniji opis veze između 4 klase. Konkretno u ovom primeru veza glasi: više pataka živi u jednom jezeru, više papagaja žive u jednom kavezu. 

![slika1](/slike/v4/slika1.png)

Slika 1.

![slika2](/slike/v4/slika2.png)

Slika 2.

Klase opsujemo atributima (svojstvima) i metodama (akcijama).
Atributi su podaci kojima opisujemo klasu. Klasa može da bude opisana sa više atributa. Na slici 3 naš primer je proširen i svaka klasa ima svoje zasebne atribute. 
Dodatno možemo da prikažemo tipove ovih podataka slika 4.


![slika3](/slike/v4/slika3.png)

Slika 3.


![slika4](/slike/v4/slika4.png)

Slika 4.

Akcije koje mogu da budu izvršene na određenoj klasi objekta su metode. Metode su kao funkcije u proceduralnom programiranju. Metode imaju pristup atributima koji su definisani u istoj klasi. Kao i funkcije, metode imaju parametre i povratne vrednosti. Možemo da definišemo više akcija u jednoj klasi.
Slika 5 prikazuje klase sa metodama. 


![slika5](/slike/v4/slika5.png)

Slika 5.
