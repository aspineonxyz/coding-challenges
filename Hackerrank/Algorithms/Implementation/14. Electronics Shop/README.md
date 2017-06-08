# [Electronics Shop](https://www.hackerrank.com/challenges/electronics-shop)

Monica wants to buy exactly one keyboard and one USB drive from her favourite electronics store. The store sells __*n*__ different brands of keyboards and __*m*__ different brands of USB drives. Monica has exactly __*s*__ dollars to spend, and she wants to spend as much of it as possible (i.e., the total cost of her purchase must be maximal).

Given the price lists for the store's keyboards and USB drives, find and print the amount money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print `-1` instead.

__Note:__ She will never buy more than one keyboard and one USB drive even if she has the leftover money to do so.

#### Input Format
The first line contains three space-separated integers describing the respective values of __*s*__ (the amount of money Monica has), __*n*__ (the number of keyboard brands) and __*m*__ (the number of USB drive brands).

The second line contains __*n*__ space-separated integers denoting the prices of each keyboard brand.

The third line contains __*m*__ space-separated integers denoting the prices of each USB drive brand.

#### Constraints
* __*1 <= n, m <= 1000*__
* __*1 <= s <= 10^6*__
* The price of each item is in the inclusive range __*[1, 10^6]*__

#### Output Format
Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print `-1` instead.

#### Sample Input 0
```
10 2 3
3 1
5 2 8
```

#### Sample Output 0
```
9
```

#### Explanation 0
She can buy the __*2nd*__ keyboard and the __*3rd*__ USB drive for a total cost of __*8 + 1 = 9*__.

#### Sample Input 1
```
5 1 1
4
5
```

#### Sample Output 1
```
-1
```

#### Explanation 1
There is no way to buy one keyboard and one USB drive because __*4 + 5 > 5*__, so we print __*-1*__.
