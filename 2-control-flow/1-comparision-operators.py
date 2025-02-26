x = 10 > 3
print(bool(x))
# Output: True

x = 10 >= 3
print(bool(x))
# Output: True

x = 10 < 20
print(bool(x))
# Output: True

x = 10 <= 3
print(bool(x))
# Output: True

x = 10 == 10
print(bool(x))
# Output: True

x = 10 == "10"
print(bool(x))
# Output: False

x = 10 != "10"
print(bool(x))
# Output: True

x = "bag" > "apple"
print(bool(x))
# Output: True
# Because letter b comes after a.

x = "bag" == "BAG"
print(bool(x))
# Output: False
# Because every letter has a numerical value that represents the letters.
# The numerical values that represents b and B are different.