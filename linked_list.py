class Element(object):
    def __init__(self, value):
        self.value = value
        self.next: Element = None
        

class LinkedList(object):
    def __init__(self, head=None):
        # head is the first element in the list
        self.head: Element = head
        
    def append(self, new_element):
        """[Explanation from Udacity]
        If the LinkedList already has a head, 
        iterate through the next reference in every Element 
        until you reach the end of the list. 
        Set next for the end of the list to be the new_element. 
        Alternatively, if there is no head already, 
        you should just assign new_element to it and do nothing else.
        Args:
            new_element (Element): Element in the linked list
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element    
        else:
            self.head = new_element
            
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        counter = 1
        current: Element = self.head
        if position < 1:
           return None 
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
            current = current.next
            counter += 1
        if position == 1:
            new_element.next = self.head
            self.head = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
            
            

# Test cases
# Set up some Elements
e1 = Element("one")
e2 = Element("two")
e3 = Element("three")
e4 = Element("four")

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
"""
# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
"""