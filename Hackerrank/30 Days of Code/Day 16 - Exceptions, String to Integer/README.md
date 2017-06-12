# [Day 16: Exceptions - String to Integer](https://www.hackerrank.com/challenges/30-exceptions-string-to-integer)

#### Objective
Today, we're getting started with Exceptions by learning how to parse an integer from a string and print a custom error message. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Read a string, __*S*__, and print its integer value; if __*S*__ cannot be converted to an integer, print `Bad String`.

__Note:__ You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a __*0*__ score.

#### Input Format
A single string, __*S*__.

#### Constraints
* __*1 <= |S| <= 5*__, where __*|S|*__ is the length of string __*S*__.
* __*S*__ is composed of *either* lowercase letters (__*a - z*__) or decimal digits (__*0-9*__).

#### Output Format
Print the parsed integer value of __*S*__, or `Bad String` if __*S*__ cannot be converted to an integer.

#### Sample Input 0
```
3
```

#### Sample Output 0
```
3
```

#### Sample Input 1
```
za
```

#### Sample Output 1
```
Bad String
```

#### Explanation
*Sample Case* __*0*__ contains an integer, so it should not raise an exception when we attempt to convert it to an integer. Thus, we print the __*3*__.
*Sample Case* __*1*__ does not contain any integers, so an attempt to convert it to an integer will raise an exception. Thus, our exception handler prints `Bad String`.
