# [Day 1: Data Types](https://www.hackerrank.com/challenges/30-data-types)

#### Objective
Today, we're discussing data types. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Complete the code in the editor below. The variables __*i*__, __*d*__, and __*s*__ are already declared and initialized for you. You must:

1. Declare __*3*__ variables: one of type int, one of type double, and one of type String.
2. Read __*3*__ lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your __*3*__ variables.
3. Use the __*+*__ operator to perform the following operations:
    1. Print the sum of __*i*__ plus your int variable on a new line.
    2. Print the sum of __*d*__ plus your double variable to a scale of one decimal place on a new line.
    3. Concatenate __*s*__ with the string you read as input and print the result on a new line.

__Note:__ If you are using a language that doesn't support using __*+*__ for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.

#### Input Format
The first line contains an integer that you must sum with __*i*__.
The second line contains a double that you must sum with __*d*__.
The third line contains a string that you must concatenate with __*s*__.

#### Output Format
Print the sum of both integers on the first line, the sum of both doubles (scaled to __*1*__ decimal place) on the second line, and then the two concatenated strings on the third line.

#### Sample Input
```
12
4.0
is the best place to learn and practice coding!
```

#### Sample Output
```
16
8.0
HackerRank is the best place to learn and practice coding!
```

#### Explanation
When we sum the integers __*4*__ and __*12*__, we get the integer __*16*__.
When we sum the floating-point numbers __*4.0*__ and __*4.0*__, we get __*8.0*__.
When we concatenate `HackerRank` with `is the best place to learn and practice coding!`, we get `HackerRank is the best place to learn and practice coding!`.

__You will not pass this challenge if you attempt to assign the Sample Case values to your variables instead of following the instructions above and reading input from stdin.__
