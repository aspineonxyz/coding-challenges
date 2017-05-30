# Inserting a Node Into a Sorted Doubly Linked List

Given a reference to the head of a doubly-linked list and an integer, __*data*__, create a new *Node* object having data value __*data*__ and insert it into a sorted linked list.

Complete the `Node* SortedInsert(Node* head, int data)` method in the editor below. It has two parameters:

1. __*head*__: A reference to the head of a doubly-linked list of *Node* objects.
2. __*data*__: An integer denoting the value of the __*data*__ field for the Node you must insert into the list.

The method must insert a new *Node* into the sorted (in ascending order) doubly-linked list whose data value is __*data*__ without breaking any of the list's double links or causing it to become unsorted.

__Note:__ Recall that an empty list (i.e., where __*head = null*__) and a list with one element are sorted lists.

#### Input Format
__Do not read any input from stdin.__ Hidden stub code reads in the following sequence of inputs and passes __*head*__ and __*data*__ to the method:

The first line contains an integer, __*q*__, denoting the number of lists that will be checked. The __*2 * q*__ subsequent lines describe the elements to insert into each list over two lines:

1. The first line contains an integer, __*n*__, denoting the number of elements that will be inserted into the list.
2. The second line contains __*n*__ space-separated integers describing the respective data values that your code must insert into the list during each call to the method.

#### Output Format
__Do not print anything to stdout.__ Your method must return a reference to the __*head*__ of the same list that was passed to it as a parameter. The custom checker for this challenge checks the list to ensure it hasn't been modified other than to properly insert the new *Node* in the correct location.

#### Sample Input
```
1
3
2 5 4
```

#### Sample Output
```
2 4 5
```

#### Explanation
1. We start out with an empty list. We insert a node with __*data = 2*__. The list becomes __*head -> 2 -> null*__. We return __*head*__.
2. The head of the previously modified list is passed to our method as an argument. We insert a node with __*data = 5*__. The list becomes __*head -> 2 <-> 5 -> null*__. We return __*head*__.
3. The head of the previously modified list is passed to our method as an argument. We insert a node with __*data = 4*__. The list becomes __*head -> 2 <-> 4 <-> 5 -> null*__. We return __*head*__.

Hidden stub code then prints the final list as a single line of space-separated integers.
