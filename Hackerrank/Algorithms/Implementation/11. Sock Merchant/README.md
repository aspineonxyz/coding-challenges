# [Sock Merchant](https://www.hackerrank.com/challenges/sock-merchant)

John's clothing store has a pile of __*n*__ loose socks where each sock __*i*__ is labeled with an integer, __*c_i*__, denoting its color. He wants to sell as many socks as possible, but his customers will only buy them in matching pairs. Two socks, __*i*__ and __*j*__, are a single matching pair if __*c_i = c_j*__.

Given __*n*__ and the color of each sock, how many pairs of socks can John sell?

#### Input Format
The first line contains an integer, __*n*__, denoting the number of socks.
The second line contains __*n*__ space-separated integers describing the respective values of __*c_0, c_1, c_2, ... , c_n-1*__.

#### Constraints
* __*1 <= n <= 100*__
* __*1 <= c_i <= 100*__

#### Output Format

Print the total number of *matching pairs* of socks that John can sell.

#### Sample Input
```
9
10 20 20 10 10 30 50 10 20
```

#### Sample Output
```
3
```

#### Explanation

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/11.%20Sock%20Merchant/img/sock-merchant-1.png" alt=sock-merchant-1>
</p>

As you can see from the figure above, we can match three pairs of socks. Thus, we print __*3*__ on a new line. 
