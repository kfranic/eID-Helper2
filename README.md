# eID Helper Fork v1.0


[![GitHub Release](https://github-basic-badges.herokuapp.com/release/kfranic/eID-Helper.svg)]() [![GitHub Download Count](https://github-basic-badges.herokuapp.com/downloads/kfranic/eID-Helper/total.svg)]() [![GitHub Issues Open](https://github-basic-badges.herokuapp.com/issues/kfranic/eID-Helper.svg)]()

## Zašto fork:
Razlog zašto sam napravio fork sa https://github.com/mariosemes/eID-Helper je da podjelim male promjene koje su potencijalno zanimljive nekom drugom i kako mi tool nije pomogao da pdijelim detalje kako debugirati problem.
Kod mene se javio isti problem:
![image](https://github.com/user-attachments/assets/f5d4efa9-999a-444b-a1a9-7ca0e0e12a88)

no kod mene je taj port nije bio otvoren već je problem bio što je port 55555 u excluded range-u.

    C:\>netsh int ipv4 show excludedportrange protocol=tcp
    
    Protocol tcp Port Exclusion Ranges
    
    Start Port    End Port
    ----------    --------
          5357        5357
         49676       49775
         49876       49975
         50000       50059     *
         50160       50259
         50360       50459
         50560       50659
         50760       50859
         54640       54739
         54740       54839
         54840       54939
         54940       55039
         55075       55174
         55175       55274
         55275       55374
         55375       55474
         55475       55574
         56006       56105
         56106       56205
         56206       56305
    
    * - Administered port exclusions.
    
    
    C:\>



## Napomena:
Aplikacija eID Helper ni na koji način nije povezana niti je dio sustava elektroničke osobne iskaznice (eOI) građana Republike Hrvatske (eid.hr). Aplikacija je Open-Source te zahvaljujući problemima s eID aplikacijom, tako je i nastala.
