# [Breaking the Records](https://www.hackerrank.com/challenges/breaking-best-and-worst-records)

Maria plays __*n*__ games of college basketball in a season. Because she wants to go pro, she tracks her points scored per game sequentially in an array defined as __*score = [s_0, s_1, ... , s_n-1]*__. After each game __*i*__, she checks to see if score __*s_i*__ breaks her record for most or least points scored so far during that season.

Given Maria's array of __*scores*__ for a season of __*n*__ games, find and print the number of times she breaks her record for most and least points scored during the season.

__Note:__ Assume her records for most and least points at the start of the season are the number of points scored during the first game of the season.

#### Input Format
The first line contains an integer denoting __*n*__ (the number of games).
The second line contains __*n*__ space-separated integers describing the respective values of __*s_0, s_1, ... , s_n-1*__.

#### Constraints
* __*1 <= n <= 1000*__
* __*0 <= s_i <= 10^8*__

#### Output Format
Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.

#### Sample Input 0
```
9
10 5 20 20 4 5 2 25 1
```

#### Sample Output 0
```
2 4
```

#### Explanation 0
The diagram below depicts the number of times Maria broke her best and worst records throughout the season:

<p align="center">
  <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/05.%20Breaking%20the%20Records/img/breaking-the-records-1.png" alt="records-1">
</p>

She broke her best record twice (after games __*2*__ and __*7*__) and her worst record four times (after games __*1*__, __*4*__, __*6*__, and __*8*__), so we print `2 4` as our answer. Note that she did not break her record for best score during game __*3*__, as her score during that game was not strictly greater than her best record at the time.

#### Sample Input 1
```
10
3 4 21 36 10 28 35 5 24 42
```

#### Sample Output 1
```
4 0
```

#### Explanation 1
The diagram below depicts the number of times Maria broke her best and worst records throughout the season:

<p align="center">
  <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/05.%20Breaking%20the%20Records/img/breaking-the-records-2.png" alt="records-2">
</p>

She broke her best record four times (after games __*1*__, __*2*__, __*3*__, and __*9*__) and her worst record zero times (no score during the season was lower than the one she earned during her first game), so we print `4 0` as our answer.
