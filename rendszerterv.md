I. A rendszer célja

Rendszerünk célja, hogy a Követelmény és Funkcionális specifikációban meghatározott megrendelői folyamatok megvalósuljanak.
Egy olyan programgyűjteményt szeretnénk elkészíteni ami kedvező a kisgyerekek fejlődéséhez, valamint gyermekek és fiatal felnőttek képpeségeik fejlesztéséhez.
A rendszert bárkielfogja tudni érni és az alkalmazás összes funkcióját kivétel nélkül minden felhasználó teljesen ingyen használhatja. Célunk, hogy
a felhasználók kikapcsolódhassanak amikor használják a programot, ezért csak olyan reklámokat használunk amelyek nem szakítják meg
Játékot.

II. Projektterv

	Dátum		Tevékenység						Résztvevő(k)
	
2019.10.17.-11.22.	Dokumentációk elkészítése és véglegesítése
2019.11.24.		Fejlesztés megkezdése
2019.11.24.-29.		Unit teszt
2019.11.29.-12.03.	Alpha teszt
2019.11.04.-12.07.	Béta teszt
2019.12.09.		Projekt átadása						A projektben résztvevő összes szereplő

III. Üzleti folyamatok modellje

Üzleti szereplõk:
	-Felhasználó
	-Admin

Támogatandó üzleti folyamatok:
	-kikapcsolódás
	-szórakozás


-Modell:
Kezdőoldal	Játékok---->Pacman
			I-->pong
			I-->snake
		 
		kilépés

IV. Követelmények

   Funkcionális követelmények:
	- Gördülékeny működés
	- Egyszerü telepítés	

   Nem funkcionális követelmények:
	- Letisztult, egyszerű kinézet
	- Minimális tárhely használata

V. Funkcionális terv

Rendszerszereplők:
	-Felhasználó

Rendszer használati esetek és lefutásaik:
	Felhasználó:
		-játék


VI. Fizikai környezet.

Kliens:

	Eszköz1	

		Eszköz:PC
		
		Operációs rendszer: Windows/Linux/IOS
		
		Környezet:python 3.7.5

		Konfiguráció: Nem specifikus.
		
		
VII. Absztrakt modell

A program mükődése során a felhasználó egyféle szerepkörben szerepelhet, mint játékos.
Egyetlen sima user felület áll rendelkezésre, a programhoz mindenkinek ugyanolyan
joga van. Rendelkezésre áll a 3 játék: -Pong, Pac-Man, Snake.

VIII. Implementációs terv

A játékok, a program felülete Python Turtle, PyCharmban készült.
Python 3.7 és/vagy 3.7.5-ben készültek.

IX. Tesztterv

 I. Alpha teszt:
	Az Alpha tesztet a program készítői végzik, amelyben a rendszert hibáit keresik.
	Amint felderítenek egy hibát jelentést írnak róla és javítják.
	Az alpha teszt során külön kell tesztelni több fontos funkciót, mint például:
	-A karakter mozgás tökéletes mükődése, megfelelő pontrendszer, dizájn letisztultsága.
 II. Béta teszt
	Itt a felhasználók elvégzik a tesztet, ahol az apróbb bugok, a játékok stabilitása,
	letisztultsága a cél.
X. Karbantartási terv
	A szoftveren nagyobb karbantartásokat nem kell végezni.
	Esetlegesen frisebb verziójú Python használatával megoldani, és azokon esetleges új
	hibák javítása.
	Igény szerint új funkciók, játékok hozzáadása.


