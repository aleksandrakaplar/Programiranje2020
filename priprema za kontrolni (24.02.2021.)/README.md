## Priprema za kontrolni 24.02.2021. ##

# Zadatak #

Potrebno je kreirati konzolnu aplikaciju koja rukuje sa korpom i voćem. 
Sistem sadrži dve klase:
Klasa Voce je opisana atributima voce_id (jedinstveni identifikator), naziv, tip_voca i korpa u kojoj se voće nalazi. Metode koje sadrži klasa Voce je redefinisana metoda \_\_str_\_\.
Klasa Korpa je opisana atributima korpa_id (jedinstveni identifikator), lista Voća, ukupan broj voća po tipu (tri atributa: broj_jabuka, broj_visanja, broj_malina. Metode koje sadrži klasa Korpa su redefinisane metode \_\_str_\_\, \_\_add_\_ i_\_sub_\_\.

*Napomene:*
Klase se nalaze u odvojenim .py modulima (voce.py i korpa.py). U posebnom modulu main.py kreirati meni i objekte klasa Korpa i Voce.
Relacija između objekata klase Korpa i Voce su: 1 korpa može da ima više voća različitog tipa, a voće može i ne mora da se nalazi u samo jednoj korpi. 
Radi jednostavnosti sistema, programski treba da se kreira samo jedna korpa. Rad sa fajlovima nije neophodan.
Predefinisani tipovi voća su: Jabuka, Visnja, Malina. Ovo ujedno označava tri atributa u klasi korpa.
Nije potrebno implementirati validacije prilikom unosa, brisanja, dodavanja.

Implementirati sledeće funkcionalnosti, koje ujedno predstavljaju stavke menija:
1. Kreiranje korpe. Korpa inicijalno sadrži praznu listu voća.
2. Kreiranje voća. Voće se inicijalno ne nalazi u korpi. Voće se dodaje u list_voca_u_skladistu, ova lista se nalazi u main.py modulu.
3. Ispis voća koji postoje u sistemu (van korpe). Redefinisati \_\_str_\_ metodu u klasi Voce tako da pozivom print(voce) ili str(voce) se izlistaju podaci o voćki. Atribut voce koje se prosleđuje u print i str metodi je objekat tipa klase Voce.
4. Dodavanje postojećeg voća u korpu. Voće se pronalazi iz list_voca_u_skladistu po voce_id (jedinstvenom identifikatoru) potom se dodaje u korpu. Potrebno je redefinisati operator + (\_\_add_\_\) u klasi Korpa, tako da pozivom korpa + voce dodaje se voce u korpu. Voditi računa o ukupnom broju voća u korpi po tipu.
5. Brisanje voća iz korpe. Voće se pronalazi iz liste voce (u Korpi) po jedinstvenom identifikatoru (voce_id). Potrebno je redefinisati operator - (\_\_sub_\_\) u klasi Korpa, tako da pozivom korpa - voce brise se voce iz korpe. Voditi računa o ukupnom broju voća u korpi po tipu.
6. Ispis sadržaja korpe. Potrebno je redefinisati metodu _\_str_\_ u klasi Korpa tako da pozivom print(korpa) ili str(korpa) izlistaju se podaci o voću koje se nalazi u korpi. Atribut korpa koje se prosleđuje u print i str metodi je objekat tipa klase Korpa.
7. Ispis voća po tipu u korpi. Potrebno je definisati metodu ispis_voca_po_tipu u klasi Korpa, tako da se pozivom ove metode ispisuju voća grupisana po tipu i ukupan broj voća svakog tipa koja se nalaze u korpi.

