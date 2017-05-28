# Birthday Chocolate

Lily has a chocolate bar consisting of a row of  squares where each square has an integer written on it. She wants to share it with Ron for his birthday, which falls on month __*m*__ and day __*d*__. Lily only wants to give Ron a piece of chocolate if it contains __*m*__ consecutive squares whose integers sum to __*d*__.

Given __*m*__, __*d*__, and the sequence of integers written on each square of Lily's chocolate bar, how many different ways can Lily break off a piece of chocolate to give to Ron?

For example, if __*m = 2*__, __*d = 3*__ and the chocolate bar contains __*n*__ rows of squares with the integers __*[1, 2, 1, 3, 2]*__ written on them from left to right, the following diagram shows two ways to break off a piece:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/6.%20Birthday%20Chocolate/img/birthday-chocolate-1.png" alt="chocolate-1">
</p>

#### Input Format

The first line contains an integer denoting __*n*__ (the number of squares in the chocolate bar).
The second line contains __*n*__ space-separated integers describing the respective values of __*s_0, s_1, ... , s_n-1*__ (the numbers written on each consecutive square of chocolate).
The third line contains two space-separated integers describing the respective values of __*d*__ (Ron's birth day) and __*m*__ (Ron's birth month).

#### Constraints
* __*1 <= n <= 100*__
* __*1 <= s_i <= 5*__, where (__*0 <= i < n*__)
* __*1 <= d <= 31*__
* __*1 <= m <=12*__

#### Output Format

Print an integer denoting the total number of ways that Lily can give a piece of chocolate to Ron.

#### Sample Input 0
```
5
1 2 1 3 2
3 2
```

#### Sample Output 0
```
2
```

#### Explanation 0

This sample is already explained in the problem statement.

#### Sample Input 1
```
6
1 1 1 1 1 1
3 2
```

#### Sample Output 1
```
0
```

#### Explanation 1
Lily only wants to give Ron __*m = 2*__ consecutive squares of chocolate whose integers sum to __*d = 3*__. There are no possible pieces satisfying these constraints:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/6.%20Birthday%20Chocolate/img/birthday-chocolate-2.png" alt="chocolate-2">
</p>

Thus, we print __*0*__ as our answer.

#### Sample Input 2
```
1
4
4 1
```

#### Sample Output 2
```
1
```

#### Explanation 2
Lily only wants to give Ron __*m = 1*__ square of chocolate with an integer value of __*d = 4*__. Because the only square of chocolate in the bar satisfies this constraint, we print __*1*__ as our answer.
