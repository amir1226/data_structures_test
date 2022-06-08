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


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 15, 7]
    numbers_tree = build_tree(numbers)
    print("In-order traversal: ", numbers_tree.in_order_traversal())
    print("Searching for value 7: ", numbers_tree.search(7))
    print("Searching for value 8: ", numbers_tree.search(8))
    countries = ["India", "Pakistan", "Germany",
                 "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    print(country_tree.in_order_traversal())

    numbers_tree = build_tree(numbers)
    print("Input numbers:", numbers)
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
"""
1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
"""
