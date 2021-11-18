class Node(object):
    def __init__(self, value):
        self.value = value
        self.next: Node = None
        

class LinkedList(object):
    def __init__(self, head=None):
        # head is the first Node in the list
        self.head: Node = head
        
    def append(self, new_node):
        """[Explanation from Udacity]
        If the LinkedList already has a head, 
        iterate through the next reference in every Node 
        until you reach the end of the list. 
        Set next for the end of the list to be the new_node. 
        Alternatively, if there is no head already, 
        you should just assign new_node to it and do nothing else.
        Args:
            new_node (Node): Node in the linked list
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node    
        else:
            self.head = new_node
            
            
    def get_position(self, position):
        """Get an Node from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        counter = 1
        current = self.head
        if position < 1:
           return None 
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_node, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd Nodes."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1
            
        if position == 1:
            new_node.next = self.head
            self.head = new_node
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next   
        if current.value == value:
            if previous:
                previous.next = current.next
                current = None
            else:
                self.head = current.next
                current = None   
                        
            

# Test cases
# Set up some Nodes
e1 = Node("one")
e2 = Node("two")
e3 = Node("three")
e4 = Node("four")

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete('one')

# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
