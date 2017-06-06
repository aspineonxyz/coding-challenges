# Apple and Orange

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where __*s*__ is the start point __*t*__ and  is the end point. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point __*a*__ and the orange tree is at point __*b*__.

![apple-and-orange-1](https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/02.%20Apple%20and%20Orange/img/apple-and-orange-1.png)

When a fruit falls from its tree, it lands __*d*__ units of distance from its tree of origin along the __*x*__-axis. A negative value of __*d*__ means the fruit fell __*d*__ units to the tree's left, and a positive value of __*d*__ means it falls __*d*__ units to the tree's right.

Given the value of __*d*__ for __*m*__ apples and __*n*__ oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [__*s*__, __*t*__])? Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your second line of output.

#### Input Format

* The first line contains two space-separated integers denoting the respective values of __*s*__ and __*t*__.
* The second line contains two space-separated integers denoting the respective values of __*a*__ and __*b*__.
* The third line contains two space-separated integers denoting the respective values of __*m*__ and __*n*__.
* The fourth line contains __*m*__ space-separated integers denoting the respective distances that each apple falls from point __*a*__.
* The fifth line contains __*n*__ space-separated integers denoting the respective distances that each orange falls from point __*b*__.

#### Constraints
* __*1 <= s, t, a, b, m, n <= 10^5*__
* __*-10^5 <= d <= 10^5*__
* __*a < s< t < b*__

#### Output Format
Print two lines of output:
1. On the first line, print the number of apples that fall on Sam's house.
2. On the second line, print the number of oranges that fall on Sam's house.

#### Sample Input 0
```
7 11
5 15
3 2
-2 2 1
5 -6
```

#### Sample Output 0
```
1
1
```

#### Explanation 0
The first apple falls at position __*5 - 2 = 3*__. 
The second apple falls at position __*5 + 2 = 7*__. 
The third apple falls at position __*5 + 1 = 6*__. 
The first orange falls at position __*15 + 5 = 20*__. 
The second orange falls at position __*15 - 6 = 9*__. 
Only one fruit (the second apple) falls within the region between __*7*__ and __*11*__, so we print __*1*__ as our first line of output. 
Only the second orange falls within the region between __*7*__ and __*11*__, so we print 1 as our second line of output.

