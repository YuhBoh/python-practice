x = input("X: ")
print(type(x))
# should show that it's a str

y = int(x) + 1
print(f"x: {x}, y: {y}")

# NOTES
# print(f): The f is for string interpolation to replace placeholders (e.g., {x})
#           with a value.

# These are inherently Falsey values:
# ""
# 0
# None (absence of a value)

# How to change data types
# int(x)
# float(x)
# bool(x)
# str(x)