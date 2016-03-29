# Lecture 1. Dynamic Connectivity

Talked about 'dynamic connectivity' which seems to mean paths and connections between mutliple objects.

Two methods are defined: union and find.

Union is used to connect two objects.

Find is used to find out if two objects are connected.

Assume connections are reflexive (p is connected to p), symmetric and transitive.

'Connected components' are a maximal set of objects that are mutually connected.

# Lecture 2. Quick Find

A so called eager/greedy approach where an expression is evaluated as soon as it's bound to a variable.

For our data structure:

An integer array id[] of length N.

Interpretation: p and q are connect if and only if they have the same id.

     0 1 2 3 4 5 6 7 8 9
id[] 0 1 1 8 8 0 0 1 8 8

So 0, 5, 6 are connected etc...

* connected(): easy...just check if p and q have the same id.
* union(): more work...find and change all compenent so that they match.

https://github.com/treerock/programming-notes-and-practice/blob/master/algs/quick_find.py

Cost Model:

algo        | init | union | find
----------------------------------
Quick Find  |  N   |   N   |   1

Union is expensive, it takes N**2 array accesses to process a sequence of N union command on N objects.

Quadratic algos do not scale.

# Lecture 3: Quick Union

Quick Union is a lazy approach. Presumably that means an expression isn't evaluated until it is needed.

Data Structure:

* Integer array id[] of length N.
* id[i] is parent of i.
* Root of i is id[id[...id[i]...]]] (keep going until reach root)

     0 1 2 3 4 5 6 7 8 9
id[] 0 1 9 4 9 6 6 7 8 9

So 9 is the parent of 2 and 4 , 4 is the parent of 3 and 6 is the parent of 5.

* connected(): check if p and q have the same root.
* union(): to merge components containing p and q, set the id of p's root to the id of q's root.

So need to be able to find root.

https://github.com/treerock/programming-notes-and-practice/blob/master/algs/quick_union.py

Cost Model

algo        | init | union | find
----------------------------------
Quick Union |  N   |   N   |   N (worst case)

Compare:

Quick-Find: Union to expensive, trees are flat but too expensive to keep flat.

Quick-Union: Trees get tall, find is too expensive (could be N array accesses).

# Lecture 3: Improve Quick Union

Weighted quick-union. Modify quick-union to avoid tall trees. Keep track of size of each tree, balance by linking root of small tree to root of larger tree.

So when you've one large and one small tree, the algorithm chooses to union the smaller tree to the larger tree, thereby minimising the number of updates.

The weighted quick-union algorithm has a couple of modifications from the quick-union:

1. An array tracks the size of the trees with root = i
2. It uses the size array to determine which tree is bigger, then union the smaller tree to the bigger tree.
3. After the union is complete, the size array is update with the new size.

Analysis:

* connected() - take time proportional to the depth of p and q.
* union() - takes constant time, given roots.

Propose that "depth of any node x is at most lg N."

Think this through, the depth of x increases by 1 when tree T1 containing x is merged into another tree T2.

Size of tree containing x can double at most lg N times.


algo        | init | union | find
----------------------------------
Quick Find  |  N   |   N   |
----------------------------------
Quick Union |  N   |   N   |  N
----------------------------------
Weighted QU |  N   |  lg N | lg N

## Quick Union with Compression

Just after computing the root of p, set the id of each examined node to point to that root.

This has the effect of flattening out the tree every time a root is calculated.

There are two variants:

1. Two-pass implementation: add a second look to root() to set the id[] of each examined node to the root.
2. One-pass variant: Make every other node in path point to it's grandparent (thereby halving path length).

## Summary

Weighted quick union (with path compression) makes it possible to solve problems that otherwise would not be address.

It takes operations from quadratic to near linear time.

algorithm               |    worst-case time
-----------------------------------
quick find              |      M * N
quick union             |      M * N
weighted QU             |      N + M log N
QU + path comp          |      N + M log N
weighted QU + path comp |      N + M lg N

# Analysis of Algorithms

User scientific method to analyse algorithms.

* Observe
* Hypothesise
* Predict
* Verify
* Validate

## Observe

Take the ThreeSum algo. Given N distinct integers, how many triples sum to zero.

A very simplistic, brute force algorithm to solve this in python looks a bit like this.

    for i in range(length):
            for j in range(length):
                for k in range(length):
                    if(numbers[i] + numbers[j] + numbers[k] == 0):
                        count+=1

We want to time how long this takes to run for a variety of inputs.

In python we can use the time module to calculate how long it take.

    import time
    start_time = time.time()
    # Do Something
    end_time = time.time()
    print(end_time - start_time)

Combining these we can get some numbers.

    import time, random
    def ThreeSum(numbers):
        length = len(a)
        count = 0
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if(numbers[i] + numbers[j] + numbers[k] == 0):
                        count+=1
        return count

    def generateInts(n):
        ints = []
        for i in range(n):
            ints.append(random.randint(-999, 999))
        return ints

    if __name__ == "__main__":
        for i in range(10, 250, 10):
            a = generateInts(i)
            start_time = time.time()
            count = ThreeSum(a)
            end_time = time.time()
            print(i, count, end_time - start_time)

The output of this looks something like:

(10, 0, 0.00018286705017089844)
(20, 6, 0.0008490085601806641)
(30, 6, 0.0033309459686279297)
(40, 12, 0.009526968002319336)
(50, 42, 0.018131017684936523)
(60, 33, 0.019998788833618164)
(70, 90, 0.045126914978027344)
(80, 153, 0.07164907455444336)
(90, 228, 0.07464003562927246)
(100, 313, 0.08504295349121094)
(110, 508, 0.1125638484954834)
(120, 519, 0.14544391632080078)
(130, 762, 0.18435096740722656)
(140, 1005, 0.3328108787536621)
(150, 1179, 0.5061309337615967)
(160, 1350, 0.4652128219604492)
(170, 1932, 0.41133689880371094)
(180, 2355, 0.9260790348052979)
(190, 2401, 0.7268738746643066)
(200, 2883, 0.9115848541259766)
(210, 3681, 1.3851799964904785)
(220, 4368, 1.5902721881866455)
(230, 4803, 1.4227659702301025)
(240, 4810, 1.2019579410552979)

If you plot that, it comes out looking rather quadratic.