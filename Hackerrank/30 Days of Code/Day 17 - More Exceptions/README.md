# [Day 17: More Exceptions](https://www.hackerrank.com/challenges/30-more-exceptions)

#### Objective
Yesterday's challenge taught you to manage exceptional situations by using try and catch blocks. In today's challenge, you're going to practice throwing and propagating an exception. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Write a *Calculator* class with a single method: int power(*int*,*int*). The power method takes two integers, __*n*__ and __*p*__, as parameters and returns the integer result of __*n^p*__. If either __*n*__ or __*p*__ is negative, then the method must throw an exception with the message: `n and p should be non-negative`.

__Note:__ Do not use an access modifier (e.g.: public) in the declaration for your *Calculator* class.

#### Input Format
Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer, __*T*__, the number of test cases. Each of the __*T*__ subsequent lines describes a test case in __*2*__ space-separated integers denoting __*n*__ and __*p*__, respectively.

#### Constraints
* No Test Case will result in overflow for correctly written code.
Output Format.

Output to stdout is handled for you by the locked stub code in your editor. There are __*T*__ lines of output, where each line contains the result of __*n^p*__ as calculated by your *Calculator* class' power method.

#### Sample Input
```
4
3 5
2 4
-1 -2
-1 3
```

#### Sample Output
```
243
16
n and p should be non-negative
n and p should be non-negative
```

#### Explanation
__*T = 4*__
__*T_0*__: __*3*__ and __*5*__ are positive, so power returns the result of __*3^5*__, which is __*243*__.
__*T_1*__: __*2*__ and __*3*__ are positive, so power returns the result of __*2^4*__, which is __*16*__.
__*T_2*__: Both inputs (__*-1*__ and __*-2*__) are negative, so power throws an exception and __*n and p should be non-negative*__ is printed.
__*T_3*__: One of the inputs (__*-1*__) is negative, so *power* throws an exception and __*n and p should be non-negative*__ is printed.
