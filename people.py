"""
people.py  -  OWNER: Iyamumpaye Brenda
========================================
Your job: describe the people in the club and the record of each borrowing.
OOP idea to show: INHERITANCE (a keeper is a member).

Build it one step at a time. Run the file after every step:
    python3 people.py
Do NOT rename anything in this file. Other files use these exact names.
"""

# STEP 1: imports
# TODO: from datetime import timedelta


# STEP 2: the class Member
# TODO: add a class variable _next_id = 1
# TODO: write __init__(self, name, room). It must set:
#         self.member_id      -> take the number from _next_id, then add 1
#         self.name
#         self.room
#         self.late_returns   -> 0
#         self.suspended_until -> None
#         self.owes           -> None   (will hold an item they lost)
# TODO: write can_borrow(self, today). It returns a PAIR:
#         (False, "must replace lost item: <item name>")  if self.owes is not None
#         (False, "suspended until <date>")                if suspended_until is
#                                                          not None and today <= suspended_until
#         (True, "")                                       otherwise
# TODO: write __str__ so printing a member shows: Brian (room B07)
class Member:
    pass


# STEP 3: the class Keeper
# INHERITANCE: Keeper extends Member, so it needs no copy of the Member code.
# TODO: make Keeper inherit from Member.
# TODO: write approve(self, item, borrower) that returns True.
class Keeper:
    pass


# STEP 4: the class Loan
# TODO: write __init__(self, item, member, start). It must set:
#         self.item, self.member, self.start
#         self.due           -> start + timedelta(days=item.loan_days)
#                               (POLYMORPHISM: each item type gives its own days)
#         self.returned_on   -> None
#         self.handled_level -> None
# TODO: write days_late(self, today): how many days today is after due,
#       or 0 if it is not late. Hint: (today - self.due).days and max(0, ...)
# TODO: write a property called active: True while returned_on is None
# TODO: write __str__ so printing a loan shows:
#         Phone charger - Brian (due 2026-11-04)
class Loan:
    pass


# STEP 5: test your work
# TODO: under the line below, make a FakeItem class with name and loan_days,
#       then create a Member, a Keeper and a Loan started 4 days ago.
#       Print isinstance(keeper, Member), the loan, days_late and active.
#       Then set suspended_until to 3 days from now and print can_borrow.
if __name__ == "__main__":
    pass

# DONE WHEN: the loan is 3 days late and active, isinstance prints True,
# can_borrow says False with a suspension message, and you can explain why
# Keeper does not need to repeat the Member code.
# HAND OVER: send this file to Diana and Francis.
