# Function and Operator Overloading 

Definicija overloading-a u strogo tipiziranim programskim jezicima višeg nivoa jeste definisanje funkcija ili operatora koje se isto zovu, ali se razlikuju po broju parametara tj. redefinisana je implementacija funkcije ili operatora.

# Function Overloading 

[primer01.py](/v7/primeri/primer01.py)

Prilikom definisanja funkcija u Pythonu, funkciji može da se prosledi nijedan ili više parametara. Ovo je koncept overloading-a u Python programskom jeziku.
Imamo dva primera function overloading: overloading built-in (ugrađenih) funkcija i overloading korisnički definisanih funkcija. 

Spisak ugrađenih funkcija [link](https://www.w3schools.com/python/python_ref_functions.asp)

# Operator Overloading

[primer01.py](/v7/primeri/primer01.py)

Overloading operatora omogućava da jedan operator ima više značenja. 
Na primer imamo operator + koji ima funkciju aritmetičkog operatora kada imamo brojeve, možemo da spojimo dve liste, ili da izvršimo konkatenaciju string-ova.

Spisak operatora [link](https://www.w3schools.com/python/python_operators.asp)

# Strukturiranje projekata u Pythonu

Do sada smo imali kratke programe koje smo pisali u jednom fajlu u vidu "skripti". Ove fajlove smo pokretali direktno iz komandne linije: *py naziv_programa.py*

## Moduli (eng. Modules)

[primer02.py](/v7/primeri/primer02.py)

Python modul je fajl sa ekstenzijom .py. Prilikom kreiranja python fajla zadajemo naziv fajlu sa ekstenzijom .py i mora da postoji python kod u ovom fajlu.
Python modul može da bude importovan u druge module ili da se pokreće direktno iz komandne linije.
\_\_name_\_ je specijalna ugradjena varijabla koja evaluira naziv trenutnog modula.
Ako se modul pokreće direktno (iz komandne linije) onda \_\_name_\_ se postavlja na string vrednost "\_\_main\_\_"
Ako je model importovan onda vrednost varijable \_\_name\_\_ je naziv tog modula.

## Paketi (eng. Packages)

[primer03.py](/v7/primeri/primer03.py)

Uz pomoć paketa mi definišemo strukturu Python programa. Paket nam označava folder(direktorijum) u kojem se nalaze slični moduli (python fajlovi). Unutar paketa mogu da se nalaze i podpaketi. Direktorijum mora da ima \_\_init\_\_.py fajl kako bi se smatrao paketom. \_\_init\_\_.py može da se ostavi praznim. 