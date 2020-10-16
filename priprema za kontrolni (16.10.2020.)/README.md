## Priprema za kontrolni 16.10.2020. ##

# Zadaci #

## Zadatak 1 ##

Napisati program koji određuje da li je celobrojni niz simetričan. Niz zadaje korisnik iz konzole. Potrebno je učitati broj elemenata i elemente niza.
Napomena: Validacija prilikom unosa nije neophodno implementirati. Koristiti pokazivače za pristup elementima niza. 
#### Primer: 
	
	a = [ 1 2 3 4 ]
	nizSimetrican(a, n) // Niz a nije simetričan
	
	b = [ 1 2 2 1 ]
	nizSimetrican(b, n) // Niz b je simetričan
	
	c = [ 1 2 5 2 1 ]
	nizSimetrican(c, n) // Niz c je simetričan

## Zadatak 2 ##

Napisati program koji sabira sve elemente na dijagonali kvadratne matrice. Matricu zadaje korisnik iz konzole. Potrebno je učitati dimenziju i elemente matrice.
Napomena: Validacija prilikom unosa nije neophodno implementirati. Koristiti pokazivače za pristup elementima niza. 
#### Primer: 
	
	A = [ 1 2 3
	      4 5 6
	      7 8 9 ]
		  
	sumPoDijagonali(redovi, kolone, A) // Suma elemenata po dijagonali: 15

## Zadatak 3 ##

Napisati program koji pronalazi najmanji pozitivan element u nizu celih brojeva. Ako ne postoji nijedan pozitivan element u niz ispisati tekst "Nema pozitivnih elemenata". Niz zadaje korisnik iz konzole. Potrebno je učitati broj elemenata i elemente niza.
Napomena: Validacija prilikom unosa nije neophodno implementirati. Koristiti pokazivače za pristup elementima niza. 
#### Primer: 
	
	a = [1 4 2 -10 -11]
	najManjiPozitivanBroj(a, n) // Najmanji pozitivan element niza je 1.

	b = [-1 -4 -2 -10 -11 0]
	najManjiPozitivanBroj(b, n) // Nema pozitivnih elemenata.
