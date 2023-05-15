# StudyGrouper

## Dokumentaatio

[tuntikirjanpito](https://github.com/Gudkat/ot-harjoitustyo/blob/master/python-study-grouper/dokumentaatio/tuntikirjanpito.md)

[vaatimusmäärittely](https://github.com/Gudkat/ot-harjoitustyo/blob/master/python-study-grouper/dokumentaatio/vaatimusmaarittely.md)

[changelog](https://github.com/Gudkat/ot-harjoitustyo/blob/master/python-study-grouper/dokumentaatio/changelog.md)

### Ohjelman asentaminen

Asenna ohjelman tarvitsemat riippuvuuden komennolla 

```bash
poetry install
```

Ensimmäisen käyttökerran yhteydessä käyttäjän tulee alustaa tietokanta graafisen käyttöliittymän kautta painamalla intialize database -nappia. 

Ohjelman sisäänkirjautuminen on oletuksena käyttäjänimi admin ja salasana admin. Nämä voi vaihtaa .env tiedostossa

### Ohjelman suorittaminen

Ohjelma käynnistetään komennolla

```bash
poetry run invoke start
```

### Ohjelman testaus
Ohjelman testit suoritetaan komennolla

poetry run invoke test

### Testikattavuusraportti

Testikattavuusraportti luodaan komennolla

poetry run invoke coverage-report

