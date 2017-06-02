# Forming a Magic Square

We define a [magic square](https://en.wikipedia.org/wiki/Magic_square) to be an __*n * n*__ matrix of distinct positive integers from __*1*__ to __*n^2*__ where the sum of any row, column, or diagonal (of length __*n*__) is always equal to the same number (i.e., the *magic constant*).

Consider a __*3 * 3*__ matrix, __*s*__, of integers in the inclusive range __*[1, 9]*__. We can convert any digit, __*a*__, to any other digit, __*b*__, in the range __*[1, 9]*__ at cost __*|a - b|*__.

Given __*s*__, convert it into a magic square at minimal cost by changing zero or more of its digits. Then print this cost on a new line.

__Note:__ The resulting magic square must contain distinct integers in the inclusive range __*[1, 9]*__.

#### Input Format
There are __*3*__ lines of input. Each line describes a row of the matrix in the form of __*3*__ space-separated integers denoting the respective first, second, and third elements of that row.

#### Constraints
* All integers in __*s*__ are in the inclusive range __*[1, 9]*__.

#### Output Format
Print an integer denoting the minimum cost of turning matrix __*s*__ into a magic square.

#### Sample Input
```
4 9 2
3 5 7
8 1 5
```

#### Sample Output
```
1
```

#### Explanation
Matrix __*s*__ initially looks like this:
```
4 9 2
3 5 7
8 1 5
```

Observe that it's not yet magic, because not all rows, columns, and center diagonals sum to the same number.

If we change the bottom right value, __*s[2][2]*__, from __*5*__ to __*6*__ at a cost of __*|6 - 5| = 1*__, __*s*__ becomes a magic square at the minimum possible cost. Thus, we print the cost, __*1*__, on a new line.
