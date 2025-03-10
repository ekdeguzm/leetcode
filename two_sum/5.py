def check_membership(nums):
    check_5 = 5 in nums
    check_ten = 10 in nums
    return check_5, check_ten

print(check_membership([1, 2, 3, 5, 7]))  # Expected output: (True, True)
print(check_membership([10, 20, 30]))     # Expected output: (False, False)

def check_identity():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1  # Same object reference

    return (list1 is list3, list1 == list2, list1 is list2)

print(check_identity())  # Expected output: (True, True, False)