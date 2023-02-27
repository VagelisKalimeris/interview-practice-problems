################################################################################
# Objective         : Given a double, ‘x’, and an integer, ‘n’, write a        #
#                     function to calculate ‘x’ raised to the power ‘n’.       #
# Time Complexity   : O(log(n))                                                #
# Space Complexity  : O(log(n))                                                #
################################################################################
def power(x, n):
    # Edge case
    if n == 0:
        return x if x is 0 else 1

    # Base case
    if n == 1:
        return x

    # Recurse
    if n % 2 == 0:
        sub_x = power(x, n / 2)
        return sub_x * sub_x
    else:
        sub_x = power(x, (n - 1) / 2)
        return sub_x * sub_x * x
