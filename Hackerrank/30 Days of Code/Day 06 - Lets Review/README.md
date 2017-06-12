# [Day 6: Let's Review](https://www.hackerrank.com/challenges/30-review-loop)

#### Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Given a string, __*S*__, of length __*N*__ that is indexed from __*0*__ to __*N - 1*__, print its *even-indexed* and *odd-indexed* characters as __*2*__ space-separated strings on a single line (see the *Sample* below for more detail).

__Note:__ __*0*__ is considered to be an even index.

#### Input Format
The first line contains an integer, __*T*__ (the number of test cases).
Each line __*i*__ of the __*T*__ subsequent lines contain a String, __*S*__.

#### Constraints
* __* 1 <= T <= 10*__
* __* 2 <= length of S <= 10000*__

#### Output Format
For each String __*S_j*__ (where __*0 <= j <= T - 1*__), print __*S_j*__'s even-indexed characters, followed by a space, followed by __*S_j*__'s odd-indexed characters.

#### Sample Input
```
2
Hacker
Rank
```

#### Sample Output
```
Hce akr
Rn ak
```

#### Explanation

###### Test Case 0:  __*S = "Hacker"*__
__*S[0] = "H"*__
__*S[1] = "a"*__
__*S[2] = "c"*__
__*S[3] = "k"*__
__*S[4] = "e"*__
__*S[5] = "r"*__
The *even* indices are __*0*__, __*2*__, and __*4*__, and the *odd* indices are __*1*__, __*3*__, and __*5*__. We then print a single line of __*2*__ space-separated strings; the first string contains the ordered characters from __*S*__'s even indices (__*Hce*__), and the second string contains the ordered characters from __*S*__'s odd indices (__*akr*__).

###### Test Case 1: __*S = "Rank"*__  
__*S[0] = "R"*__
__*S[1] = "a"*__
__*S[2] = "n"*__
__*S[3] = "k"*__
The *even* indices are __*0*__ and __*2*__, and the *odd* indices are __*1*__ and __*3*__. We then print a single line of __*2*__ space-separated strings; the first string contains the ordered characters from __*S*__'s even indices (__*Rn*__), and the second string contains the ordered characters from __*S*__'s odd indices (__*ak*__).
