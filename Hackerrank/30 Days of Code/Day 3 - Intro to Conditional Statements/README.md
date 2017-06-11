# [Day 3: Intro to Conditional Statements](https://www.hackerrank.com/challenges/30-conditional-statements)

#### Objective
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Given an integer, __*n*__, perform the following conditional actions:

* If __*n*__ is odd, print `Weird`
* If __*n*__ is even and in the inclusive range of __*2*__ to __*5*__, print `Not Weird`
* If __*n*__ is even and in the inclusive range of __*6*__ to __*20*__, print `Weird`
* If __*n*__ is even and greater than __*20*__, print `Not Weird`
Complete the stub code provided in your editor to print whether or not __*n*__ is weird.

#### Input Format
A single line containing a positive integer, __*n*__.

#### Constraints
* __*1 <= n <= 100*__

#### Output Format

Print `Weird` if the number is weird; otherwise, print `Not Weird`.

#### Sample Input 0
```
3
```

#### Sample Output 0
```
Weird
```

#### Sample Input 1
```
24
```

#### Sample Output 1
```
Not Weird
```

#### Explanation

###### Sample Case 0: __*n = 3*__
__*n*__ is odd and odd numbers are weird, so we print `Weird`.

###### Sample Case 1: __*n = 24*__
__*n > 20*__ and __*n*__ is even, so it isn't weird. Thus, we print `Not Weird`.
