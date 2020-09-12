## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
    * Takes an input string and returns an index/number
    * It accepts a value/key and returns the value associated with that key
    * it maps a value to an index

2. Collision resolution
    * We use linked list to solved hashtable collisions. If more than one value maps to an index, then chain the values together in a linked list

3. Performance of basic hash table operations
    * The performance of basic hash table operations is O(1)

4. Load factor
    * used to determine when to expand or shrink the hashtable
    * Load factor = num elements / num slots
    * Expand table if load factor > 0.7
    * Shrink if < 0.2

5. Automatic resizing
    * If the hashtable load factor is less than 0.2, then shrink the hashtable, but if it is greater than 0.7 then expand the hashtable

6. Various use cases for hash tables
    * Memoization, 
    * Caching
    * Hash-and-store: Using O(1) operations to store/delete/get values to save memory space

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.