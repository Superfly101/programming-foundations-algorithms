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

* Classifies performance as the input size grows
* "O" indicates the order of operation: time scale to perform an operation
* Many alogorithms and data structures have more than one O (Inserting data, searching for data, deleting data, etc.)

## Common Big-O Terms

| Notation         | Description   | Example                                                                            |
| ---------------- | ------------- | ---------------------------------------------------------------------------------- |
| O(1)             | Constant time | Looking up a single element in an array                                            |
| O(log n)         | Logarithmic   | Finding an item in a sorted array with a binary search                             |
| O(n)             | Linear time   | Searching an unsorted array for a specific value                                   |
| O(n log n)       | Log-linear    | Complex sorting alogorithms like heap sort and merge sort                          |
| O(n<sup>2</sup>) | Quadratic     | Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort |
