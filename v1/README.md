# Instalacija i podešavanje okruženja #

## Instalacija Python 

**Python3** možete skinuti sa sledećeg [link](https://www.python.org/downloads/)-a 
U zavisnosti od operativnog sistema odabraćete odgovarajuću **Python 3.9.0** verziju. Postoje dve verzije **Python** (**Python 2** i **Python 3**). Na ovom predmetu mi ćemo da koristimo najnoviju verziju **Python 3**. **Python 2** je stara verzija Python-a i više ne postoji podrška za ovu verziju. Ne postoji velika razlika između ovih verzija. Postoji manja razlika u sintaksi.

## Instalacija okruženja

Na ovom predmetu čemo koristiti **PyCharm** IDE (Integration Development Enviorment). IDE je softverska aplikacija uz pomoć koje možemo da razvijamo aplikacije u raznim programskim jezicima. 
PyCharm možete da skinete sa sledećeg [link](https://www.jetbrains.com/pycharm/download/#section=windows)-a. Postoje dve verzije. PyCharm Professional je plaćena verzija koju možete da skinete i da se registrujete uz pomoć vaših školskih email adresa. PyCharm Community je besplatna verzija. Bilo koja verzija PyCharm-a je u redu da se instalira za potrebe ovog predmeta.

Alternative: Notepad++, Jupyter Notebook

# Uvod 

Program je sekvenca naredbi koje govore računaru šta treba da uradi. Uz pomoć programskog jezika mi možemo računaru da zadajemo ove naredbe. Naredbe se pišu po sintaksi i sematici odabranog programskog jezika npr. c = a + b. Ali ova naredba mora da se prevede iz jezika visokog nivoa u mašinski jezik. Ovo može da se postigne na dva načina: *kompajlerom* ili *interpreterom*. Kompajler je program koji izvorni kod (pisan u programskom jeziku visokog nivoa) prevodi u mašinski kod koji se dalje izvršava (Slika 1.). Interpreter je program koji simulira kompjuter koji razume programske jezike visokog nivoa. Ne prevodi se izvorni kod u mašinski. (Slika 2.)
Python je programski jezik visokog nivoa koji koristi interpreter prilikom pokretanja programa. Program se izvršava linija po linija.

![compiling](/slike/compiling.png)

Slika 1. Kompajliranje jezika visokog nivoa Slika je preuzeta iz [knige](https://iran-lms.com/images/images/Books/PDF/Python-Programming_-An-Introduction-to-Computer-Science-Franklin-Beedle--Associates-2016---John-M.-Zelle.pdf).

![interpreting](/slike/interpreting.png)

Slika 2. Interpretiranje jezika visokog nivoa. Slika je preuzeta iz [knige](https://iran-lms.com/images/images/Books/PDF/Python-Programming_-An-Introduction-to-Computer-Science-Franklin-Beedle--Associates-2016---John-M.-Zelle.pdf).

U ovoj lekciji pokazaćemo:
#### Primer01 ####
1. Kako da se ispiše tekst u konzoli 
2. Deklarisanje varijable
3. Kako korisnik može da unese vrednosti iz konzole
4. Rad sa stringovima
5. Aritmetičke operacije 
6. Operacije poređenja
7. Logičke operatore 
8. Bit operatori
9. Primer kalkulatora
#### Primer02 ####
1. if - else naredba 
2. while petlja
3. for petlja 
#### Primer03 ####
1. liste
2. torke
#### Primer04 ####
1. Definisanje metoda


# Zadaci #
1. Implementirati konzolnu aplikaciju koja nudi korisniku sledeće opcije 
	1. Ispis svih elemenata u listi
	2. Unos novog elementa u listu 
	3. Modifikacija/Izmena postojećeg elementa u listi (korisnik prosledi naziv elementa koji želi da izmeni)
	4. Brisanje postojećeg elementa iz liste (korisnik prosledi naziv elementa koji želi da obriše)
	
Prepušteno je vama da birate podatke koji će se nalaziti u listi. Npr. list životinja, boja, škola, itd.
Lista treba samo da sadrži jedinstvene nazive. (boja: ["crvena", "plava", "zelena"])).
Prilikom pokretanja programa zadati inicijalne vrednosti liste.
	

# Domaći #

1. Implementirati program koji na osnovu zadatog broja meseca vraća broj dana u tom mesecu. (Napomena: ne treba da računate prestupnu godinu za februar: rešenje za februar(2. mesec) je 28, 29)
2. Implementirati program koji na osnovu zadate sekunde u danu (0 - 86400) prikazuje vreme u formatu hh:mm:ss, hh-sat, mm-minut, ss-sekund.
3. Izračunati faktorijel proizvoljno zadatog prirodnog broja. (Napomena: ideja nije da koristite ugrađenu funkciju math.factorial(). Vaše rešenje možete uporediti sa rešenjem koje dobijete pozivom ugrađene funkcije.)
Napomena za domaći: Validaciju prilikom unosa ne morate implementirati. Npr. ako se traži od korisnika broj, uneće se broj. 

#### Napomena: ####
Primeri sa časa se nalaze u folderu primeri, rešenje domaćih zadatak se nalazi u folderu domaći-rešenje.
