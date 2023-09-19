def add_beg(self,data):
    new_node=Node(data)
    self.node.ref=self.head
    self.head=new_node