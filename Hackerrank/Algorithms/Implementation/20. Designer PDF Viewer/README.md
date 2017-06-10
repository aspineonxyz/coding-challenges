# [Designer PDF Viewer](https://www.hackerrank.com/challenges/designer-pdf-viewer)

When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In a new kind of PDF viewer, the selection of each word is independent of the other words; this means that each rectangular selection area forms independently around each highlighted word. For example:

<p align="center">
    <img src="https://github.com/joshuatvernon/coding-challenges/blob/master/Hackerrank/Algorithms/Implementation/20.%20Designer%20PDF%20Viewer/img/designer-pdf-viewer-1.png" alt="designer-pdf-viewer-1">
</p>

In this type of PDF viewer, the *width* of the rectangular selection area is equal to the number of letters in the word times the width of a letter, and the *height* is the maximum height of any letter in the word.

Consider a word consisting of lowercase English alphabetic letters, where each letter is __*1mm*__ wide. Given the height of each letter in millimetres (__*mm*__), find the total area that will be highlighted by blue rectangle in __*mm^2*__ when the given word is selected in our new PDF viewer.

#### Input Format
The first line contains __*26*__ space-separated integers describing the respective heights of each consecutive lowercase English letter (i.e., __*h_a, h_b, h_c, ... , h_y, h_z*__).
The second line contains a single word, consisting of lowercase English alphabetic letters.

#### Constraints
* __*1<= h_? <= 7*__, where __*?*__ is an English lowercase letter.
* Word contains no more than __*10*__ letters.

#### Output Format
Print a single integer denoting the area of highlighted rectangle when the given word is selected. The unit of measurement for this is square millimetres (__*mm^2*__), but you must only print the integer.

#### Sample Input
```
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
```

#### Sample Output
```
9
```

#### Explanation
We are highlighting the word `abc`:

The tallest letter in `abc` is `b`, and __*h_b = 3*__. The selection area for this word is __*3 * 1mm * 3mm = 9mm^2*__.
__Note:__ Recall that the width of each character is __*1mm*__.
