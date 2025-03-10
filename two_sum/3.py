def logical_ops(a, b):
    both_true = a and b
    one_true = a or b
    return both_true, one_true

print(logical_ops(True, False))  # Expected output: (False, True)
print(logical_ops(False, False)) # Expected output: (False, False)
print(logical_ops(True, True))   # Expected output: (True, True)
