# Crtanje teksta

Primer: [StageAnimWithText](/v11/StageAnimWithText)

pygame.font je modul za učitavanje i prikazivanje teksta.  <br />
Potrebno je kreirati Font objekat sa pygame.font.SysFont <br />
SysFont(name, size, bold=False, italic=False) -> Font

- kreira se Font objekat iz sistemskih fontova. Link do fontova u Windows 10 operativnom sistemu [fonts](https://docs.microsoft.com/en-us/typography/fonts/windows_10_font_list)
- name:str naziv font-a. Ako se zadato ime fonta ne postoji, odabraće se font koji je sličan navedenom ili default
- size:int veličina slova

Font(filename, size) -> Font 

- kreira Font objekat iz fajla . To su fajlovi sa ekstenzijom npr. .TTF, .EOT, .OTF, itd.. TTF fajl je font file format koji je kreiran od strane Apple, ali koristi se u Macintosh i Windows operativnim sistemima. 

Nakon toga treba da nacrtamo font na novu podlogu. <br />
font.render(text, antialias, color, background=None) -> Surface 

- text: str, text koji će se ispisati 
- antialias:bool (True, False) - indikator da li da ivice slova budu glatke ili ne. Ako se ne koristi anti-alias onda slika koja se prikazuje je 8-bitna, iz dve boje. 
- color:Color - boja teksta

Nakon toga ova podloga (eng. Surface) može da se blit-uje (prikaže) na kanavasu. <br />
canvas.blit(text_image, (x, y))

- text_image:Surface - podloga sa tekstom, kreiran preko render metode 
- (x, y):(int, int) - koordinate po x i y osi koje određuju poziciju gde će se text isrctati na kanvasu
