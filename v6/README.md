# Osnovni koncept OOP 

- Enkapsulacija
- Apstrakcija 
- Nasleđivanje :heavy_check_mark:
- Polimorfizam :heavy_check_mark:

## Nasleđivanje (eng. Inheritance)

[primer01.py](/v6/primeri/primer01.py)

Nasleđivanje predstavlja vezu eng. *"is-a"*. Ovim označavamo da klasa može da nasledi osobine druge klase. Prednost nasleđivanja je ponovno iskorišćavanje koda i važi tranzitivnost.
Pojmovi koji se najčešće koriste da opišu dve klase u ovakvoj vezi su nadklasa(roditeljska klasa) i podklasa. Klasa čija polja se nasleđuju je roditeljska klasa, klasa koja će ova polja da nasledi je poklasa. 
Moguće je naslediti samo polja i metode koja su public ili protected. Privatna polja i metode nije moguće naslediti.
Python podržava jednostruko, nasleđivanje u više nivoa, hibridno nasleđivanje, hijerarhijsko nasleđivanje i višestruko nasleđivanje. 

[primer02.py](/v6/primeri/primer02.py)

U Python-u nadklasa (osnovna klasa) svih klasa je object klasa. Object klasa ima svoja ugrađena svojstva i metode, koje sve ostale klase nasleđuju. 

## Polimorfizam (eng. Polymorphism)

[primer01.py](/v6/primeri/primer01.py)

Polimorfizam nam omogućava da definišemo metodu u podklasi (child class) koja će imati isto ime kao i metoda u nadklasi (parent class). Nasleđivanje nam omogućava da podklasa nasledi sva svojstva i metode nadklase. Nasleđene metode u podklasama možemo da  redefinišemo. Proces ponovne implementacije nasleđene metode podklase se naziva eng. *method overriding*.

## Zadatak za domaći

1. Kreirati klasu Smestaj koji od atributa ima naziv, adresu i grad. Od funkcija treba da se redefiniše (override) metoda __str__ koja će da vraća vrednosti prethodno pomenutih atributa.  Kreirati klasu Hotel koja nasleđuje klasu Smeštaj. Pored nasleđenih atributa iz klase Smeštaj, klasa Hotel treba da ima atribut broj zvezdica hotela. Hotel redefiniše metodu __str__ gde treba da se prikažu svi podaci vezani za Hotel (uključujući i nasleđene podatke iz Smeštaja).
Omogućiti kreiranje Smeštaja tj. kreiranje Hotela, ispis svih kreiranih Hotela.
