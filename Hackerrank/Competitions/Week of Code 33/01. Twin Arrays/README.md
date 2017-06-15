# [Twin Arrays](https://www.hackerrank.com/contests/w33/challenges/twin-arrays)

You are given two arrays __*A*__ and __*B*__ each containing __*n*__ integers. You need to choose exactly __*one*__ number from __*A*__ and exactly __*one*__ number from __*B*__ such that the index of the two chosen numbers is not same and the sum of the 2 chosen values is minimum.

Your objective is to find and print this minimum value.

For example in the image shown below __1 + 6*__ is the minimum sum.

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Competitions/Week%20of%20Code%2033/01.%20Twin%20Arrays/img/twin-arrays-1.jpg" alt="twin-arrays-1">
</p>

#### Input Format
The first line contains an integer __*n*__ denoting the size of two arrays.
Each of the next two lines contains __*n*__ space separated integers denoting array __*A*__ and __*B*__ respectively.

#### Constraints
* __*2 <= n <= 10^5*__
* __*1 <= array elements <= 10^5*__

#### Output Format
Print the minimum sum which can be obtained under the conditions mentioned in the problem statement.

#### Sample Input 0
```
5
5 4 3 2 1
1 2 3 4 5
```

#### Sample Output 0
```
2
```

#### Explanation 0
Minimum sum will be obtained by choosing number at the last index of first array and first index of the second array, i.e. __*2*__.
