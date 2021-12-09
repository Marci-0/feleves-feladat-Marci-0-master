# Feleves Feladat

1) Semmit
2) Csinaljon Web-es REST-es endpoint-ot amin fel lehet vinni resource-okat (POST, GET). A resource-t FS-en tarolja (JSON). A request-et validalja.
3) A resource-okat MongoDB-ben tarolja.
4) A felvitt resrouce-on egyszeru elemzeseket vegez async modon (fork, Queue) es update-eli a resource-t az eredmennyel. Egyszeru elemzes peldaul statisztikai szamitasok vagy numerikus modszerek (numpy, scipy). 
5) A resource alapjan komplex adatelemzest es vizualizaciot vege adatbanyaszati modszerekkel. Peldaul, klaszterezes, predikcio (regressziova) vagy adat vizualizacio (scikit, sklearn, pandas, matplotlib, seaborn). 

A feldatokkal szemben tamasztott altalanos elvarasok:
 - PEP8 PyLint / Flake8
 - Git, Github (Classroom-os repo)
 - Teszteles 

Feladat otletek
 - Vernyomasmero berendezes kiertekelese. A paciens hordja a keszuleket ami adott idokozonkent rogziti a vernyomasat (systolic, diastolic). Keressunk erdekes esemenyeket, jelezzuk az eredmenyben es vizualizaljuk az adatokat.

 - Greenhouse sensor evaluation. Uveghazban merjuk a temperatuer-t, hummidity-t es a brightness-t (fenyero). Statisztikai adatok es vizualizacio.

- Tomegkozlekedes, forgalom szamlalas. Adot jaraton Minden megallo utan megszamoljuk az utasokat (felszallok, leszallok). Az egyes jaratokon a megallok szama fix. A jarat az ut vegen feltolti a merest es az idopontot. Az egyes jaratokon mennyi az atlagos forgalom? Melyik megallokon van sok felszallo / leszallo? Az utasok letszamat grafikonon abrazolja. 

- Barmi egyeb otlet johet
