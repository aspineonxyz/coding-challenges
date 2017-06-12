# [Day 27: Testing](https://www.hackerrank.com/challenges/30-testing)

#### Objective
This challenge is very different from the others we've completed because it requires you to generate a valid test case for a problem instead of solving the problem. There is no input to read, you simply have to generate and print test values for the problem that satisfy both the problem's Input Format and the criteria laid out in the Task section. Check out the Tutorial tab for an instructional video on testing!

Consider the following problem (but do not solve it):

#### Problem Statement
A Discrete Mathematics professor has a class of __*n*__ students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than __*k*__ students are present when class starts. Given the arrival time of each student, determine if the class is canceled.

#### Input Format
The first line of input contains __*t*__, the number of lectures.
The information for each lecture spans two lines. The first line has two space-separated integers, __*n*__ (the number of students in the class) and __*k*__ (the cancelation threshold). The second line contains __*n*__ space-separated integers describing the array of students' arrival times (__*A = a_0, a_1, ... , a_n-1*__).

__Note:__ Non-positive arrival times (__*a_i <= 0*__) indicate the student arrived early or on time; positive arrival times (__*a_i > 0*__) indicate the student arrived __*a_i*__ minutes late. If a student arrives exactly on time __*a_i = 0*__, the student is considered to have entered before the class started.

#### Output Format
For each test case, print the word `YES` if the class is canceled or `NO` if it is not.

#### Example
When properly solved, this input:
```
2
4 3
-1 -3 4 2
4 2
0 -1 2 1
```
Produces this output:
```
YES
NO
```
For the first test case, __*k = 3*__. The professor wants at least __*3*__ students in attendance, but only __*2*__ arrive on time (__*-3*__ and __*-1*__). Thus, the class is canceled.

For the second test case, __*k = 2*__. The professor wants at least __*2*__ students in attendance, and do arrive on time (__*0*__ and __*-1*__). Thus, the class is *not* canceled.

#### Task
Create and print a test case for the problem above that meet the following criteria:
* __*t <= 5*__
* __*3 <= n <= 200*__
* __*1 <= k <= n*__
* __*-10^3 <= a_i <=10^3*__, where __*i ϵ [1,n]*__
* The value of __*n*__ must be distinct across all the test cases.
* Array __*A*__ must have at least __*1*__ zero, __*1*__ positive integer, and __*1*__ negative integer.

#### Scoring
If you submit __*x*__ correct test cases, you will earn __*(20 · x)%*__ of the maximum score. You must submit __*5*__ test cases to earn the maximum possible score.

#### Input Format
You are not responsible for reading anything from stdin.

#### Output Format
Print __*11*__ lines of output that can be read by the Professor challenge as valid input. Your test case must result in the following output when fed as input to the Professor challenge's solution:
```
YES
NO
YES
NO
YES
```

#### Explanation
Your code must print lines of output that follow the *Input Format* in the Professor challenge above. For example, this partial solution to this challenge:
```
print('2')
print('4 3')
print('-1 -3 4 2')
print('5 2')
print('0 -1 2 1 4')
```
prints the following output that can be used as valid input for the Professor challenge:
```
2
4 3
-1 -3 4 2
5 2
0 -1 2 1 4
```
When read by a valid solution to the Professor challenge, it produces the following output:
```
YES
NO
```
You must do something similar to this, except that the test case you develop must meet the constraints set in the *Task* section above.
