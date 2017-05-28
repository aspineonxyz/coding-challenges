# Arrays - DS

An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, __*A*__, of size __*N*__, each memory location has some unique index, __*i*__ (where __*0 <= i <= N*__), that can be referenced as __*A[i]*__ (you may also see it written as __*A_i*__).

Given an array, __*A*__, of __*N*__ integers, print each element in reverse order as a single line of space-separated integers.

__Note:__ If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

#### Input Format
The first line contains an integer, __*N*__ (the number of integers in __*A*__). 
The second line contains __*N*__ space-separated integers describing __*A*__.

#### Constraints
* __*1 <= N <= 10^3*__
* __*1 <= A_i <= 10^4*__, where __*A_i*__ is the __*i^th*__ integer in __*A*__.

#### Output Format
Print all __*N*__ integers in __*A*__ in reverse order as a single line of space-separated integers.

#### Sample Input
````
4
1 4 3 2
````
#### Sample Output
```
2 3 4 1
```