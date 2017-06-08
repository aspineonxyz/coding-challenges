# [Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles)

Colleen is turning __*n*__ years old! She has __*n*__ candles of various heights on her cake, and candle __*i*__ has height __*height_i*__. Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the __*height_i*__ for each individual candle, find and print the number of candles she can successfully blow out.

#### Input Format
The first line contains a single integer, __*n*__, denoting the number of candles on the cake.
The second line contains __*n*__ space-separated integers, where each integer __*i*__ describes the height of candle __*i*__.

#### Constraints
* __*1 <= n <= 10^5*__
* __*1 <= height_i <= 10^7*__

#### Output Format
Print the number of candles Colleen blows out on a new line.

#### Sample Input 0
```
4
3 2 1 3
```

#### Sample Output 0
```
2
```

#### Explanation 0
We have one candle of height __*1*__, one candle of height __*2*__, and two candles of height __*3*__. Colleen only blows out the tallest candles, meaning the candles where __*height = 3*__. Because there are __*2*__ such candles, we print __*2*__ on a new line.
