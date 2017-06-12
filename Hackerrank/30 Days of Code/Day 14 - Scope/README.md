# [Day 14: Scope](https://www.hackerrank.com/challenges/30-scope)

#### Objective
Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!

The *absolute difference* between two integers, __*a*__ and __*b*__, is written as __*|a-b|*__. The *maximum absolute difference* between two integers in a set of positive integers, __*elements*__, is the largest absolute difference between any two integers in __*elements*__.

The Difference class is started for you in the editor. It has a private integer array (__*elements*__) for storing __*N*__ non-negative integers, and a public integer (__*maximumDifference*__) for storing the maximum absolute difference.

#### Task
Complete the Difference class by writing the following:
* A class constructor that takes an array of integers as a parameter and saves it to the __*elements*__ instance variable.
* A *computeDifference* method that finds the maximum absolute difference between any __*2*__ numbers in __*N*__ and stores it in the __*maximumDifference*__ instance variable.

#### Input Format
You are not responsible for reading any input from stdin. The locked *Solution* class in your editor reads in __*2*__ lines of input; the first line contains __*N*__, and the second line describes the __*elements*__ array.

#### Constraints
* __*a <= N <= 10*__
* __*1 <= elements[i] <= 100*__, where __*0 <= i <= N - 1*__

#### Output Format
You are not responsible for printing any output; the Solution class will print the value of the __*maximumDifference*__ instance variable.

#### Sample Input
```
3
1 2 5
```

#### Sample Output
```
4
```

#### Explanation
The scope of the __*elements*__ array and __*maximumDifference*__ integer is the entire class instance. The class constructor saves the argument passed to the constructor as the __*elements*__ instance variable (where the *computeDifference* method can access it).

To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any __*2*__ elements:
__*|1 - 2| = 1*__
__*|1 - 5| = 4*__
__*|2 - 5| = 3*__

The maximum of these differences is __*4*__, so it saves the value __*4*__ as the __*maximumDifference*__ instance variable. The locked stub code in the editor then prints the value stored as __*maximumDifference*__, which is __*4*__.
