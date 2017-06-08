# [The Hurdle Race](https://www.hackerrank.com/challenges/the-hurdle-race)

Dan is playing a video game in which his character competes in a hurdle race by jumping over __*n*__ hurdles with heights __*h_0,h_1, ... , h_n-1*__. He can initially jump a maximum height of __*k*__ units, but he has an unlimited supply of magic beverages that help him jump higher! Each time Dan drinks a magic beverage, the maximum height he can jump during the race increases by __*1*__ unit.

Given __*n*__, __*k*__, and the heights of all the hurdles, find and print the minimum number of magic beverages Dan must drink to complete the race.

#### Input Format
The first line contains two space-separated integers describing the respective values of __*n*__ (the number of hurdles) and __*k*__ (the maximum height he can jump without consuming any beverages).
The second line contains  space-separated integers describing the respective values of __*h_0, h_1, ... , h_n-1*__.

#### Constraints
* __*1 <= n, k <= 100*__
* __*1 <= h_i <= 100*__

#### Output Format
Print an integer denoting the *minimum* number of magic beverages Dan must drink to complete the hurdle race.

#### Sample Input 0
```
5 4
1 6 3 5 2
```

#### Sample Output 0
```
2
```

#### Explanation 0
Dan's character can jump a maximum of __*k = 4*__ units, but the tallest hurdle has a height of __*h_1 = 6*__:

<p align="center">
    <img src="" alt="">
</p>

To be able to jump all the hurdles, Dan must drink __*6 - 4 = 2*__ magic beverages.

#### Sample Input 1
```
5 7
2 5 4 5 2
```

#### Sample Output 1
```
0
```

#### Explanation 1
Dan's character can jump a maximum of __*k = 7*__ units, which is enough to cross all the hurdles:

<p align="center">
    <img src="" alt="">
</p>

Because he can already jump all the hurdles, Dan needs to drink __*0*__ magic beverages.
