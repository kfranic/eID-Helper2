# eID Helper v1.0

[![GitHub Release](https://github-basic-badges.herokuapp.com/release/mariosemes/eID-Helper.svg)]() [![GitHub Download Count](https://github-basic-badges.herokuapp.com/downloads/mariosemes/eID-Helper/total.svg)]() [![GitHub Issues Open](https://github-basic-badges.herokuapp.com/issues/mariosemes/eID-Helper.svg)]()

##### Preuzimanje (x86 & x64):
https://github.com/mariosemes/eID-Helper/releases

##### Napomena:
Aplikacija eID Helper ni na koji način nije povezana niti je dio sustava elektroničke osobne iskaznice (eOI) građana Republike Hrvatske (eid.hr). Aplikacija je Open-Source te zahvaljujući problemima s eID aplikacijom, tako je i nastala.


## Gdje, što i zašto?
Jedan od razloga zašto i jeste ovdje je problem potpisivanja servisa eID-a prilikom potpisivanja, često neuspješno. Na bazi službenog odgovora podrške eOI, kada se desi navedeni problem, potrebno je pronaći i ugasiti proces koji radi na portu "55555" pa zatim ponovno pokrenuti Signer.exe.

## Aplikacija eID Helper radi upravo to.
1. Pronalazi proces na portu "55555"
2. Silno ga gasi ukoliko je aktivan
3. Pronalazi Signer.exe na računalu
4. Ponovno pokreće aplikaciju za potpisivanje

## Windows Security
Windows će prepoznati eID Helper kao prijetnju, iz razloga što autor aplikacije nije prijavljen (da skratim... nisam lud), stoga paljenje aplikacije je u potpunosti na vama.
Jedan od razloga zašto je aplikacija na GitHub-u je transparentnost koda.
