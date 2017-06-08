# [Bon Appétit](https://www.hackerrank.com/challenges/bon-appetit)

Anna and Brian order __*n*__ items at a restaurant, but Anna declines to eat any of the __*Kth*__ item (where __*0 <= K <= n*__) due to an allergy. When the check comes, they decide to split the cost of all the items they shared; however, Brian may have forgotten that they didn't split the __*Kth*__ item and accidentally charged Anna for it.

You are given __*n*__, __*K*__, the cost of each of the __*n*__ items, and the total amount of money that Brian charged Anna for her portion of the bill. If the bill is fairly split, print `Bon Appetit`; otherwise, print the amount of money that Brian must refund to Anna.

#### Input Format
The first line contains two space-separated integers denoting the respective values of __*n*__ (the number of items ordered) and __*K*__ (the __*0*__-based index of the item that Anna did not eat).
The second line contains __*n*__ space-separated integers where each integer __*i*__ denotes the cost, __*c[i]*__, of item __*i*__ (where __*0 <= i < n*__).
The third line contains an integer, __*b_charged*__, denoting the amount of money that Brian charged Anna for her share of the bill.

#### Constraints
* __*2 <= n <= 10^5*__
* __*0 <= k < n*__
* __*0 <= c[i] <= 10^4*__
* __*0 <= b <= ∑ c[i]*__

#### Output Format
If Brian did not overcharge Anna, print `Bon Appetit` on a new line; otherwise, print the difference (i.e., __*b_charged - b_actual*__) that Brian must refund to Anna (it is guaranteed that this will always be an integer).

#### Sample Input 0
```
4 1
3 10 2 9
12
```

#### Sample Output 0
```
5
```

#### Explanation 0
Anna didn't eat item __*c[i] = 10*__, but she shared the rest of the items with Brian. The total cost of the shared items is __*3 + 2 + 9 = 14*__ and, split in half, the cost per person is __*b_actual = 7*__. Brian charged her __*b_charged = 12*__ for her portion of the bill, which is more than the __*7*__ dollars worth of food that she actually shared with him. Thus, we print the amount Anna was overcharged, __*b_charged - b_actual = 12 - 7 = 5*__, on a new line.

#### Sample Input 1
```
4 1
3 10 2 9
7
```

#### Sample Output 1
```
Bon Appetit
```

#### Explanation 1
Anna didn't eat item __*c[i] = 10*__, but she shared the rest of the items with Brian. The total cost of the shared items is __*3 + 2 + 9 = 14*__ and, split in half, the cost per person is __*b_actual = 7*__. Because this matches the amount, __*b_charged = 7*__, that Brian charged Anna for her portion of the bill, we print `Bon Appetit` on a new line.
