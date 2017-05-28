# Between Two Sets

Consider two sets of positive integers, __*A = {a_0, a_1, ... , a_n-1}*__ and __*B = {b_0, b_1, ... , b_m-1}*__. We say that a positive integer, __*x*__, is between sets __*A*__ and __*B*__ if the following conditions are satisfied:

1. All elements in __*A*__ are factors of __*x*__.
2. __*x*__ is a factor of all elements in __*B*__.

In other words, some __*x*__ is between __*A*__ and __*B*__ if that value of __*x*__ satisfies __*x mod a_i = 0*__ for every __*a_i*__ in __*A*__ and also satisfies __*b_i mod x = 0*__ for every __*b_i*__ in __*B*__. For example, if __*A = {2,6}*__ and __*B = {12}*__, then our possible __*x*__ values are __*6*__ and __*12*__.

Given __*A*__ and __*B*__, find and print the number of integers (i.e., possible __*x*__'s) that are between the two sets.

#### Input Format
The first line contains two space-separated integers describing the respective values of __*n*__ (the number of elements in set __*A*__) and __*m*__ (the number of elements in set __*B*__).
The second line contains __*n*__ distinct space-separated integers describing __*a_0, a_1, ... , a_n-1*__.
The third line contains __*m*__ distinct space-separated integers describing __*b_0, b_1, ... , b_m-1*__.

#### Constraints
* __*1 <= n, m <= 10*__
* __*1 <= a_i <= 100*__
* __*1 <= b_i <= 100*__


#### Output Format
Print the number of integers that are considered to be between __*A*__ and __*B*__.

#### Sample Input
```
2 3
2 4
16 32 96
```

#### Sample Output
```
3
```

#### Explanation

There are three __*x*__ values between __*A = {2,4}*__ and __*b = {16,32,96}*__:

* __*x = 4*__:
    * All the elements in __*A*__ evenly divide __*x = 4*__.
    * __*x = 4*__ evenly divides all the elements in __*B*__.
* __*x = 8*__:
    * All the elements in __*A*__ evenly divide __*x = 8*__.
    * __*x = 8*__ evenly divides all the elements in __*B*__.
* __*x = 16*__:
    * All the elements in __*A*__ evenly divide __*x = 16*__.
    * __*x = 16*__ evenly divides all the elements in __*B*__.
    
Thus, we print __*3*__ as our answer.
