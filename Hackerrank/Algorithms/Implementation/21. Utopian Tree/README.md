# [Utopian Tree](https://www.hackerrank.com/challenges/utopian-tree){:target="_blank"}
# <a href="www.hackerrank.com/challenges/utopian-tree" target="_blank">Utopian Tree</a>

The Utopian Tree goes through __*2*__ cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by __*1*__ meter.

Laura plants a Utopian Tree sapling with a height of __*1*__ meter at the onset of spring. How tall will her tree be after __*N*__ growth cycles?

#### Input Format
The first line contains an integer, __*T*__, the number of test cases.
__*T*__ subsequent lines each contain an integer, __*N*__, denoting the number of cycles for that test case.

#### Constraints
* __*1 <= T <= 10*__
* __*0 <= N <= 60*__

#### Output Format
For each test case, print the height of the Utopian Tree after __*N*__ cycles. Each height must be printed on a new line.

#### Sample Input
```
3
0
1
4
```

#### Sample Output
```
1
2
7
```

#### Explanation
There are __*3*__ test cases.

In the first case (__*N = 0*__), the initial height (__*H = 1*__) of the tree remains unchanged.

In the second case (__*N = 1*__), the tree doubles in height and is __*2*__ meters tall after the spring cycle.

In the third case (__*N = 4*__), the tree doubles its height in spring (__*H = 2*__), then grows a meter in summer (__*H = 3*__), then doubles after the next spring (__*H = 6*__), and grows another meter after summer (__*H = 7*__). Thus, at the end of __*4*__ cycles, its height is __*7*__ meters.
