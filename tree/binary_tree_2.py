class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
        if value > self.data:
            if self.right:
                return self.right.search(value)
        return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum

    def post_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    "----- Deletion ----- "

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            self.data = self.right.find_min()
            self.right = self.right.delete(self.data)

        return self
    # Exercise

    def delete_2(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # Change for exercise
            self.data = self.left.find_max()
            self.left = self.left.delete(self.data)

        return self


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 15, 7]
    numbers_tree = build_tree(numbers)
    print("Before deleting 15: ", numbers_tree.in_order_traversal())
    print("Delete 15: ", numbers_tree.delete_2(15))
    print("After deleting 15: ", numbers_tree.in_order_traversal())
