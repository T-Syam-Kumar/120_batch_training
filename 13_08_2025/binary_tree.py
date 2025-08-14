class Node:
    def __init__(self,key):
        self.left = None 
        self.right = None
        self.val = key
    #preordertraversal 
    def tra_pre_order(self):
        print(self.val,end = "->")
        if self.left:
            self.left.tra_pre_order()
        if self.right:
            self.right.tra_pre_order()
    #inordertraversal
    def tra_in_order(self):
        if self.left:
            self.left.tra_in_order()
        print(self.val,end = "->")
        if self.right:
            self.right.tra_in_order()
    #postordertraversal
    def tra_post_order(self):
        if self.left:
            self.left.tra_post_order()
        if self.right:
            self.right.tra_post_order()
        print(self.val, end = "->")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print("pre order traversal : ", end = " ")
root.tra_pre_order()
print("\nin order traversal : ", end = " ")
root.tra_in_order()
print("\npost order traversal : ", end = " ")
root.tra_post_order()

