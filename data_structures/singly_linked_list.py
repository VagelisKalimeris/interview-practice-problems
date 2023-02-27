class SingleListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append(self, data):
        if self.data is None:
            self.data = data
        else:
            curr_node = self
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = SingleListNode(data)
        return self

    def append_multi(self, data_list):
        for dt in data_list:
            self.append(dt)
        return self

    def print(self):
        print(self.data)
        if self.next:
            self.next.print()

    def list_is_identical_with(self, other):
        curr_a, curr_b = self, other

        while curr_a or curr_b:
            if not (curr_a and curr_b) or (curr_a.data != curr_b.data):
                return False
            curr_a, curr_b = curr_a.next, curr_b.next

        return True

    def create_loop_in_list(self, start_node_num, end_node_num):
        assert start_node_num < end_node_num, 'Loop start/end Error!'

        curr_node, counter, start_node = self, 0, None

        while curr_node.next:
            if counter == start_node_num:
                start_node = curr_node
            elif counter == end_node_num:
                curr_node.next = start_node
                break
            counter += 1
            curr_node = curr_node.next


#  Helper function
def get_int_in_inv_list(lst):
    rev_int, curr_node = '', lst

    while curr_node:
        rev_int += str(curr_node.data)
        curr_node = curr_node.next

    return int(rev_int[::-1])
