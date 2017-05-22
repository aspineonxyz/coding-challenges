# Compare the Triplets

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from __*1*__ to __*100*__ for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet __*A = (a_0, a_1, a_3)*__, and the rating for Bob's challenge to be the triplet __*B = (b_0, b_1, b_2)*__.

Your task is to find their comparison points by comparing __*a_0*__ with __*b_0*__, __*a_1*__ with __*b_1*__, and __*a_2*__ with __*b_2*__.

If __*a_i > b_i*__, then Alice is awarded __*1*__ point.
If __*a_i < b_i*__, then Bob is awarded __*1*__ point.
If __*a_i == b_i*__, then neither person receives a point.
Comparison points is the total points a person earned.

Given __*A*__ and __*B*__, can you compare the two challenges and print their respective comparison points?

#### Input Format
The first line contains __*3*__ space-separated integers, __*a_0*__, __*a_1*__, and __*a_2*__, describing the respective values in triplet __*A*__.
The second line contains __*3*__ space-separated integers, __*b_0*__, __*b_1*__, and __*b_2*__, describing the respective values in triplet __*B*__.

#### Constraints
* __*1 <= a_i <= 100*__
* __*1 <= b_i <= 100*__

#### Output Format
Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

#### Sample Input
```
5 6 7
3 6 10
```

#### Sample Output
```
1 1
```

#### Explanation
In this example:
* __*A = (a_0, a_1, a_2) = (5, 6, 7)*__
* __*B = (b_0, b_1, b_2) = (3, 6, 10)*__

Now, let's compare each individual score:
* __*a_0 > b_0*__, so Alice receives __*1*__ point.
* __*a_1 == b_1*__, so nobody receives a point.
* __*a_2 < b_2*__, so Bob receives __*1*__ point.

Alice's comparison score is __*1*__, and Bob's comparison score is __*1*__. Thus, we print `1 1` (Alice's comparison score followed by Bob's comparison score) on a single line.