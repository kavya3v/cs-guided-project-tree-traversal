#create BST
class BSTNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#insert a node
    def insert(self,value):
        if value <= self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                #let the right node figure it out
                self.right.insert(value)
#print node
    def print_node(self):
        print(self.value)
        if self.left:
            self.left.print_node()
        if self.right:
            self.right.print_node()

#print iter
    def print_iter_DFS(self):
        stack=[] 
        stack.append(self)
        res=[]
        while(len(stack) > 0):
         
            curr_node = stack.pop()
            res.append(curr_node.value)
            if curr_node is None:
                return

            if curr_node.right is not None:
                stack.append(curr_node.right)

            if curr_node.left is not None: #since we pop the last added item
                stack.append(curr_node.left)
            
        return res

    def print_iter_BFS(node):
        #use queue for BFS 
        q=[] #items added to the front - removed from the back FIFO
        q.insert(0,node) #insert new items to the front of the array
        res=[]
        while q:
            curr=q.pop() #so we remove the old items from the back
            res.append(curr)
            if curr.left is not None:
                q.insert(0,curr.left) #add the child to front of the array
            if curr.right is not None:
                q.insert(0,curr.right)
        return res

            
            


root = BSTNode(5)
root.insert(3)
root.insert(7)
root.print_node()
print(root.print_iter_DFS())
print(root.print_iter_DFS())