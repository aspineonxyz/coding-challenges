# Kangaroo

There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location __*x_1*__ and moves at a rate of __*v_1*__ meters per jump. The second kangaroo starts at location __*x_2*__ and moves at a rate of __*v_2*__ meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?

#### Input Format
A single line of four space-separated integers denoting the respective values of __*x_1*__, __*v_1*__, __*x_2*__, and __*v_2*__.

#### Constraints
* __*0 <= x_1 < x_2 <= 10000*__
* __*1 <= v_1 <= 10000*__
* __*1 <= v_2 <= 10000*__

#### Output Format
Print __YES__ if they can land on the same location at the same time; otherwise, print __NO__.

__Note:__ The two kangaroos must land at the same location after making the same number of jumps.

#### Sample Input 0
```
0 3 4 2
```

#### Sample Output 0
```
YES
```

#### Explanation 0
The two kangaroos jump through the following sequence of locations:
1. __*0 -> 3 -> 6 -> 9 -> 12*__
2. __*4 -> 6 -> 8 -> 10 -> 12*__
Thus, the kangaroos meet after __*4*__ jumps and we print __YES__.

#### Sample Input 1
```
0 2 5 3
```

#### Sample Output 1
```
NO
```

#### Explanation 1
The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e., __*x_2 > x_1*__). Because the second kangaroo moves at a faster rate (meaning __*v_2 > v_1*__) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. Thus, we print NO.
