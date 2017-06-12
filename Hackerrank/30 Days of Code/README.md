# [30 Days of Code](https://www.hackerrank.com/domains/tutorials/30-days-of-code)

```python
class Days(object):
  def __init__(self):
    self.day = 0
  def __iter__(self):
    return self
  def __next__(self):
    if self.day == 30:
      raise StopIteration
    else:
      self.day += 1
      return "Day " + str(self.day)

days = Days()
for d in days:
  print(d)
```

1. [Day 0: Hello, World.](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2000%20-%20Hello%2C%20World)
2. [Day 1: Data Types](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2001%20-%20Data%20Types)
3. [Day 2: Operators](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2002%20-%20Operators)
4. [Day 3: Intro to Conditional Statements](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2003%20-%20Intro%20to%20Conditional%20Statements)
5. [Day 4: Class vs. Instance](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2004%20-%20Class%20vs.%20Instance)
6. [Day 5: Loops](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2005%20-%20Loops)
7. [Day 6: Let's Review](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2006%20-%20Lets%20Review)
8. [Day 7: Arrays](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2007%20-%20Arrays)
9. [Day 8: Dictionaries and Maps](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2008%20-%20Dictionaries%20and%20Maps)
10. [Day 9: Recursion](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2009%20-%20Recursion)
11. [Day 10: Binary Numbers](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2010%20-%20Binary%20Numbers)
12. [Day 11: 2D Arrays](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2011%20-%202D%20Arrays)
13. [Day 12: Inheritance](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2012%20-%20Inheritance)
14. [Day 13: Abstract Classes](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2013%20-%20Abstract%20Classes)
15. [Day 14: Scope](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2014%20-%20Scope)
16. [Day 15: Linked List](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2015%20-%20Linked%20List)
17. [Day 16: Exceptions - String to Integer](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2016%20-%20Exceptions%2C%20String%20to%20Integer)
18. [Day 17: More Exceptions](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2017%20-%20More%20Exceptions)
19. [Day 18: Queues and Stacks](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2018%20-%20Queues%20and%20Stacks)
20. [Day 19: Interfaces](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2019%20-%20Interfaces)
21. [Day 20: Sorting](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2020%20-%20Sorting)
22. [Day 21: Generics](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2021%20-%20Generics)
23. [Day 22: Binary Search Trees](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2022%20-%20Binary%20Search%20Tree)
24. [Day 23: BST Level-Order Traversal](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2023%20-%20BST%20Level-Order%20Traversal)
25. [Day 24: More Linked Lists](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2024%20-%20More%20Linked%20Lists)
26. [Day 25: Running Time and Complexity](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2025%20-%20Running%20Time%20and%20Complexity)
27. [Day 26: Nested Logic](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2026%20-%20Nested%20Logic)
28. [Day 27: Testing](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2027%20-%20Testing)
29. [Day 28: RegEx, Patterns, and Intro to Databases](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2028%20-%20RegEx%2C%20Patterns%2C%20and%20Intro%20to%20Databases)
30. [Day 29: Bitwise AND](https://github.com/joshuatvernon/coding-challenges/tree/master/Hackerrank/30%20Days%20of%20Code/Day%2029%20-%20Bitwise%20AND)
