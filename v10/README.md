# Animacije 

Primer: [StageAnimation](/v10/StageAnimation)

# Animacija učitanih slika 

Do sada smo predstavljali predmete na kanvasu kao skup geometrijskih oblika koje smo iscrtavali uz pomoć pygame.draw metode. Prilikom pokretanja smo menjali koordinate x (kretanje levo, desno) i y (kretanje gore, dole) svih geometrijskih oblika od kojih je predmet sačinjen. <br />
Ove nedelje ćemo učitavati skup slika eng. sprite. Pozivom ovih slika dobijamo efekat kretanja predmeta na kanvasu. Slike se učitavaju sa pygame.image.load(putanja_do_slike) metodom i iscrtavaju se na kanvas sa canvas.blit(ucitana_slika) metodom. Sprite sa kojim ćemo raditi je dinosaurus koji se nalazi na [linku](/sprites/v10/png/dino). Postoje dosta besplatnih slika online npr. [link](https://www.gameart2d.com/freebies.html).
<br />

## Priprema slika za iscrtavanje 
Modul [load_sprites](/v10/StageAnimation/load_sprites.py)
Slike je neophodno učitati u in-memory kolekciju. Moguće je koristiti rečnik za čuvanje učitanih slika. Rečnik predstavlja mogu stanja u kojim se dino nalazi. 
<br />
Moguća stanja su u rečniku predstavljena kao ključevi i imaju redom vrednosti:

- 0 (Dead)
- 1 (Idle)
- 2 (Jump)
- 3 (Run)
- 4 (Walk)

Za svako stanje postoji skup slika u [folderu](/sprites/v10/png/dino). Vrednosti prethodno nabrojanih ključeva su učitane korespodentne slike za data stanja. Npr. za stanje Idle, kada dino stoji, imamo 10 slika (Idle(1), Idle(2), itd.) i ove slike će biti učitane kao elementi liste images_dino_idle. Potom će ova lista da bude dodata odgovarajućem ključu unutar rečnika (npr. dino_stages["Idle"] = images_dino_idle, itd.). Neophodno je na odgovarajući način učitati sve slike, i grupisati ih unutar kolekcije kao što je npr. rečnik.

<br />

## Iscrtavanje slike (kretanje u mestu)
Metoda new_frame_no_movement(canvas, width, height, y_horizon) unutar modula [draw_sprites](/v10/StageAnimation/draw_sprites.py)
<br />
Pre nego što se slika iscrta proverava se stanje u kojem se slika nalazi i koja slika je po redu se se prikaže iz tog stanja. (metode, calculate_stage() i calculate_show_image()). Dodatne promenljive koje opisuju stanje i sliku su: 

- image_stage:int vrednost ključa, predstavlja stanje u kojem se nalazi dino (npr. 0-Dead, 1-Idle, itd.)
- image_index:int vrednost pozicije elementa u listi, predstavlja sliku dina u posmatranom stanju (npr. Idle(1) je na poziciji 0 u listi koja se nalazi u rečniku pod vrednosti ključa 1, itd.)

U prvom primeru dino se kreće u mestu tako da image_stage = 4 (stanje Walk) i image_index treba da se menja u svakom frejmu (indeksi od 0 do 9). Ako se stavi image_index = 0 kreće se od prve slike.
U svakom frejmu treba da prikazujemo novu sliku dinosaurusa (u posmatranom stanju Walk), dok ne stignemo do poslednje slike u posmatranoj listi. Kada se stigne do poslednje slike neophodno je vratiti se na prvu sliku (image_index = 0). Implementacija rešenja je u metodi calculate_show_image().
<br />
Na kraju se iscrtava pozadina i dino sa metodama draw_background(canvas, width, height, y_horizon) i draw_dino(canvas, load.dino_stages, y_horizon). Parametri koji se prosleđuju ovim metodama su canvas na kojem će se iscrtati pozadina i sprite, širina i visina prozora i y_horizon koji predstavlja y koordinatu podloge na kojoj se dino nalazi i na kojoj će se kretati.

## Iscrtavanje slike sa kretanjem na podlozi
Metoda new_frame_movement(canvas, width, height, y_horizon, dino_step) unutar modula [draw_sprites](/v10/StageAnimation/draw_sprites.py)
<br />
U ovom primeru imamo promenu vrednosti x-koordinate dinosaurusa tako da se kreće ka desnoj ivici ekrana. Kada dođe do kraja nastaviće kretanje van prozora.

## Iscrtavanje slike sa kretanjem na podlozi prilikom čega se postuju granice
Metoda new_frame_movement2(canvas, width, height, y_horizon, dino_step) unutar modula [draw_sprites](/v10/StageAnimation/draw_sprites.py)
<br />
U ovom primeru imamo promenu vrednosti x-koordinate dinosaurusa tako da se kreće ka desnoj ivici ekrana. U svakom frejmu imamo proveru da li se dino kreće u granicama prozora sa metodom check_in_screen(x, y, x_max, y_max, x_min=0, y_min=0). Ostatak koda je isti kao u prethodnim primerima.

## Iscrtavanje slike sa kretanjem, proverom granica ekrana i kolizije sa kamenom
Metoda new_frame_movement3(canvas, width, height, y_horizon, dino_step) unutar modula [draw_sprites](/v10/StageAnimation/draw_sprites.py)

Unutar metode calculate_stage(collision) vrši se provera u svakom frejmu da li sprite treba da promeni svoje stanje. Ovde se pišu uslovi kada treba da dođe do promene stanja (npr. kada treba iz stanja Walk da pređe u stanje Dead). Prosleđuje se dodatni parametar collision kao indikator da li je došlo do kolizije i ako jeste da se menja stanje u Dead image_stage = 0 i da se krene od prve slike za dato stanje image_index = 0.

Napomena: Prvo pozivati calculate_stage() pa tek onda calculate_show_image() metodu.

## Zadaci za vežbu 

U prvom zadatku neophodno je dopuniti calculate_stage sa proverom da li treba dino da pređe iz stanja Dead u Walking. Dino treba iz stanje Walking u Dead da pređe kada udari u kamen i onda iz stanja Dead u Walking kada se prikaže poslednja slika za Dead (kada image_index >= len(load.dino_stages.get(image_stage)) - 1). Kako dino ne bi ponovo završio u Dead stanju neophodno ga je malo pomeriti pa ponovo proveriti collision.
<br />

U drugom zadatku neophodno je napisati novu calculate_stage metodu tako da proverava da li je došlo do kolizije i ako jeste da se prelazi iz stanja Walking u Jump. Dodatna provera je da li je dino završio sa skokom (kada dotakne podlogu onda je skok završen) i u tom trenutku prelazi iz stanja Jump u Walk opet. Prilikom skoka treba da se menja i pravac kretanja, ne samo po x osi nego i po y-osi. Kada se vrati u stanje Walk onda je opet samo po x-osi kretanje.

## Definisanje boja po naziv 

Klasa Color pygame.Color(color_value) ima parametar color_value po kojem se boja zadaje po nazivu (string tip). Spisak naziva boja možete pronaći na sledećem [linku](https://mike632t.wordpress.com/2018/02/10/displaying-a-list-of-the-named-colours-available-in-pygame/)


# Zadaci za vežbu 

1. Dopuniti zadatak StageAnimation tako da primer kretanja dinosaurusa funkcioniše na način koji je prikazan na slici 1. Dinosaurus prilikom sudaranja sa kamenom treba da padne, nakon čega nastavlja kretanje.
2. Dopuniti zadatak StageAnimacija tako da primer kretanja dinosaurusa funkcioniše na način koji je prikazan na slici 2. Dinosaurus prilikom sudaranja sa kamenom treba da ga preskoči, nakon čega nastavlja kretanje.
<br />

![slika1](/slike/v10/dino_collision.gif)

Slika 1.

![slika2](/slike/v10/dino_jump.gif)

Slika 2.
