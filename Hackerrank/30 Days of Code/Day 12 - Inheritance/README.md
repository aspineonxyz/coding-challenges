# [Day 12: Inheritance](https://www.hackerrank.com/challenges/30-inheritance)

#### Objective
Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
You are given two classes, *Person* and *Student*, where *Person* is the base class and *Student* is the derived class. Completed code for *Person* and a declaration for *Student* are provided for you in the editor. Observe that *Student* inherits all the properties of *Person*.

Complete the *Student* class by writing the following:

* A *Student* class constructor, which has __*4*__ parameters:
    1. A string, __*firstName*__.
    2. A string, __*lastName*__.
    3. An integer, __*id*__.
    4. An integer array (or vector) of test scores, __*scores*__.
* A char *calculate()* method that calculates a *Student* object's average and returns the grade character representative of their calculated average:

<p align="center">
    <img src="" alt="inheritance">
</p>

#### Input Format
The locked stub code in your editor calls your *Student* class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin:
The first line contains __*firstName*__, __*lastName*__, and __*id*__, respectively. The second line contains the number of test scores. The third line of space-separated integers describes __*scores*__.

#### Constraints
* __*1 <= |firstName|, |lastName| < 10*__
* __*|id| ≡ 7*__
* __*0 <= score, average <= 100*__

#### Output Format
This is handled by the locked stub code in your editor. Your output will be correct if your *Student* class constructor and *calculate()* method are properly implemented.

#### Sample Input
```
Heraldo Memelli 8135627
2
100 80
```

#### Sample Output
```
Name: Memelli, Heraldo
ID: 8135627
Grade: O
```

#### Explanation
This *Student* had __*2*__ scores to average: __*100*__ and __*80*__.  The student's average grade is __*(100 + 80)/2 = 90*__. An average grade of __*90*__ corresponds to the letter grade __*O*__, so our *calculate()* method should return the character `'O'`.
