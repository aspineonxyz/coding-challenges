#### [Algorithms](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms)

```python
def binary_search(items, goal):
  if len(items) == 0:
    return False
  mid = len(items) // 2
  if items[mid] == goal:
    return True
  elif items[mid] <= goal:
    return binary_search(items[mid+1:], goal)
  else:
    return binary_search(items[:mid], goal)
```

##### [Warmup](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup)

1. [Solve Me First](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/01.%20Solve%20Me%20First)
2. [Simple Array Sum](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/02.%20Simple%20Array%20Sum)
3. [Compare the Triplets](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/03.%20Compare%20the%20Triplets)
4. [A Very Big Sum](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/04.%20A%20Very%20Big%20Sum)
5. [Diagonal Difference](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/05.%20Diagonal%20Difference)
6. [Plus Minus](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/06.%20Plus%20Minus)
7. [Staircase](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/07.%20Staircase)
8. [Mini-Max Sum](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/08.%20Mini-Max%20Sum)
9. [Birthday Cake Candles](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/09.%20Birthday%20Cake%20Candles)
10. [Time Conversion](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Warmup/10.%20Time%20Conversion)

##### [Implementation](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation)
1. [Grading Students](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/01.%20Grading%20Students)
2. [Apple and Orange](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/02.%20Apple%20and%20Orange)
3. [Kangaroo](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/03.%20Kangaroo)
4. [Between Two Sets](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/04.%20Between%20Two%20Sets)
5. [Breaking the Records](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/05.%20Breaking%20the%20Records)
6. [Birthday Chocolate](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/06.%20Birthday%20Chocolate)
7. [Divisible Sum Pairs](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/07.%20Divisible%20Sum%20Pairs)
8. [Migratory Birds](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/08.%20Migratory%20Birds)
9. [Day of the Programmer](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/09.%20Day%20of%20the%20Programmer)
10. [Bon Appétit](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/10.%20Bon%20Appetit)
11. [Sock Merchant](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/11.%20Sock%20Merchant)
12. [Drawing Book](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/12.%20Drawing%20Book)
13. [Counting Valleys](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/13.%20Counting%20Valleys)
14. [Electronics Shop](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/14.%20Electronics%20Shop)
15. [Cats and a Mouse](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/15.%20Cats%20and%20a%20Mouse)
16. [Forming a Magic Square](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/16.%20Forming%20a%20Magic%20Square)
17. [Picking Numbers](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/17.%20Picking%20Numbers)
18. [Climbing the Leaderboard](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/18.%20Climbing%20the%20Leaderboard)
19. [The Hurdle Race](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/19.%20The%20Hurdle%20Race)
20. [Designer PDF Viewer](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/20.%20Designer%20PDF%20Viewer)
21. [Utopian Tree](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/Algorithms/Implementation/21.%20Utopian%20Tree)
<!--to be continued . . .-->
