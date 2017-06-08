# [Migratory Birds](https://www.hackerrank.com/challenges/migratory-birds)

A flock of __*n*__ birds is flying across the continent. Each bird has a type, and the different types are designated by the ID numbers __*1*__, __*2*__, __*3*__, __*4*__, and __*5*__.

Given an array of __*n*__ integers where each integer describes the type of a bird in the flock, find and print the type number of the most common bird. If two or more types of birds are equally common, choose the type with the smallest ID number.

#### Input Format
The first line contains an integer denoting __*n*__ (the number of birds).
The second line contains __*n*__ space-separated integers describing the respective type numbers of each bird in the flock.

#### Constraints
* __*5 <= n <= 2 x 10^5*__
* It is guaranteed that each type is __*1*__, __*2*__, __*3*__, __*4*__, or __*5*__.

#### Output Format
Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.

#### Sample Input 0
```
6
1 4 4 4 5 3
```

#### Sample Output 0
```
4
```

#### Explanation 0
The different types of birds occur in the following frequencies:

* Type __*1*__: __*1*__  bird
* Type __*2*__: __*0*__  birds
* Type __*3*__: __*1*__  bird
* Type __*4*__: __*3*__  birds
* Type __*5*__: __*1*__  bird

The type number that occurs at the highest frequency is type __*4*__, so we print __*4*__ as our answer.
