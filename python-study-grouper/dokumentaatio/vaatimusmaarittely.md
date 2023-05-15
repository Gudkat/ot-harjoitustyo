# Vaatimusmääritely 

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on auttaa opiskelijoita löytämään samaa kurssia suorittavia opiskelijoita, joiden kanssa voi suorittaa kurssia yhdessä ja tehdä harjoitustehtäviä ryhmissä. Sovellusta käyttää _pääkäyttäjä_, joka voi luoda ryhmiä ja lisätä opiskelijoita ryhmiin. Opiskelija voi ilmoittautua ryhmähakuun _Guest_ tilassa.

## Käyttäjät

Sovelluksella on aluksi yksi käyttäjärooli; _pääkäyttäjä_. _Pääkäyttäjällä_ on oikeudet hallinnoida ryhmiä ja käyttäjätilejä. Myöhemmin ohjelmaan saatetaan lisätä _Opiskelija_ käyttäjä ryhmä, jolla on oikeus nähdä omat ryhmät sekä liittyä että poistua ryhmistä, ja _RyhmänOmistaja_ rooli jolla on oikeus luoda ryhmiä ja hallinnoida itse luomiaan ryhmiä.

## Käyttöliittymäluonnos

Sovellus koostuu viidestä eri näkymästä. 

![](./kuvat/UI_sketch.jpg)

Sovellus aukeaa kirjautumisnäkymään, josta voi joko kirjautua sisään pääkäyttäjän tunnuksilla tai käytätä ohjelmaa _Guest_ tilassa. Mikäli käyttäjä valitsee _Guest_ tilan, hän pääsee näkymään, missä voi lisätä kurssin tunnuksen ja sähköpostiosoitteen, mikä vastaa ilmottautumista opintoryhmän etsijäksi. Mikäli ohjelman käyttäjä valitsee kirjautumisen alkutilassa, tämän jälkeen hänellä on status _pääkäyttäjä_. _Pääkäyttäjä_ pääsee kurssilistaukseen, josta voi joko valita tai poistaa kurssin sekä näkee ryhmää etsivien opiskelijoiden opiskelijoiden määrän. Kurssivalinnan jälkeen _pääkäyttäjä_ näkee kaikki kurssin opiskelijaryhmät. Tässä näkymässä _pääkäyttäjä_ voi luoda uuden ryhmän, tai lisätä opiskelijoita aiemmin luotuihin ryhmiin. Jos _pääkäyttäjä_ valitsee kurssilaisten lisäyksen, hän siirtyy listaukseen, missä näkyy ryhmättömät opiskelijat. 

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Opiskelija voi lisätä itsensä ohjelmaan ilman käyttäjätiliä.

- Ohjelmalla on vain yksi käyttäjä, _pääkäyttäjä_, joten tunnusta ei tarvitse luoda vaan se on jo olemassa.
- _Pääkäyttäjä_ voi kirjautua sisään sovellukseen. 

### Kirjautumisen jälkeen

- _Pääkäyttäjä_ näkee kaikki kurssit, joihin on liitetty opiskelijoita.
  - _Pääkäyttäjä_ voi poistaa kurssin.
  - _Pääkäyttäjä_ voi valita kurssin, 
    - Ohjelma näyttää valitun kurssin opintoryhmät.
    - Jos valitaan ryhmä, ohjelma näyttää ryhmän jäsenten sähköpostiosoitteet.
    - Käyttäjä voi luoda uuden ryhmän.
    - Käyttäjä voi lisätä opiskelijoita ryhmiin.
- Käyttäjä voi kirjautua ulos sovelluksesta.

## Jatkokehitysideoita

Perusversion jälkeen sovellukseen voisi lisätä seuraavia ominaisuuksia:
- Mahdollistaa opiskelijan ilmottautumaan ryhmähakuun verkon kautta.
- Voidaan luoda uusia käyttäjäryhmiä
  - _Opiskelija_
    - _Opiskelija_ näkisi omat ryhmänsä ja voisi hallinnoida jäsenyyttään niissä
          - _Opiskelija_ voi lisätä itselle sopivat ajat yhdessäopiskeluun ryhmähaussa
  - _RyhmänOmistaja_
    - _RyhmänOmistaja_ voi luoda ryhmiä
      - Kurssin opettaja voi luoda ryhmiä opiskelijoille
    - _RyhmänOmistaja_ voi hallinnoida omia ryhmiään    
- Ryhmänäkymään tulisi näkyville, milloin opiskelijat ovat vapaana yhdessäopiskeluun
- Erilaisten ryhmien luominen
  - Mahdollisuus valita kuinka monta opiskelijaa mahtuu mukaan ryhmään
  - Mahdollisuus luoda etäopiskeluryhmiä
  - Määrittely tavotteista ryhmälle
- Ryhmien näkyminen opiskelijoille, jolloin opiskelija voi valita mihin ryhmään haluaa liittyä
- Ryhmän luoja saa _RyhmänOmistajan_ oikeudet
  - Ryhmän omistaja voi kutsua opiskelijoita ryhmään
  - Ryhmän omistaja voi poistaa ryhmän jäseniä
  - Jos ryhmän omistaja poistaa itsensä ryhmästä, ryhmän omistajaksi valitaan ryhmässä oleva opiskelija, joka on ollut ryhmässä kauimmin
