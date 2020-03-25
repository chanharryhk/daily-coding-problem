# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def checkSums(array, k):
    dict = {}
    for i, e in enumerate(array):
        if k - e == 0:
            dict[e] = True
        dict[k - e] = True
        if e in dict.keys():
            return True
    return False

assert not checkSums([], 17)
assert checkSums([10, 15, 3, 7], 17)
assert checkSums([2], 2)