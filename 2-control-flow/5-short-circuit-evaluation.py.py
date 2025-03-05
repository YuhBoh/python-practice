high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
  print("Eligible")
else:
  print("Not Eligible")
Output: "Eligible"
# Short Circuit just means that from left to right, if the first condition (if high_income) is not met, the code stops there. Doesn't matter if the rest meets the conditions.