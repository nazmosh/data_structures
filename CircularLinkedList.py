class CircularLinkedList:

    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = node
            self.head.next= self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = node
            node.next = self.head


    def prepend(self, new_node, target_node):
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
            while current_node.next!= target_node:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = target_node


    def __len__(self):
        if self.head == None:
            return 0
        p = self.head
        counter = 1
        while p.next != self.head:
            p = p.next
            counter += 1
        return counter

    def split_in_half (self):
        if not self.head:
            return None
        if len(self) == 0:
            return None
        half_one = CircularLinkedList()
        half_two = CircularLinkedList()
        halfway = int(len(self) / 2)
        cur_node = self.head
        counter = 0
        while counter < halfway:
            half_one.append(cur_node)
            cur_node = cur_node.next
            counter = counter + 1

        while counter < len(self):
            half_two.append(cur_node)
            cur_node = cur_node.next
            counter = counter + 1
        
        return half_one, half_two
            

    def print_list(self):
        current_node = self.head
        if self.head!= None:
            while current_node:
                print("[{}]".format(current_node.data))
                current_node = current_node.next
                if current_node == self.head:
                    break

    
    def is_circular_linked_list (self, input_list):
        p = input_list.head
        while p.next != input_list.head:
            if p.next == None:
                return False
            p = p.next
        return True
            
        
        
        
    

                
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    linked_list = CircularLinkedList()
    node1 = Node ("A")
    node2 = Node ("B")
    node3 = Node ("C")
    new_node = Node (4)
    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.append(node3)
    linked_list.prepend(new_node, node2)

    #linked_list.print_list()

    print ("length of the list is {}".format(len(linked_list)))

    half_one,  half_two = linked_list.split_in_half()
    half_one.print_list()
    print ("***************")
    half_two.print_list()
