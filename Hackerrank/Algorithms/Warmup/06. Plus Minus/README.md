# [Plus Minus](https://www.hackerrank.com/challenges/plus-minus)

Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to __*10^-4*__ are acceptable.

#### Input Format
The first line contains an integer, __*N*__, denoting the size of the array.
The second line contains __*N*__ space-separated integers describing an array of numbers __*(a_0, a_1, a_2, ... , a_n-1)*__.

#### Output Format

You must print the following __*3*__ lines:
1. A decimal representing of the fraction of positive numbers in the array compared to its size.
2. A decimal representing of the fraction of negative numbers in the array compared to its size.
3. A decimal representing of the fraction of zeroes in the array compared to its size.

#### Sample Input
```
6
-4 3 -9 0 4 1         
```
#### Sample Output
```
0.500000
0.333333
0.166667
```

#### Explanation

There are __*3*__ positive numbers, __*2*__ negative numbers, and __*1*__ zero in the array.
The respective fractions of positive numbers, negative numbers and zeroes are __*3/6 = 0.500000*__, __*2/6 = 0.333333*__ and __*1/6 = 0.166667*__, respectively.
