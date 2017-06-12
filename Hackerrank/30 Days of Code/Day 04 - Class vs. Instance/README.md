# [Day 4: Class vs. Instance](https://www.hackerrank.com/challenges/30-class-vs-instance)

#### Objective
In this challenge, we're going to learn about the difference between a class and an instance; because this is an *Object Oriented* concept, it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Write a *Person* class with an instance variable, __*age*__, and a constructor that takes an integer, __*initialAge*__, as a parameter. The constructor must assign __*initialAge*__ to __*age*__ after confirming the argument passed as __*initialAge*__ is not negative; if a negative argument is passed as __*initialAge*__, the constructor should set __*age*__ to __*0*__ and print `Age is not valid, setting age to 0.`. In addition, you must write the following instance methods:

1. *yearPasses()* should increase the __*age*__ instance variable by __*1*__.
2. *amIOld()* should perform the following conditional actions:
    * If __*age < 13*__, print `You are young.`.
    * If __*age > 13*__ and __*age < 18*__, print `You are a teenager.`.
    * Otherwise, print `You are old.`.
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

__Note:__ Do not remove or alter the stub code in the editor.

#### Input Format
Input is handled for you by the stub code in the editor.

The first line contains an integer, __*T*__ (the number of test cases), and the __*T*__ subsequent lines each contain an integer denoting the __*age*__ of a Person instance.

#### Constraints
* __*1 <= T <= 4*__
* __*-5 <= age <= 30*__

#### Output Format
Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print __*2*__ or __*3*__ lines (depending on whether or not a valid __*initialAge*__ was passed to the constructor).

#### Sample Input
```
4
-1
10
16
18
```

#### Sample Output
```
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
```

#### Explanation

###### Test Case 0: __*initialAge = -1*__
Because __*initialAge < 0*__, our code must set __*age*__ to __*0*__ and print the "Age is not valid..." message followed by the young message. Three years pass and __*age = 3*__, so we print the young message again.

###### Test Case 1: __*initialAge = 10*__
Because __*initialAge < 13*__, our code should print that the person is young. Three years pass and __*age = 13*__, so we print that the person is now a teenager.

###### Test Case 2: __*initialAge = 16*__
Because __*13 <= initialAge < 18*__, our code should print that the person is a teenager. Three years pass and __*age = 19*__, so we print that the person is old.

###### Test Case 3: __*initialAge = 18*__
Because __*initialAge >= 18*__, our code should print that the person is old. Three years pass and the person is still old at __*age = 21*__, so we print the old message again.

__The extra line at the end of the output is supposed to be there and is trimmed before being compared against the test case's expected output. If you're failing this challenge, check your logic and review your print statements for spelling errors.__
