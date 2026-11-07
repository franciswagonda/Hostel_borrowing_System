"""
items.py  -  OWNER: Alvin Mugisha Allan
=========================================
Your job: describe the things that can be borrowed.
OOP ideas to show: ABSTRACTION, INHERITANCE, POLYMORPHISM.

Build it one step at a time. Run the file after every step:
    python3 items.py
Do NOT rename anything in this file. Other files use these exact names.
"""

# STEP 1: imports
# TODO: import ABC and abstractmethod from the abc module.


# STEP 2: the abstract class Item
# ABSTRACTION: nobody should be able to create a plain Item.
# TODO: make Item inherit from ABC.
# TODO: add a class variable _next_id = 1 (it counts the items).
# TODO: write __init__(self, name, owner). It must set:
#         self.item_id   -> take the number from _next_id, then add 1 to _next_id
#         self.name      -> the name of the item
#         self.owner     -> the member who owns it
#         self.status    -> the text "available"
# TODO: add two ABSTRACT properties: category and loan_days
#         (use @property and @abstractmethod together, like the Animal example)
# TODO: add a class variable requires_approval = False
# TODO: write __str__ so that printing an item shows something like:
#         #001 Phone charger [Daily use, 1 day(s)] - owner: Amina
class Item:
    pass


# STEP 3: four child classes
# INHERITANCE: each child extends Item and only sets class variables.
# POLYMORPHISM: each child gives its OWN loan_days.
#
#   Class          category      loan_days   requires_approval
#   DailyItem      "Daily use"   1           False
#   HouseholdItem  "Household"   3           False
#   StudyItem      "Study"       7           False
#   SpecialItem    "Special"     1           True
#
# TODO: replace each "pass" below with the right class variables.
class DailyItem(Item):
    pass


class HouseholdItem(Item):
    pass


class StudyItem(Item):
    pass


class SpecialItem(Item):
    pass


# STEP 4: test your work
# TODO: under the line below, create a FakeOwner class with a name attribute,
#       make a DailyItem and a SpecialItem, and print them with their
#       loan_days and requires_approval.
# TODO: also try Item("x", owner) and check that you get a TypeError.
if __name__ == "__main__":
    pass

# DONE WHEN: your test prints correctly, Item("x", owner) fails, and you can
# explain why Item is abstract and how each child gives its own loan_days.
# HAND OVER: send this file to Francis.
