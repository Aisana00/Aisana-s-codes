thisset = {"apple", "banana", "cherry"}

thisset.discard("apple")

print(thisset)

"""
If the item to remove does not exist, discard() will NOT raise an error.
"""

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}
print(thisset[0])
