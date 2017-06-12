# [Day 25: Running Time and Complexity](https://www.hackerrank.com/challenges/30-running-time-and-complexity)

#### Objective
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

#### Task
A *prime* is a natural number greater than __*1*__ that has no positive divisors other than __*1*__ and itself. Given a number, __*n*__, determine and print whether it's __*Prime*__ or __*Not prime*__.

__Note:__ If possible, try to come up with a __*O(√N)*__ primality algorithm, or see what sort of optimizations you come up with for an __*O(n)*__ algorithm. Be sure to check out the *Editorial* after submitting your code!

#### Input Format
The first line contains an integer, __*T*__, the number of test cases.
Each of the __*T*__ subsequent lines contains an integer, __*n*__, to be tested for primality.

#### Constraints
* __*1 <= T <= 30*__
* __*1 <= n <= 2 x 10^9*__

#### Output Format
For each test case, print whether __*n*__ is __*Prime*__ or __*Not prime*__ on a new line.

#### Sample Input
```
3
12
5
7
```

#### Sample Output
```
Not prime
Prime
Prime
```

#### Explanation

###### Test Case 0: __*n = 12*__.
__*12*__ is divisible by numbers other than __*1*__ and itself (i.e.: __*2*__, __*3*__, __*6*__), so we print __*Not prime*__ on a new line.

###### Test Case 1: __*n = 5*__.
__*5*__ is only divisible __*1*__ and itself, so we print __*Prime*__ on a new line.

###### Test Case 2: __*n = 7*__.
__*7*__ is only divisible __*1*__ and itself, so we print __*Prime*__ on a new line.
