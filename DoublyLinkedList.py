class DoublyLinkedList:

    def __init__(self):
        self.head = None



    def append(self, node):
        if self.head:
            p = self.head
            while p.next:
                p =  p.next
        
            p.next =  node
            node.prev = p
            node.next = None
        else:
            self.head = node


    def prepend(self, new_node, target_node):
        if self.head == target_node:
            new_node.prev = None
            self.head.prev = new_node
            new_node.next = self.head
        elif self.head:
            p= self.head
            while p.next != target_node:
                p = p.next

            p.next = new_node
            new_node.prev = p
            new_node.next = target_node
            target_node.prev = new_node
        elif not self.head:
            self.append(new_node)


    def print_list(self):
        p = self.head
        while p:
            print("[{}]".format(p.data))
            p = p.next
        
        
    

                
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


if __name__ == "__main__":

    dll = DoublyLinkedList()

    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(7)

    dll.append (node1)
    dll.prepend (node2, node1)
    dll.append (node3)
    
    dll.print_list()