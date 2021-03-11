class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        next_id = self.maxDepth()
        value.id = next_id
        if value.id <= self.value.id:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if target == self.value.name:
            return self.value.bio
        if target < self.value.name:
            if self.left is None:
                return False

            return self.left.search(target)

        else:
            if self.right is None:
                return False

            return self.right.search(target)

    def maxDepth(self):
        # Your code here
        left_hight = 0
        right_height = 0
        if self.right:
            right_height = self.right.maxDepth()

        if self.left:
            left_hight = self.left.maxDepth()

        largest_height = max(right_height, left_hight)
            
        return 1 + largest_height

    def find_minimum_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_minimum_value()

    def delete(self, value):
        if self.value > value:
            self.left = self.left.delete(value)
        elif self.value < value:
            self.right = self.right.delete(value)
        else:
            if self.left is not None and self.right is None:
                return self.left
            elif self.right is not None and self.left is None:
                return self.right
            else:
                nex_min_value = self.right.find_minimum_value()
                self.value = nex_min_value
                self.right = self.right.delete(nex_min_value)
        return self

    def print_tree(self):
        print(self.value.name)
        
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()

    def print_tree_inter(self):
        queue = []
        # push first node
        queue.insert(0 ,self)
        
        while len(queue) > 0:
            top_item = queue.pop()
            #do things to item
            print(top_item.value.id)

            # go left
            if top_item.right:
                queue.insert(0, top_item.right)
                
            if top_item.left:
                queue.insert(0, top_item.left)


import random

class User:
    def __init__(self, name, bio):
        self.id =  0
        self.name = name
        self.bio = bio

#user_id = 0
user1 = User("paul", "I wish I was a fish")
root = BSTNode(user1)

#ser_id = root.maxDepth()
user2 = User("dave", "")
root.insert(user2)

#user_id = root.maxDepth()
user3 = User("mike", "Love hurts")
root.insert(user3)





#root.insert(12)
#root.insert(13)
#root.insert(14)

print(root.search('paul'))
#print(root.search(11))

#root.print_tree_inter()
#print(root.maxDepth())

#root = root.delete(12)
root.print_tree()
root.print_tree_inter()





