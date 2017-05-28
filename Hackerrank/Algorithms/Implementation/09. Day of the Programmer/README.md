# Day of the Programmer

Marie invented a [Time Machine](https://en.wikipedia.org/wiki/Time_machine) and wants to test it by time-traveling to visit Russia on the [Day of the Programmer](https://en.wikipedia.org/wiki/Day_of_the_Programmer) (the __*256th*__ day of the year) during a year in the inclusive range from __*1700*__ to __*2700*__.

From __*1700*__ to __*1917*__, Russia's official calendar was the [Julian calendar](https://en.wikipedia.org/wiki/Julian_calendar); since __**__ they used the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) system. The transition from the Julian to Gregorian calendar system occurred in __*1918*__, when the next day after January __*31st*__ was February __*14th*__. This means that in __*1918*__, February __*14th*__ was the __*32nd*__ day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has __*29*__ days during a leap year, and __*28*__ days during all other years. In the Julian calendar, leap years are divisible by __*4*__; in the Gregorian calendar, leap years are either of the following:

Divisible by __*400*__.
Divisible by __*4*__ and not divisible by __*100*__.

Given a year, __*y*__, find the date of the __*256th*__ day of that year according to the official Russian calendar during that year. Then print it in the format `dd.mm.yyyy`, where `dd` is the two-digit day, `mm` is the two-digit month, and `yyyy` is __*y*__.

#### Input Format
A single integer denoting year __*y*__.

#### Constraints
* __*1700 <= y <= 2700*__

#### Output Format
Print the full date of Day of the Programmer during year __*y*__ in the format `dd.mm.yyyy`, where `dd` is the two-digit day, `mm` is the two-digit month, and `yyyy` is __*y*__.

#### Sample Input 0
```
2017
```

#### Sample Output 0
```
13.09.2017
```

#### Explanation 0
In the year __*y = 2017*__, January has __*31*__ days, February has __*28*__ days, March has __*31*__ days, April has __*30*__ days, May has __*31*__ days, June has __*30*__ days, July has __*31*__ days, and August has __*31*__ days. When we sum the total number of days in the first eight months, we get __*31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 = 243*__. Day of the Programmer is the __*256th*__ day, so then calculate __*256 - 243 = 13*__ to determine that it falls on day __*13*__ of the __*9th*__ month (September). We then print the full date in the specified format, which is `13.09.2017`.

#### Sample Input 1
```
2016
```

#### Sample Output 1
```
12.09.2016
```

#### Explanation 1
Year __*y = 2016*__ is a leap year, so February has __*29*__ days but all the other months have the same number of days as in __*2017*__. When we sum the total number of days in the first eight months, we get __*31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 = 244*__. Day of the Programmer is the __*256th*__ day, so then calculate  to determine that it falls on day __*12*__ of the __*9th*__ month (September). We then print the full date in the specified format, which is `12.09.2016`.
