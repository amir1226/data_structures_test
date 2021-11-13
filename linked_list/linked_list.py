class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def  __repr__(self):
        if self.head is None:
            return "Linked list is empty"

        itr = self.head
        llstr = ''
        while itr:
            llstr += f" {itr.data} -->"
            itr = itr.next
        return llstr
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index<0 or index>=len(self):
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next # Apunto al siguiente nodo
                break
            itr = itr.next #Esto es para avanzar en la iteración
            count += 1
    def insert_at(self,index,data):
        if index<0 or index>=len(self):
            raise Exception("Invalid index")
        if index==0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                my_next = itr.next
                itr.next = Node(data, my_next)
                break
            itr = itr.next
            count += 1
    # Exercise 1        
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        if itr == None:
            return
        while itr:
            if itr.data == data_after:
                itr.next=Node(data_to_insert, itr.next)
                return
            itr = itr.next
        else:
            print(f"Value {data_to_insert} not found")
    
    def remove_by_value(self,data_to_remove):
        itr = self.head
        if itr == None:
            return
        if itr.data == data_to_remove:
            self.head = itr.next
            return
        while itr:
            if itr.next != None and itr.next.data == data_to_remove:
                itr.next= itr.next.next
                return
            itr = itr.next
        else:
            print(f"Value {data_to_remove} not found")
            


if __name__ == '__main__':
    # linked_list = LinkedList()
    # print(linked_list)
    # linked_list.insert_at_beginning(10)
    # linked_list.insert_at_beginning(20)
    # linked_list.insert_at_beginning(40)
    # linked_list.insert_at_end(66)
    # print(linked_list)

    # linked_list_2 = LinkedList()
    # linked_list_2.insert_values([2,20,25,3])
    # print(linked_list_2)
    # print(len(linked_list_2))
    # linked_list_2.remove_at(2)
    # print(linked_list_2)
    # linked_list_2.insert_at(2,25)
    # print(linked_list_2)
    # linked_list_2.insert_after_value(25,123)
    # print(linked_list_2)
    # linked_list_2.insert_after_value(24,122)
    # print(linked_list_2)
    # linked_list_2.remove_by_value(122)
    # print(linked_list_2)
    # linked_list_2.remove_by_value(123)
    # print(linked_list_2)
    # linked_list_2.remove_by_value(2)
    # print(linked_list_2)
    # linked_list_2.insert_after_value(20,33)
    # print(linked_list_2)

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    print(ll)
    ll.insert_after_value("mango","apple")
    print(ll)
    ll.remove_by_value("orange")
    print(ll)
    ll.remove_by_value("figs")
    print(ll)
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    print(ll)





