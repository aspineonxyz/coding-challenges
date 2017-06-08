# [Grading Students](https://www.hackerrank.com/challenges/grading)

HackerLand University has the following grading policy:
* Every student receives a __*grade*__ in the inclusive range from __*0*__ to __*100*__.
* Any __*grade*__ less than __*40*__ is a failing grade.

Sam is a professor at the university and likes to round each student's __*grade*__ according to these rules:
* If the difference between the __*grade*__ and the next multiple of __*5*__ is less than __*3*__, round __*grade*__ up to the next multiple of __*5*__.
* If the value of the __*grade*__ is less than __*38*__, no rounding occurs as the result will still be a failing grade.

For example, __*grade = 84*__ will be rounded to __*85*__ but __*grade = 29*__ will not be rounded because the rounding would result in a number that is less than __*40*__.

Given the initial value of __*grade*__ for each of Sam's __*n*__ students, write code to automate the rounding process. For each __*grade*__, round it according to the rules above and print the result on a new line.

#### Input Format
The first line contains a single integer denoting __*n*__ (the number of students).
Each line __*i*__ of the __*n*__ subsequent lines contains a single integer, __*grade*__, denoting student __*i*__'s grade.

#### Constraints
* __*1 <= n <= 60*__
* __*0 <= grade <= 100*__

#### Output Format
For each __*grade*__, of the __*n*__ grades, print the rounded grade on a newline.

#### Sample Input 0
```
4
73
67
38
33
```

#### Sample Output 0
```
75
67
40
33
```

#### Explanation 0
<p align="center">
  <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/01.%20Grading%20Students/img/grading-students-1.png" alt="grades">
</p>

1. Student __*1*__ received a __*73*__, and the next multiple of __*5*__ from __*73*__ is __*75*__. Since __*75 - 73 < 3*__, the student's grade is rounded to __*75*__.
2. Student __*2*__ received a __*67*__, and the next multiple of __*5*__ from __*67*__ is __*70*__. Since __*70 - 67 = 3*__, the grade will not be modified and the student's final grade is __*67*__.
3. Student __*3*__ received a __*38*__, and the next multiple of __*5*__ from __*38*__ is __*40*__. Since __*40 - 38 < 3*__, the student's grade will be rounded to __*40*__.
4. Student __*4*__ received a grade below __*38*__, so the grade will not be modified and the student's final grade is __*33*__.
