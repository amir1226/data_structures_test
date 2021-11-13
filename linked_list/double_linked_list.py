class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# Exercise 2
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self,data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
            self.tail = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node      
    def insert_at_ending(self,data):
        if self.tail == None:
            node = Node(data, self.head, None)
            self.head = node
            self.tail = node
        else:
            node = Node(data, None, self.tail)
            self.tail.next = node
            self.tail = node   

    def print_forward(self):
        if self.head is None:
            print("Double linked list is empty")
            return
        text = "Forward: "
        itr = self.head
        while itr:
            text += f" {itr.data} ->"
            itr = itr.next
        print(text)

    def print_backward(self):      
        if self.tail is None:
            print("Double linked list is empty")
            return
        text = "Backward: "
        itr = self.tail
        while itr:
            text += f" {itr.data} ->"
            itr = itr.prev
        print(text)

    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count  

    def __find_node_by_index(self, index):
        n = len(self)
        if index < 0 or index >= n:
            raise Exception("Invalid index")
        if index == 0:
            return self.head
        if index == n-1:
            return self.tail
            
        itr = self.head.next
        count = 1
        while itr:
            if(count == index):
                return itr
            itr = itr.next
            count += 1

    def get_value_by_index(self, index):
        node = self.__find_node_by_index(index)
        print(f"Index {index} has value {node.data}")

    def insert_previous_index(self, index, value):
        finded_node = self.__find_node_by_index(index)
        if  finded_node.prev != None:
            new_node = Node(value, finded_node, finded_node.prev)
            finded_node.prev.next = new_node
            finded_node.prev = new_node       
        else:
            new_node = Node(value, finded_node, finded_node.prev)
            finded_node.prev = new_node       
            self.head = new_node
 

    def insert_next_index(self, index, value):
        finded_node = self.__find_node_by_index(index)
        if  finded_node.next != None:
            new_node = Node(value, finded_node.next , finded_node)
            finded_node.next.prev = new_node
            finded_node.next = new_node
        else:
            new_node = Node(value, finded_node.next , finded_node)
            finded_node.next = new_node
            self.tail = new_node


    def delete_by_index(self, index):
        finded_node = self.__find_node_by_index(index)
        if index == 0:
            finded_node.next.prev = None
            self.head = finded_node.next
        elif index == len(self)-1:
            finded_node.prev.next = None
            self.tail = finded_node.prev
        else:
            finded_node.next.prev = finded_node.prev
            finded_node.prev.next = finded_node.next


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.print_forward()
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(5)
    dll.insert_at_ending(66)

    dll.print_forward()
    dll.print_backward()

    print("Head is: " + str(dll.head.data))
    print("Tail is: " + str(dll.tail.data))
    dll.get_value_by_index(3)
    
    print(len(dll))

    dll.insert_previous_index(3, 12)
    dll.print_forward()

    dll.insert_previous_index(0, 99)
    dll.print_forward()


    dll.insert_next_index(2, 123)
    dll.print_forward()

    dll.insert_next_index(6, 1000)
    dll.print_forward()

    dll.delete_by_index(0)
    dll.print_forward()
    
    print("Head is: " + str(dll.head.data))

    dll.delete_by_index(6)
    dll.print_forward()
    
    print("Tail is: " + str(dll.tail.data))

    dll.delete_by_index(1)
    dll.print_forward()
    dll.print_backward()

















