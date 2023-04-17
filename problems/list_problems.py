from problems.data_structures.singly_linked_list import SingleListNode


################################################################################
# Objective         : Given two sorted linked lists, merge them so the         #
#                     resulting linked list is also sorted.                    #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(1)                                                     #
################################################################################
def merge_sorted_lists(list_a, list_b):
    res_list = SingleListNode()
    curr_a, curr_b = list_a, list_b

    while True:
        if (curr_a and curr_b and curr_a.data < curr_b.data) or \
                                                        (curr_a and not curr_b):
            res_list.append(curr_a.data)
            curr_a = curr_a.next
        elif (curr_a and curr_b and curr_a.data > curr_b.data) or \
                                                        (curr_b and not curr_a):
            res_list.append(curr_b.data)
            curr_b = curr_b.next
        elif curr_a and curr_b and curr_a.data == curr_b.data:
            res_list.append_multi([curr_a.data, curr_b.data])
            curr_a, curr_b = curr_a.next, curr_b.next
        else:
            break

    return res_list


################################################################################
# Objective         : Given a linked list, check if the linked list has a loop #
#                     or not.                                                  #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(1)                                                     #
################################################################################
def find_loop_in_list(lst):
    if not lst.next:
        return False

    one_step_curr, two_step_curr = lst, lst.next
    while two_step_curr:
        if one_step_curr == two_step_curr:
            return True
        one_step_curr = one_step_curr.next
        two_step_curr = two_step_curr.next
        if two_step_curr:
            two_step_curr = two_step_curr.next

    return False


################################################################################
# Objective         : You are given the head pointers of two linked lists      #
#                     where each linked list represents an inverted integer    #
#                     number (i.e. each node is a digit). Add them and return  #
#                     the new linked list.                                     #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(1)                                                     #
################################################################################
def add_inv_int_lists(list_a, list_b):
    res_list = SingleListNode()
    curr_a, curr_b = list_a, list_b

    hold = 0
    while curr_a or curr_b or hold:
        dig_a = int(curr_a.data) if curr_a else 0
        dig_b = int(curr_b.data) if curr_b else 0

        addition_digits = [int(dig) for dig in str(dig_a + dig_b + hold)]
        if len(addition_digits) == 1:
            res_list.append(addition_digits[0])
            hold = 0
        else:
            res_list.append(addition_digits[1])
            hold = addition_digits[0]

        curr_a = curr_a.next if curr_a else curr_a
        curr_b = curr_b.next if curr_b else curr_b

    return res_list
