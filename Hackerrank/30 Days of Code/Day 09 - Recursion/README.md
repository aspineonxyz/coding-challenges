# [Day 9: Recursion](https://www.hackerrank.com/challenges/30-recursion)

#### Objective
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

#### Recursive Method for Calculating Factorial

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/30%20Days%20of%20Code/Day%2009%20-%20Recursion/img/day-9-recursion.png" alt="recursion">
</p>

#### Task
Write a factorial function that takes a positive integer, __*N*__ as a parameter and prints the result of __*N!*__ (__*N*__ factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of __*0*__.

#### Input Format
A single integer, __*N*__ (the argument to pass to factorial).

#### Constraints
* __*2 <= N <= 12*__
* Your submission must contain a recursive function named factorial.

#### Output Format
Print a single integer denoting __*N!*__.

#### Sample Input
```
3
```

#### Sample Output
```
6
```

#### Explanation

Consider the following steps:
1. __*factorial(3) = 3 x factorial(2)*__
2. __*factorial(2) = 2 x factorial(1)*__
3. __*factorial(1) = 1*__

From steps __*2*__ and __*3*__, we can say __*factorial(2) = 2 x 1*__; then when we apply the value from __*factorial(2)*__ to step __*1*__, we get __*factorial(3) = 3 x 2 x 1 = 6*__. Thus, we print __*6*__ as our answer.
