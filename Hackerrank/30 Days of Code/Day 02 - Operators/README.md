# [Day 2: Operators](https://www.hackerrank.com/challenges/30-operators)

#### Objective
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Given the *meal* price (base cost of a meal), *tip* percent (the percentage of the *meal* price being added as tip), and *tax* percent (the percentage of the *meal* price being added as tax) for a meal, find and print the meal's *total* cost.

__Note:__ Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

#### Input Format
There are __*3*__ lines of numeric input:
The first line has a double, __*mealCost*__ (the cost of the *meal* before *tax* and *tip*).
The second line has an integer, __*tipPercent*__ (the percentage of __*mealCost*__ being added as *tip*).
The third line has an integer, __*taxPercent*__ (the percentage of __*mealCost*__ being added as *tax*).

#### Output Format
Print` The total meal cost is totalCost dollars.`, where __*totalCost*__ is the rounded integer result of the entire bill (__*mealCost*__ with added *tax* and *tip*).

#### Sample Input
```
12.00
20
8
```

#### Sample Output
```
The total meal cost is 15 dollars.
```

#### Explanation

###### Given:
__*mealCost = 12*__, __*tipPercent = 20*__, __*taxPercent = 8*__

###### Calculations:
__*tip = 12 x 20/100 = 2.4*__
__*tax = 12 x 8/100 = 0.96*__
__*totalCost = mealCost + tip + tax = 12 + 2.4 + 0.96 = 15.36*__
__*round(totalCost) = 15*__

We round __*totalCost*__ to the nearest dollar (integer) and then print our result:

```
The total meal cost is 15 dollars.
```
