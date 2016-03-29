# Data Structures

## Searching

There is this concept of a symbol table. It describes an abstract mechanism where we can save information (a value) and later search and retrieve that information specifying a key.

The data structure associates a value with a key. It supports two primary operations insert (put) and search (get).

## Binary Search Tree

A binary search tree, aka ordered or sorted binary tree, is a fundamental data structure, often used to contruct more abstract data structures such as sets, multisets and associative arrays.

The benefit of a BST is that it's relatively fast for sorting and searching.

It's a node based binary tree structure where:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys more than the node's key.
* The subtrees are also BSTs.
* There are no duplicate nodes.

"Let x be a node in a Binary Search Tree. If y is a node in the left subtree, the y.key < x.key. Or if y is a node in the right subtree, the y.key > x.key."

[1]: http://algs4.cs.princeton.edu/32bst/
[2]: https://en.wikipedia.org/wiki/Binary_search_tree
[3]: http://interactivepython.org/courselib/static/pythonds/Trees/bst.html