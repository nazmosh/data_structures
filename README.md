# data structure implementation
This is a repo for implementations of native data structures that are not otherwise readily available or built in the Python language. 

## Circular linked list
Circular Linked List is a variation of Linked list in which the first element points to the last element and the last element points to the first element. Both Singly Linked List and Doubly Linked List can be made into a circular linked list.

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
