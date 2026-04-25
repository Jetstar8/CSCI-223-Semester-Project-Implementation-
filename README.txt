# CSCI-223-Semester-Project-Implementation- Jess Martin
Implementing Dijkstra's Algorithm for a Shortest intersection search

The required file must have in each line: Two nodes that connect, separated by a space, and then the distance between them.
For example:
A B 2
B C 1

There are two example of input files, Inputfile.txt and inputfile2.txt. To change the name of the file being
turned into a graph, go into the main function and change the filename.
Then when the python file is ran, the user will provide two inputs: a start node and an end node. If the node is not in
the input file - aka the graph, then the program will error.

In the PathFinder Class I implemented Dijkstra's algorithm which uses a priority queue to pop the shortest distance.
I decided to use heapq for the priority queue because for push() and pop() it has a time complexity of O(log n) by
keeping the queue in partial order; which is all we need for the smallest element to be at the top, since Dijkstra's only
needs the unvisited node with the smallest distance.

Runtime:

Dijkstra's Loop:
O(V log V) for every node visited
O(E log V) for every edge relaxed and push()ed to queue.
= 0((V+E) LOG V)

