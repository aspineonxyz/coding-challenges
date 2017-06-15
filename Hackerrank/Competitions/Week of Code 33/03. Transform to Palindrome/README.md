<!-- # [Transform to Palindrome](https://www.hackerrank.com/contests/w33/challenges/transform-to-palindrome)

The Orion alphabet system consists of __*n*__ letters, denoted by the integers from __*1*__ to __*n*__. The __*i^th*__ Orion letter is denoted by the integer __*i*__.

Some Orion letters can be transformed to other Orion letters. A transformation is denoted by a pair of two Orion letters, __*x -> y*__. Using this transformation, you can replace letter __*x*__ with letter __*y*__.

Transformations also have additional properties:
1. If letter __*x*__ can be transformed to letter __*y*__ using a transformation, then letter __*y*__ can be transformed to letter __*x*__ as well.
2. If letter __*x*__ can be transformed to letter __*y*__ and letter __*y*__ can be transformed to letter __*z*__, then letter __*x*__ can be transformed to letter __*z*__ as well.

You are given a sequence __*S*__ comprising of __*m*__ Orion letters. You are given __*k*__ transformations that can be applied to __*S*__. You may apply transformations to zero or more letters in the sequence. When a transformation is applied to a letter, the other letters of the string remain unaffected. You can also apply a single transformation multiple times on the same sequence.

Print the length of the *longest possible palindromic subsequence* after applying zero or more transformations on the letters of the given sequence.

For example, in the sequence below, transformation __*4 -> 3*__ is first applied to the sequence __*1 4 5 9 3 1*__ to obtain __*1 3 5 9 3 1*__. The *longest palindrome subsequence* is then obtained from the resulting transformed sequence by removing letter __*9*__.

<p align="center">
    <img src="" alt="transform-to-palindrome">
</p>

#### Input Format
The first line contains three space separated integers __*n*__, __*k*__ and __*m*__. The following __*k*__ lines each contain two space separated integers __*x*__ and __*y*__, denoting a transformation from letter __*x*__ to letter __*y*__. The last line contains __*m*__ positive integers (elements of the string).

#### Constraints
* __*1 <= n <= 10^5*__
* __*1 <= k <= 10^*6__
* __*1 <= m <= 10^*_3_
* __*1 <= x,y <= n*__
* __*1 <= S_i <= n*__

#### Output Format
Print a single line containing an integer denoting the length of the *longest possible palindromic subsequence* which can be obtained after applying transformations on the given string.

#### Sample Input 0
```
10 7 6
1 3
5 7
3 5
2 6
2 4
8 4
10 9
1 9 2 3 10 3
```

#### Sample Output 0
```
5
```

#### Explanation 0
The given string is __*1 9 2 3 10 3*__. After transforming the last letter from __*3*__ to __*1*__, string becomes __*1 9 2 3 10 1*__. After transforming __*10*__ to __*9*__, string becomes __*1 9 2 3 9 1*__. One of the longest palindromic subsequence is formed as follows __*1 9 2 _ 9 1*__.

#### Sample Input 1
```
10 8 15
1 2
1 3
2 7
3 1
4 5
6 8
9 6
10 5
1 4 5 7 9 8 1 3 10 4 5 10 2 7 8
```

#### Sample Output 1
```
10
```

#### Explanation 1
After performing various transformations, the following string can be obtained __*1 4 4 1 6 6 2 1 10 5 4 4 3 1 8*__. One of the longest palindromic subsequence is __*1 4 4 1 6 6 _ 1 _ _ 4 4 _ 1 _*__. -->
