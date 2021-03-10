# Pygame 

Omogućava kreiranje grafičkih igrica, ali ne 3D igrica. 
Kreiraćemo klijentsku aplikaciju koju ćemo moći kasnije pokretati i na drugim računarima.

# Uvod 

## Crtanje na canvasu 

### RGB (Red-Green-Blue)

Boje se definišu kao lista (RBG) tri boja: crvena, zelena, plava. 
Svaki element RGB liste je broj u rasponu od 0 do 255. Ovaj broj označava prisutnost određene boje gde 0 znači odsutnost boje, a 255 da je dosta te boje prisutno. Kombinacija ovih tri boji dobijamo ostale boje. 
Način definisanje boje: BOJA = [R, G, B]

Na primer:
CRNA = [0, 0, 0]
BELA = [255, 255, 255]
CRVENA = [255, 0, 0]
ZELENA = [0, 255, 0]
BLUE = [0, 0, 255]

Na sledećem [linku](https://htmlcolorcodes.com/color-picker/) postoji eng. color-picker koji generiše RGB torku u zavisnosti od odabrane boje sa grafičkog prikaza.

### Koordinate 

U pygame uvek se prosleđuju pozicije kao (X, Y) koordinate (Slika 1.). Početna koordinata (0, 0) se nalazi u gornjem levom uglu.

![slika1](/slike/v8/slika01.png)

Slika 1.

### Oblici 

PyGame podržava razne oblike.
Klasa pygame.Rect predstavlja pravougaonik. Objekat pravougaonik možemo da kreiramo:
- Rect(left, top, width, height) -> Rect
	- left: udaljenost gorenjeg levog temena od leve ivice prozora (po x-osi)
	- top: udaljenost gorenjeg levog temena od gornje ivice prozora (po y-osi)
	- width: širina pravougaonika 
	- height: visina pravougaonika

### Prikaz na kanvas

Sa pygame.draw metodom možemo da crtanom razne oblike na canvasu. 

pygame.draw.line je metoda sa kojom možemo da crtamo liniju. 
- line(surface, color, start_pos, end_pos, width) -> Rect 
	- surface: Surface - je canvas na kojem crtamo 
	- color: Color, int, tuple(int, int, int, [int]) - je boja sa kojom crtamo oblik
	- start_pos: tuple(int or float, int or float) or list(int or float) - početno teme
	- end_pos: tuple(int or float, int or float) or list(int or float) - kranje teme
	- postoji i opcioni parametar width koji označava debljinu linije, po defaultu vrednost je 0 
	- povratna vrednost je Rect
	
pygame.draw.rect je metoda sa kojom možemo da crtamo pravougaonik. 
- rect(surface, color, rect) -> Rect 
	- surface: Surface - je canvas na kojem crtamo 
	- color: Color, int, tuple(int, int, int, [int]) - je boja sa kojom crtamo oblik
	- rect: Rect - pravougaonik koji crtamo, navodimo poziciju i dimenzije (širinu i visinu)
	- postoje i opcioni parametri kao što je width koji označava debljinu linije, po defaultu vrednost je 0 
	- povratna vrednost je Rect

pygame.draw.circle je metoda sa kojom možemo da crtamo krug. 
- circle(surface, color, center, radius) -> Rect 
	- surface: Surface - je canvas na kojem crtamo 
	- color: Color, int, tuple(int, int, int, [int]) - je boja sa kojom crtamo oblik
	- center: tuple(int or float, int or float) or list(int or float, int or float) - centar kruga predstavljen sa (x, y) koordinatama
	- radius: (int or float) - je poluprečnik kruga, računa se od centra
	- postoje i opcioni parametri kao što je width koji označava debljinu linije, po defaultu vrednost je 0 
	- povratna vrednost je Rect

pygame.draw.polygon je metoda sa kojom možemo da crtamo poligone. 
- polygon(surface, color, points) -> Rect 
	- surface: Surface - je canvas na kojem crtamo 
	- color: Color, int, tuple(int, int, int, [int]) - je boja sa kojom crtamo oblik	
	- points: (tuple(coordinate) or list(coordinate) - sekvenca tri ili više koordinata koje čine teme poligona
	- postoje i opcioni parametar width koji označava debljinu linije, po defaultu vrednost je 0 
	
Spisak ostalih oblika koje možete nacrtati se nalazi na sledećem [linku](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect).

### Prikazivanje postojeće slike

Potrebno je da učitamo sliku metodom image.load(putanja_do_slike).

BLIT (eng. bit-boundary block transfer) - logička operacija, gde se block podataka kopira ili prenosi u memoriju.
Na kanvasu možete prikazati i slike koje se nalaze u fajl sistemu sa metodom blit(). 
blit(source, dest, area=None, special_flag=0) -> Rect 
- source: Surface - canvas na kojem će se slika prikazati 
- dest: (tuple(coordinate) ili Rect - koordinate gorenjeg levog temena slike, ili Rect - koordinate gorenjeg levog temena pravougaonika

 
 
# Zadaci za vežbe

1. Kreirati projekat MyFirstGame u PyCharmu  
2. Instalirati pygame paket
3. Nacrtati sledeće slike:

![slika2](/slike/v8/sveca.png)

Slika 2.