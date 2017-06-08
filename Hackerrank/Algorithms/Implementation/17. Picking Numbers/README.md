# [Picking Numbers](https://www.hackerrank.com/challenges/picking-numbers)

Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is __*<= 1*__.

#### Input Format
The first line contains a single integer, __*n*__, denoting the size of the array.
The second line contains __*n*__ space-separated integers describing the respective values of __*a_0, a_1, ... , a_n-1*__.

#### Constraints
* __*2 <= n <= 100*__
* __*0 < a_i < 100*__
* The answer will be __* >= 2*__.

#### Output Format
A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is __*<= 1*__.

#### Sample Input 0
```
6
4 6 5 3 3 1
```

#### Sample Output 0
```
3
```

#### Explanation 0
We choose the following multiset of integers from the array: __*{4, 3, 3}*__. Each pair in the multiset has an absolute difference __*<= 1*__ (i.e., __*|4 - 3| = 1*__ and __*|3 - 3| = 1*__), so we print the number of chosen integers, __*3*__, as our answer.

#### Sample Input 1
```
6
1 2 2 3 1 2
```

#### Sample Output 1
```
5
```

#### Explanation 1
We choose the following multiset of integers from the array: __*{1, 2, 2, 1, 2}*__. Each pair in the multiset has an absolute difference __*<= 1*__ (i.e., __*|1 - 2| = 1*__, __*|1 - 1| = 0*__, and __*|2 - 2| = 0*__), so we print the number of chosen integers, __*5*__, as our answer.
