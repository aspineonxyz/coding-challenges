# [Day 26: Nested Logic](https://www.hackerrank.com/challenges/30-nested-logic/submissions/code/36350398)

#### Objective
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing!

#### Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: __*fine = 0*__.
2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, __*fine = 15 Hackos x (the number of days late)*__.
3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the __*fine = 500 Hackos x (the number of months late)*__.
4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of __*10000 Hackos*__.

#### Input Format
The first line contains __*3*__ space-separated integers denoting the respective __*day*__, __*month*__, and __*year*__ on which the book was actually returned.
The second line contains __*3*__ space-separated integers denoting the respective __*day*__, __*month*__, and __*year*__ on which the book was expected to be returned (due date).

#### Constraints
* __*1 <= D <= 31*__
* __*1 <= M <= 12*__
* __*1 <= Y <= 3000*__
* __*It is guaranteed that the dates will be valid Gregorian calendar dates.*__

#### Output Format
Print a single integer denoting the library fine for the book received as input.

#### Sample Input
```
9 6 2015
6 6 2015
```

#### Sample Output
```
45
```

#### Explanation
Given the following return dates:
Actual: __*D_a = 9, M_a = 6, Y_a = 2015*__
Expected: __*D_e = 6, M_e = 6, Y_e = 2015*__

Because __*Y_e ≡ Y_a*__, we know it is less than a year late.
Because __*M_e ≡ M_a*__, we know it's less than a month late.
Because __*D_e ≡ D_a*__, we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be __*15 HAckos x (# days late)*__. We then print the result of __*15 x (D_a - D_e) = 15 x (9 - 6) = 45*__ as our output.
