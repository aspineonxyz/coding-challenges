# [Day 28: RegEx, Patterns, and Intro to Databases](https://www.hackerrank.com/challenges/30-regex-patterns)

#### Objective
Today, we're working with regular expressions. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
Consider a database table, *Emails*, which has the attributes *First Name* and *Email ID*. Given __*N*__ rows of data simulating the *Emails* table, print an alphabetically-ordered list of people whose email address ends in __*@gmail.com*__.

#### Input Format
The first line contains an integer, __*N*__, total number of rows in the table.
Each of the __*N*__ subsequent lines contains __*2*__ space-separated strings denoting a person's first name and email ID, respectively.

#### Constraints
* __*2 <= N <= 30*__
* Each of the first names consists of lower case letters __*[a - z]*__ only.
* Each of the email IDs consists of lower case letters __*[a - z]*__, __*@*__ and __*.*__ only.
* The length of the first name is no longer than 20.
* The length of the email ID is no longer than 50.

#### Output Format
Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

#### Sample Input
```
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
```

#### Sample Output
```
julia
julia
riya
samantha
tanya
```
