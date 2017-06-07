# Climbing the Leaderboard

Alice is playing an arcade game and wants to climb to the top of the leaderboard. Can you help her track her ranking as she beats each level? The game uses [Dense Ranking](https://en.wikipedia.org/wiki/Ranking#Dense_ranking_.28.221223.22_ranking.29), so its leaderboard works like this:

* The player with the highest score is ranked number __*1*__ on the leaderboard.
* Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

For example, four players have the scores __*100*__, __*90*__, __*90*__, and __*80*__. Those players will have ranks __*1*__, __*2*__, __*2*__, and __*3*__, respectively.

When Alice starts playing, there are already __*n*__ people on the leaderboard. The score of each player __*i*__ is denoted by __*s_i*__. Alice plays for __*m*__ levels, and we denote her total score after passing each level __*j*__ as __*alice_j*__. After completing each level, Alice wants to know her current rank.

You are given an array, __*scores*__, of [monotonically decreasing](https://en.wikipedia.org/wiki/Monotonic_function) leaderboard scores, and another array, __*alice*__, of Alice's cumulative scores for each level of the game. You must print __*m*__ integers. The __*jth*__ integer should indicate the current rank of alice after passing the __*jth*__ level.

#### Input Format
The first line contains an integer, __*n*__, denoting the number of players already on the leaderboard.
The next line contains __*n*__ space-separated integers describing the respective values of __*scores_0, scores_1, ... , scores_n-1*__.
The next line contains an integer, __*m*__, denoting the number of levels Alice beats.
The last line contains __*m*__ space-separated integers describing the respective values of __*alice_0, alice_1, ... , alice_m-1*__.

#### Constraints
* __*1 <= n <= 2 x 10^5*__
* __*1 <= m <= 2 x 10^5*__
* __*0 <= scores_i <= 10^9*__ for __*0 <= i < n*__
* __*0 <= alice_j <= 10*__ for __*0 <= j < m*__
* The existing leaderboard, __*scores*__, is in descending order.
* Alice's scores are cumulative, so __*alice*__ is in ascending order.

#### Subtask
For __*60%*__ of the maximum score:
* __*1 <= n <= 200*__
* __*1 <= m <= 200*__

#### Output Format
Print __*m*__ integers. The  integer should indicate the rank of alice after passing the __*jth*__ level.

#### Sample Input 0
```
7
100 100 50 40 40 20 10
4
5 25 50 120
```

#### Sample Output 0
```
6
4
2
1
```

#### Explanation 0
Alice starts playing with __*7*__ players already on the leaderboard, which looks like this:

<p align="center">
    <img src="" alt="climbing-the-leaderboard1">
</p>

After Alice finishes level __*0*__, her score is __*5*__ and her ranking is __*6*__:

<p align="center">
    <img src="" alt="climbing-the-leaderboard2">
</p>

After Alice finishes level __*1*__, her score is __*25*__ and her ranking is __*4*__:

<p align="center">
    <img src="" alt="climbing-the-leaderboard3">
</p>

After Alice finishes level __*2*__, her score is __*50*__ and her ranking is tied with Caroline at __*2*__:

<p align="center">
    <img src="" alt="climbing-the-leaderboard4">
</p>

After Alice finishes level __*3*__, her score is __*120*__ and her ranking is __*1*__:

<p align="center">
    <img src="" alt="climbing-the-leaderboard5">
</p>
