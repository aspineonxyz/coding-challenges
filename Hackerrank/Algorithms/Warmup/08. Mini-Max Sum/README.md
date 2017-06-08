# [Mini-Max Sum](https://www.hackerrank.com/challenges/mini-max-sum)

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#### Input Format

A single line of five space-separated integers.

#### Constraints

Each integer is in the inclusive range __*[1, 10^9]*__.

#### Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

#### Sample Input
```
1 2 3 4 5
```

#### Sample Output
```
10 14
```

#### Explanation
Our initial numbers are __*1*__, __*2*__, __*3*__, __*4*__, and __*5*__. We can calculate the following sums using four of the five integers:

1. If we sum everything except __*1*__, our sum is __*2 + 3 + 4 + 5 = 14*__.
2. If we sum everything except __*2*__, our sum is __*1 + 3 + 4 + 5 = 13*__.
3. If we sum everything except __*3*__, our sum is __*1 + 2 + 4 + 5 = 12*__.
4. If we sum everything except __*4*__, our sum is __*1 + 2 + 3 + 5 = 11*__.
5. If we sum everything except __*5*__, our sum is __*1 + 2 + 3 + 4 = 10*__.

As you can see, the minimal sum is __*1 + 2 + 3 + 4 = 10*__ and the maximal sum is __*2 + 3 + 4 + 5 = 14*__. Thus, we print these minimal and maximal sums as two space-separated integers on a new line.

__Hints:__ Beware of integer overflow! Use 64-bit Integer.
