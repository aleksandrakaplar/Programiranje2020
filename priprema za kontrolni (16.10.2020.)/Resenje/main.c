#include <stdio.h>
#include <stdlib.h>

// zadatak 1
void definisanjeNiza(int* niz, int brojElemenata) {
    printf("Unesite elemenate niza: \n");
    for(int i = 0; i < brojElemenata; i++) {
        printf("Unesite %d. element niza: ", i+1);
        scanf("%d", niz+i);
    }
}

void nizSimetrican(int* niz, int brojElemenata) {

    int simetrican = 1;

    for(int i = 0; i < brojElemenata; i++) {
        if(*(niz + i) != *(niz + brojElemenata - 1 - i)) {
            simetrican = 0;
            break;
        }
    }
    if(simetrican)
        printf("Niz je simetrican.\n");
    else
        printf("Niz nije simetrican.\n");

}

// zadatak 2

void definisanjeMatrice(int redovi, int kolone, int* matrica) {
    printf("Unesite matricu:\n");
    for(int i = 0; i < redovi; i++) {
        for(int j = 0; j < kolone; j++) {
            printf("Unesite [%d][%d] element: ", i, j);
            scanf("%d", (matrica + i*kolone)+j);
        }
    }
}

void sabiranjePoDijagonali (int redovi, int kolone, int* matrica) {
   int suma = 0;
   for(int i = 0; i < redovi; i++) {
        for(int j = 0; j < kolone; j++) {
            if(i == j) {
                suma = suma + *((matrica + i*kolone)+j);
            }
        }
    }
    printf("Suma elemenata po dijagonali: %d\n", suma);

}

// zadatak 3

void najManjiPozitivanBroj(int* niz, int brojElemenata) {
    int najveci = *(niz);
    for(int i = 0; i < brojElemenata; i++) {
        if(najveci < *(niz + i)) {
            najveci = *(niz + i);
        }

    }
    int najmanji = najveci;

    for(int i = 0; i < brojElemenata; i++) {
        if(najmanji > *(niz + i) && *(niz + i) > 0) {
            najmanji = *(niz + i);
        }

    }

    if(najmanji > 0) {
        printf("Najmanji pozitivni element je: %d", najmanji);
    } else {
        printf("Nema pozitivnih elemenata.");
    }
}
/*
void ispisNiza(int* niz, int brojElemenata) {
    printf("\n");
    for(int i = 0; i < brojElemenata; i++) {
        printf("%d", *(niz + i));
    }
    printf("\n");
}*/

int main()
{

    printf("Zadatak 1:\n");

    int n;
    printf("Unesite broj elemenata niza >>");
    scanf("%d", &n);

    int niz[n];
    definisanjeNiza(niz, n);
    nizSimetrican(niz, n);


    printf("Zadatak 2:\n");

    int redovi, kolone;

    printf("Unesite broj redova >>");
    scanf("%d", &redovi);
    printf("Unesite broj kolona >>");
    scanf("%d", &kolone);

    int matrica[redovi][kolone];
    definisanjeMatrice(redovi, kolone, matrica);
    sabiranjePoDijagonali(redovi, kolone, matrica);

    printf("Zadatak 3:\n");

    //int n;
    printf("Unesite broj elemenata niza >>");
    scanf("%d", &n);

    int b[n];
    definisanjeNiza(b, n);

    najManjiPozitivanBroj(b, n);

    return 0;
}
