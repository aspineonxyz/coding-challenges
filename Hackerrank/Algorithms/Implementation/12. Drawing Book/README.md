# Drawing Book

Brie’s Drawing teacher asks her class to open their __*n*__-page book to page number __*p*__. Brie can either start turning pages from the front of the book (i.e., page number __*1*__) or from the back of the book (i.e., page number __*n*__), and she always turns pages one-by-one (as opposed to skipping through multiple pages at once). When she opens the book, page __*1*__ is always on the right side:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/12.%20Drawing%20Book/img/drawing-book-1.png" alt="drawing-book-1">
</p>

Each page in the book has two sides, front and back, except for the last page which may only have a front side depending on the total number of pages of the book (see the Explanation sections below for additional diagrams).

Given __*n*__ and __*p*__, find and print the minimum number of pages Brie must turn in order to arrive at page __*p*__.

#### Input Format
The first line contains an integer, __*n*__, denoting the number of pages in the book.
The second line contains an integer, __*p*__, denoting the page that Brie's teacher wants her to turn to.

#### Constraints
* __*1 <= n <= 10^5*__
* __*1 <= p <= n*__

#### Output Format
Print an integer denoting the minimum number of pages Brie must turn to get to page __*p*__.

#### Sample Input 0
```
6
2
```

#### Sample Output 0
```
1
```

#### Explanation 0
If Brie starts turning from page __*1*__, she only needs to turn __*1*__ page:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/12.%20Drawing%20Book/img/drawing-book-2.png" alt="drawing-book-2">
</p>

If Brie starts turning from page __*6*__, she needs to turn __*2*__ pages:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/12.%20Drawing%20Book/img/drawing-book-3.png" alt="drawing-book-3">
</p>

Because we want to print the minimum number of page turns, we print __*1*__ as our answer.

#### Sample Input 1
```
5
4
```

#### Sample Output 1
```
0
```

#### Explanation 1
If Brie starts turning from page __*1*__, she needs to turn __*2*__ pages:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/12.%20Drawing%20Book/img/drawing-book-4.png" alt="drawing-book-4">
</p>

If Brie starts turning from page __*5*__, she doesn't need to turn any pages:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/12.%20Drawing%20Book/img/drawing-book-5.png" alt="drawing-book-5">
</p>

Because we want to print the minimum number of page turns, we print __*0*__ as our answer.
