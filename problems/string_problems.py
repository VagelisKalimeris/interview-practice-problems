################################################################################
# Objective         : Write a function that takes a string s as input and      #
#                     checks whether it’s a palindrome or not.                 #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(1)                                                     #
################################################################################
def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


################################################################################
# Objective         : Write a function that takes a string s as input and      #
#                     checks whether it can be a valid palindrome by removing  #
#                     at most one character from it.                           #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(1)                                                     #
################################################################################
def is_palindrome_relaxed(s, flag=False):
    i, j = 0, len(s) - 1

    # Edge cases
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        return False

    while i <= j:
        if s[i] != s[j]:
            if not flag:
                return is_palindrome_relaxed(s[i:j], True) or \
                    is_palindrome_relaxed(s[i + 1:j + 1], True)
            return False
        i += 1
        j -= 1

    return True


################################################################################
# Objective         : Given a sentence, reverse the order of its words,        #
#                     without affecting the order of letters within a given    #
#                     word.                                                    #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(n)                                                     #
################################################################################
def reverse_words_order(sentence):
    return ' '.join(reversed(sentence.split()))


################################################################################
# Objective         : Given two strings s and t, return true if t is an        #
#                     anagram of s, and false otherwise.                       #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(n)                                                     #
################################################################################
def is_anagram(s, t):
    t_list = [x for x in t]
    for x in s:
        if x in t_list:
            t_list.remove(x)
        else:
            return False
    return t_list == []