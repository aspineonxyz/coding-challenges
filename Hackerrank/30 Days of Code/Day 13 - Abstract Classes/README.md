# [Day 13: Abstract Classes](https://www.hackerrank.com/challenges/30-abstract-classes)

#### Objective
Today, we're taking what we learned yesterday about [Inheritance](https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html) and extending it to [Abstract Classes](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html). Because this is a very specific Object-Oriented concept, submissions are limited to the few languages that use this construct. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Given a Book class and a *Solution* class, write a *MyBook* class that does the following:
* Inherits from *Book*
* Has a parameterized constructor taking these __*3*__ parameters:
    1. string __*title*__
    2. string __*author*__
    3. int __*price*__
* Implements the *Book* class' abstract *display()* method so it prints these __*3*__ lines:
    1. __*Title*__, a space, and then the current instance's __*title*__.
    2. __*Author*__, a space, and then the current instance's __*author*__.
    3. __*Price*__, a space, and then the current instance's __*price*__.
__Note:__ Because these classes are being written in the same file, you must not use an access modifier (e.g.: __*price*__) when declaring *MyBook* or your code will not execute.

#### Input Format
You are not responsible for reading any input from stdin. The *Solution* class creates a Book object and calls the *MyBook* class constructor (passing it the necessary arguments). It then calls the display method on the *Book* object.

#### Output Format
The __*void display()*__ method should print and label the respective __*title*__, __*author*__, and __*price*__ of the MyBook object's instance (with each value on its own line) like so:
```
Title: $title
Author: $author
Price: $price
```
__Note:__ The __*$*__ is prepended to variable names to indicate they are placeholders for variables.

#### Sample Input
The following input from stdin is handled by the locked stub code in your editor:
```
The Alchemist
Paulo Coelho
248
```

#### Sample Output
The following output is printed by your __*display()*__ method:
```
Title: The Alchemist
Author: Paulo Coelho
Price: 248
```   
