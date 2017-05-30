# Cats and a Mouse

Two cats named __*A*__ and __*B*__ are standing at integral points on the x-axis. Cat __*A*__ is standing at point __*x*__ and cat __*B*__ is standing at point __*y*__. Both cats run at the same speed, and they want to catch a mouse named __*C*__ that's hiding at integral point __*z*__ on the x-axis. Can you determine who will catch the mouse?

You are given __*q*__ queries in the form of __*x*__, __*y*__, and __*z*__. For each query, print the appropriate answer on a new line:

* If cat __*A*__ catches the mouse first, print `Cat A`.
* If cat __*B*__ catches the mouse first, print `Cat B`.
* If both cats reach the mouse at the same time, print `Mouse C` as the two cats fight and mouse escapes.

#### Input Format
The first line contains a single integer, __*q*__, denoting the number of queries.
Each of the __*q*__ subsequent lines contains three space-separated integers describing the respective values of __*x*__ (cat __*A*__'s location), __*y*__ (cat __*B*__'s location), and __*z*__ (mouse __*C*__'s location).

#### Constraints
* __*1 <= q <= 100*__
* __*1 <= x, y, z <= 100*__

#### Output Format
On a new line for each query, print `Cat A` if cat __*A*__ catches the mouse first, `Cat B` if cat __*B*__ catches the mouse first, or `Mouse C` if the mouse escapes.

#### Sample Input 0
```
3
1 2 3
1 3 2
2 1 3
```

#### Sample Output 0
```
Cat B
Mouse C
Cat A
```

#### Explanation 0
*Query 0:* The positions of the cats and mouse are shown below:

<p align="center">
    <img src="" alt="cat-and-a-mouse-1">
</p>

Cat  will catch the mouse first, so we print Cat B on a new line.

*Query 1:* In this query, cats __*A*__ and __*B*__ reach mouse __*C*__ at the exact same time:

<p align="center">
    <img src="" alt="cat-and-a-mouse-2">
</p>

Because the mouse escapes, we print `Mouse C` on a new line.
