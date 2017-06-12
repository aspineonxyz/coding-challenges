# [Day 29: Bitwise AND](https://www.hackerrank.com/challenges/30-bitwise-and)

#### Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Given set __*S = {1,2,3,...,N}*__. Find two integers, __*A*__ and __*B*__ (where __*A < B*__), from set __*S*__ such that the value of __*A & B*__ is the maximum possible and also less than a given integer, __*K*__. In this case, __*&*__ represents the bitwise AND operator.

#### Input Format
The first line contains an integer, __*T*__, the number of test cases.
Each of the __*T*__ subsequent lines defines a test case as __*2*__ space-separated integers, __*N*__ and __*K*__, respectively.

#### Constraints
* __*1 <= T <= 10^3*__
* __*2 <= N <= 10^3*__
* __*2 <= K <= N*__

#### Output Format
For each test case, print the maximum possible value of __*A & B*__ on a new line.

#### Sample Input
```
3
5 2
8 5
2 2
```

#### Sample Output
```
1
4
0
```

#### Explanation
__*N = 5, K = 2 S = {1,2,3,4,5}*__
All possible values of __*A*__ and __*B*__ are:
1. __*A = 1, B = 2, A & B = 0*__
2. __*A = 1, B = 3, A & B = 1*__
3. __*A = 1, B = 4, A & B = 0*__
4. __*A = 1, B = 5, A & B = 1*__
5. __*A = 2, B = 3, A & B = 2*__
6. __*A = 2, B = 4, A & B = 0*__
7. __*A = 2, B = 5, A & B = 0*__
8. __*A = 3, B = 4, A & B = 0*__
9. __*A = 3, B = 5, A & B = 1*__
10. __*A = 4, B = 5, A & B = 4*__
The maximum possible value of __*A & B*__ that is also __*< (K = 2)*__ is __*1*__, so we print __*1*__ on a new line.
