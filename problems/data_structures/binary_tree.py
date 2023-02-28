class TreeNode:
    def __init__(self, data=None):
        self.lc = None
        self.rc = None
        self.data = data

    # Insert Node
    def insert(self, data):
        if self.data or data == self.data:
            if data < self.data:
                if self.lc is None:
                    self.lc = TreeNode(data)
                else:
                    self.lc.insert(data)
            elif data > self.data:
                if self.rc is None:
                    self.rc = TreeNode(data)
                else:
                    self.rc.insert(data)
        else:
            self.data = data
        return self

    def insert_multiple(self, data_list):
        for dt in data_list:
            self.insert(dt)
        return self

    # Print the Tree
    def print_tree(self):
        if self.lc:
            self.lc.print_tree()
        print(self.data),
        if self.rc:
            self.rc.print_tree()
