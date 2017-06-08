# [Divisible Sum pairs](https://www.hackerrank.com/challenges/divisible-sum-pairs)

You are given an array of __*n*__ integers, __*a_0, a_1 ... , a_n-1*__, and a positive integer, __*k*__. Find and print the number of __*(i, j)*__ pairs where __*i < j*__ and __*a_i*__ + __*a_j*__ is evenly divisible by __*k*__.

#### Input Format

The first line contains __*2*__ space-separated integers, __*n*__ and __*k*__, respectively.
The second line contains __*n*__ space-separated integers describing the respective values of __*a_0, a_1 ... , a_n-1*__.

#### Constraints
* __*2 <= n <= 100*__
* __*1 <= k <= 100*__
* __*1 <= a_i <= 100*__

#### Output Format
Print the number of __*(i, j)*__ pairs where __*i < j*__ and __*a_i*__ + __*a_j*__ is evenly divisible by __*k*__.

#### Sample Input
```
6 3
1 3 2 6 1 2
```

#### Sample Output
```
 5
```

#### Explanation
Here are the __*5*__ valid pairs:
* __*(0, 2) -> a_0 + a_2 = 1 + 2 = 3*__
* __*(0, 5) -> a_0 + a_5 = 1 + 2 = 3*__
* __*(1, 3) -> a_1 + a_3 = 3 + 6 = 9*__
* __*(2, 4) -> a_2 + a_4 = 2 + 1 = 3*__
* __*(4, 5) -> a_4 + a_5 = 1 + 2 = 3*__
