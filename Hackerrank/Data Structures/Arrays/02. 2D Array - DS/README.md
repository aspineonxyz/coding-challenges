# 2D Array - DS

#### Context 
Given a __*6 x 6*__ 2D Array, __*A*__:
```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
We define an hourglass in __*A*__ to be a subset of values with indices falling in this pattern in __*A*__'s graphical representation:
```
a b c
  d
e f g
```
There are __*16*__ hourglasses in __*A*__, and an hourglass sum is the sum of an hourglass' values.

#### Task 
Calculate the hourglass sum for every hourglass in __*A*__, then print the maximum hourglass sum.

__Note:__ If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

#### Input Format
There are __*6*__ lines of input, where each line contains __*6*__ space-separated integers describing 2D Array __*A*__; every value in __*A*__ will be in the inclusive range of __*-9*__ to __*9*__.

#### Constraints
* __*-9 <= A[i][j] <= 9*__
* __*0 <= i,j <= 5*__

#### Output Format
Print the largest (maximum) hourglass sum found in __*A*__.

#### Sample Input
```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```

#### Sample Output
```
19
```

#### Explanation
__*A*__ contains the following hourglasses:
```
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
```
The hourglass with the maximum sum (__*19*__) is:
```
2 4 4
  2
1 2 4
```