# Some Data structure implementations
This is a repo for implementations of native data structures that are not otherwise readily available or built in the Python language. 

## Circular linked list
Circular Linked List is a variation of Linked list in which the first element points to the last element and the last element points to the first element. Both Singly Linked List and Doubly Linked List can be made into a circular linked list.

![CLL](https://static.javatpoint.com/ds/images/circular-singly-linked-list.png)

### Methods

- *append()* appends a Node object to the end of the linked list, since this is a circular linked list, this means the object will be appended BEFORE the head of the list. 
  - _complexity_ *O(n)* since we need to traverse the entire list (length n) to get to the "last" node (the node before the HEAD)
- *prepend()* appends a Node object before a given *target* Node within the list. 
  - _complexity_ *O(n)* since we need to traverse n Nodes  to get to our target node.
- *split_in_half()* Splits the linked list into two separate circular linked lists. 
  - _complexity_ *O(n)* since the length of the list is n, then $n / 2$ can still be considered n. 
- *print_list()* prints the list node by node. 
  - _complexity_ *O(n)* since we need to traverse the entire list.

## Doubly linked list
The first and last nodes of a doubly linked list are immediately accessible (i.e., accessible without traversal, and usually called head and tail) and therefore allow traversal of the list from the beginning or end of the list, respectively: e.g., traversing the list from beginning to end, or from end to beginning, in a search of the list for a node with specific data value. Any node of a doubly linked list, once obtained, can be used to begin a new traversal of the list, in either direction (towards beginning or end), from the given node.

### Methods

- *append()* appends a Node object to the end of the linked list, since this is a circular linked list, this means the object will be appended BEFORE the head of the list. 
  - _complexity_ *O(n)* since we need to traverse the entire list (length n) to get to the last node
- *prepend()* appends a Node object before a given *target* Node within the list. 
  - _complexity_ *O(n)* since we need to traverse n Nodes  to get to our target node.
- *print_list()* prints the list node by node. 
  - _complexity_ *O(n)* since we need to traverse the entire list.

![DLL](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)
