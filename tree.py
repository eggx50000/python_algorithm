class BinaryTree:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()
    def to_list(self):
        list=[]
        if self.left:
            list.extend(self.left.to_list())
        list.append(self.val)
        if self.right:
            list.extend(self.right.to_list())
        return list
    
bt10=BinaryTree(10)
bt8=BinaryTree(8)
bt6=BinaryTree(6)
bt4=BinaryTree(4)
bt2=BinaryTree(2)
bt1=BinaryTree(1)
bt0=BinaryTree(0)

bt4.left=bt1
bt4.right=bt8
bt1.left=bt0
bt1.right=bt2
bt8.left=bt6
bt8.right=bt10

root=bt4

root.print()
print(root.to_list())
