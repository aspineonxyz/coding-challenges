# [Day 23: BST Level-Order Traversal](https://www.hackerrank.com/challenges/30-binary-trees)

#### Objective
Today, we're going further with Binary Search Trees. Check out the Tutorial tab for learning materials and an instructional video!

#### Task
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, __*root*__, pointing to the root of a binary search tree. Complete the *levelOrder* function provided in your editor so that it prints the level-order traversal of the binary search tree.

__Hint:__ You'll find a queue helpful in completing this challenge.

#### Input Format
The locked stub code in your editor reads the following inputs and assembles them into a BST:
The first line contains an integer, __*T*__ (the number of test cases).
The __*T*__ subsequent lines each contain an integer, __*data*__, denoting the value of an element that must be added to the BST.

#### Output Format
Print the __*data*__ value of each node in the tree's level-order traversal as a single line of __*N*__ space-separated integers.

#### Sample Input
```
6
3
5
4
7
2
1
```

#### Sample Output
```
3 2 5 1 4 7
```

#### Explanation
The input forms the following binary search tree:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/30%20Days%20of%20Code/Day%2023%20-%20BST%20Level-Order%20Traversal/img/bst-level-order-traversal.png" alt="bst-level-order-traversal">
</p>

We traverse each level of the tree from the root downward, and we process the nodes at each level from left to right. The resulting level-order traversal is __*3 -> 2 -> 5 -> 1 -> 4 -> 7*__, and we print these data values as a single line of space-separated integers.
