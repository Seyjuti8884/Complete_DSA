class Linkedlist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head==None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref