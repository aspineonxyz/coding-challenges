# A Very Big Sum

You are given an array of integers of size __*N*__. You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

#### Input Format
The first line of the input consists of an integer __*N*__. The next line contains __*N*__ space-separated integers contained in the array.

#### Output Format
Print a single value equal to the sum of the elements in the array.

#### Constraints
* __*1 <= N <= 10*__
* __*0 <= A[i] <= 10^10*__

#### Sample Input
```
5
1000000001 1000000002 1000000003 1000000004 1000000005
```

#### Output
```
5000000015
```

__Note:__

The range of the 32-bit integer is __*(-2^31)*__ to __*(2^31 - 1)*__ or __*[-2147483648, 2147483647]*__.
When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums.
