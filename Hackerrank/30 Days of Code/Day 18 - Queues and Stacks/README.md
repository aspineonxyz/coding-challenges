*palindrome*# [Day 18: Queues and Stacks](https://www.hackerrank.com/challenges/30-queues-stacks)

Welcome to Day 18! Today we're learning about Stacks and Queues. Check out the Tutorial tab for learning materials and an instructional video!

A *palindrome* is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, __*S*__, is a *palindrome*?

To solve this challenge, we must first take each character in __*s*__, enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and *pop* the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means __*s*__ isn't a *palindrome*).

Write the following declarations and implementations:
1. Two instance variables: one for your __*stack*__, and one for your __*queue*__.
2. A void *pushCharacter(char ch)* method that pushes a character onto a stack.
3. A void *enqueueCharacter(char ch)* method that enqueues a character in the __*queue*__ instance variable.
4. A char *popCharacter()* method that pops and returns the character at the top of the __*stack*__ instance variable.
5. A char *dequeueCharacter()* method that dequeues and returns the first character in the __*queue*__ instance variable.

#### Input Format
You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string __*s*__. It then calls the methods specified above to pass each character to your instance variables.

#### Constraints
* __*s*__ is composed of lowercase English letters.

#### Output Format
You are not responsible for printing any output to stdout.
If your code is correctly written and __*s*__ is a *palindrome*, the locked stub code will print __*The word, s, is a palindrome.*__; otherwise, it will print __*The word, s, is not a palindrome*__.

#### Sample Input
```
racecar
```

#### Sample Output
```
The word, racecar, is a palindrome.
```
