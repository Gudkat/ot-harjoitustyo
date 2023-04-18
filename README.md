# StudyGrouper

## Dokumentaatio

[tuntikirjanpito](https://github.com/Gudkat/ot-harjoitustyo/blob/master/python-study-grouper/dokumentaatio/tuntikirjanpito.md)

[vaatimusmäärittely](https://github.com/Gudkat/ot-harjoitustyo/blob/master/python-study-grouper/dokumentaatio/vaatimusmaarittely.md)

[changelog](https://github.com/Gudkat/ot-harjoitustyo/blob/master/python-study-grouper/dokumentaatio/changelog.md)

### Ohjelman suorittaminen

Ohjelma alustaa tietokannan komennolla 

poetry run invoke start

Ohjelman käyttöliittymä ei lähde tällä komennolla käyntiin toistaiseksi (importtien kanssa tappelussa kului aikaa. sain apua pajasta mutta ei ollut aikaa osaamiseni puitteissa korjata tänään), se pitää avata ui kansiosta ui.py tiedoston kautta. Käyttöliittymässä toimii tällähetkellä kirjautmisnäkymä, siitä siirtyminen vierastilaan ja siellä kurssin ja sähköpostin lisääminen tietokantaan, ja tästä tilasta palaaminen kirjautumisnäkymään

### Ohjelman testaus
Ohjelman testit suoritetaan komennolla

poetry run invoke test

### Testikattavuusraportti

Testikattavuusraportti luodaan komennolla

poetry run invoke coverage-report

