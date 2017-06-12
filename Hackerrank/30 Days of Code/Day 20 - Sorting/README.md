# [Day 20: Sorting](https://www.hackerrank.com/challenges/30-sorting)

#### Objective
Today, we're discussing a simple sorting algorithm called *Bubble Sort*. Check out the Tutorial tab for learning materials and an instructional video!

Consider the following version of Bubble Sort:
```
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;

    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }

    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
```

#### Task
Given an array, __*a*__, of size __*n*__ distinct elements, sort the array in ascending order using the *Bubble Sort* algorithm above. Once sorted, print the following __*3*__ lines:
1. `Array is sorted in numSwaps swaps.``
where __*numSwaps*__ is the number of swaps that took place.
2. `First Element: firstElement`
where __*firstElement*__ is the first element in the sorted array.
3. `Last Element: lastElement`
where __*lastElement*__ is the last element in the sorted array.

__Hint:__ To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

#### Input Format
The first line contains an integer, __*n*__, denoting the number of elements in array __*a*__.
The second line contains __*n*__ space-separated integers describing the respective values of __*a_0, a_1, ... , a_n-1*__.

#### Constraints
* __*2 <= n <= 600*__
* __*1 <= a_i <= 2 x 10^6*__, where __*0 <= i <= n*__.

#### Output Format
Print the following three lines of output:
1. `Array is sorted in numSwaps swaps.``
where __*numSwaps*__ is the number of swaps that took place.
2. `First Element: firstElement`
where __*firstElement*__ is the first element in the sorted array.
3. `Last Element: lastElement`
where __*lastElement*__ is the last element in the sorted array.

#### Sample Input 0
```
3
1 2 3
```

#### Sample Output 0
```
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
```

#### Explanation 0
The array is already sorted, so __*0*__ swaps take place and we print the necessary __*3*__ lines of output shown above.

#### Sample Input 1
```
3
3 2 1
```

#### Sample Output 1
```
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
```

#### Explanation 1
The array __*a = [3,2,1]*__ is *not sorted*, so we perform the following __*3*__ swaps:
1. __*[3,2,1] -> [2,3,1]*__
2. __*[2,3,1] -> [2,1,3]*__
3. __*[2,1,3] -> [1,2,3]*__

At this point the array is sorted and we print the necessary __*3*__ lines of output shown above.
