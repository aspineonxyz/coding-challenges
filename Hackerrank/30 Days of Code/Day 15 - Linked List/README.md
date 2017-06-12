# [Day 15: Linked List](https://www.hackerrank.com/challenges/30-linked-list/submissions/code/32284623)

#### Objective
Today we're working with *Linked Lists*. Check out the Tutorial tab for learning materials and an instructional video!

A *Node* class is provided for you in the editor. A *Node* object has an integer data field, __*data*__, and a *Node* instance pointer, __*next*__, pointing to another node (i.e.: the next node in a list).

A *Node* insert function is also declared in your editor. It has two parameters: a pointer, __*head*__, pointing to the first node of a linked list, and an integer __*data*__ value that must be added to the end of the list as a new *Node* object.

#### Task
Complete the insert function in your editor so that it creates a new *Node* (pass __*data*__ as the *Node* constructor argument) and inserts it at the tail of the linked list referenced by the __*head*__ parameter. Once the new node is added, return the reference to the __*head*__ node.

__Note:__ If the __*head*__ argument passed to the insert function is *null*, then the initial list is empty.

#### Input Format
The insert function has  parameters: a pointer to a *Node* named __*head*__, and an integer value, __*data*__.
The constructor for *Node* has __*1*__ parameter: an integer value for the __*data*__ field.

You do not need to read anything from stdin.

#### Output Format
Your *insert* function should return a reference to the __*head*__ node of the linked list.

#### Sample Input
The following input is handled for you by the locked code in the editor:
The first line contains __*T*__, the number of test cases.
The __*T*__ subsequent lines of test cases each contain an integer to be inserted at the list's tail.
```
4
2
3
4
1
```

#### Sample Output
The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:
```
2 3 4 1
```

#### Explanation
__*T = 4*__, so the locked code in the editor will be inserting __*4*__ nodes.
The list is initially empty, so __*head*__ is null; accounting for this, our code returns a new node containing the data value __*2*__ as the __*head*__ of our list. We then create and insert nodes __*3*__, __*4*__, and __*1*__ at the tail of our list. The resulting list returned by the last call to __*insert*__ is __*[2,3,4,1]*__, so the printed output is `2 3 4 1`.

<p align="">
    <img src="" alt="linked-list-1">
</p>
