# Alogrithms

## Algorithm Characteristics

### Algorithm Complexity

- Space Complexity: How much memory does the alogirthm require?
- Time Complexity: How mych time does it take to complete?

### Inputs and output

- What does the alogrithm accept, and what are the results?

### Classification

- Serial / parallel
- Exact / approximate
- Deterministic / non-deterministic

## Common Algorithms

### Search algorithms

- Find specific data in a structure ( for example, a substring within a string)

### Sorting algorithms

- Take a dataset and apply a sort order to it

### Computational alogrithms

- Given one set of data, derive another from it ( is a given number a prime?)

### Collection algorithms

- Manipulating or navigating set of data that are stored within a particular structure (count specific items, navigate among data elements, filter out unwanted data, etc.)

## Example

### Euclid's Algorithm

Find the greatest common denomiator (GCD) of two integers.

Example: GCD of 20 and 8 is 4 (because 8 / 4 is 2; and 20 / 4 is 5)

1. For two integers a and b, where a > b, divide a by b.
2. If the remainder, r, is 0, then stop: GCD is b.
3. Otherwise, set a to b, b ro r, and repeat at step 1 until r is 0.

## Understanding Algorithm Performance

- Measure how an algortithm responds to dataset size
- Big-O notation
  - Classifies performance as the input size grows
  - "O" indicates the order of operation: time scale to perform an operation
  - Many alogorithms and data structures have more than one O (Inserting data, searching for data, deleting data, etc.)

## Common Big-O Terms

| Notation         | Description   | Example                                                                            |
| ---------------- | ------------- | ---------------------------------------------------------------------------------- |
| O(1)             | Constant time | Looking up a single element in an array                                            |
| O(log n)         | Logarithmic   | Finding an item in a sorted array with a binary search                             |
| O(n)             | Linear time   | Searching an unsorted array for a specific value                                   |
| O(n log n)       | Log-linear    | Complex sorting alogorithms like heap sort and merge sort                          |
| O(n<sup>2</sup>) | Quadratic     | Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort |

## Common Data Structures

- Arrays
- Linked Lists
- Stacks and queues
- Trees
- Hash tables

### Array Operations

- Calculate itms index: O(1)
- Insert or delete item at beginning: O(n)
- Insert or delete item in middle :O(n)
- Insert or delete item at end: O(1)

## Sorting Data

- Bubble Sort
- Merge Sort
- Quick sort

### The Bubble Sort

- One of the most basic sorting alogorithms
- Very simple to understand and implement
- Performance: O(n<sup>2</sup>)
- Other sorting alogorithms are generally much better
- Not considered to be a pratical solution

### The Merge Sort

- Divide-and-congquer algorithm
- Breaks a dataset into individual pieces and merges them
- Uses recursion to operate on datasets
- Performs well on large set of data
- In general has a performance of O(n log n) time complexity

### The Quicksort

- Divide-and-conquer algorithm, like the merge sort
- Also uses recursion to perfomr sorting
- Generally performs better than merge sort, O(n log n)
- Operates in place on the data
- Worst case is O(n<sup>2</sup>) when data is mostly sorted already
