from abc import ABC, abstractmethod
# ABSTRACTION: Item is an abstract base class that cannot be instantiated directly.
from abc import ABC


class Item(ABC):
    _next_id = 1
    requires_approval = False

    def __init__(self, name, owner):
        self.item_id = Item._next_id
        Item._next_id += 1
        self.name = name
        self.owner = owner
        self.status = "available"

    @property
    @abstractmethod
    def category(self):
        """Must return the category string."""
        pass

    @property
    @abstractmethod
    def loan_days(self):
        """Must return the number of loan days."""
        pass

    def __str__(self):
        return f"#{self.item_id:03d} {self.name} [{self.category}, {self.loan_days} day(s)] owner: {self.owner.name}"
    
# INHERITANCE & POLYMORPHISM: Each child fills in its specific category, loan_days, and approval rules.

class DailyItem(Item):
    category = "Daily use"
    loan_days = 1
    requires_approval = False


class HouseholdItem(Item):
    category = "Household"
    loan_days = 3
    requires_approval = False


class StudyItem(Item):
    category = "Study"
    loan_days = 7
    requires_approval = False


class SpecialItem(Item):
    category = "Special"
    loan_days = 1
    requires_approval = True

if __name__ == "__main__":
    class FakeOwner:
        name = "Amina"

    # Testing child classes
    items = [
        DailyItem("Phone charger", FakeOwner()),
        SpecialItem("Formal shoes", FakeOwner())
    ]

    for i in items:
        print(i, i.loan_days, i.requires_approval)

    # Testing abstract class restriction (should raise TypeError)
    try:
        Item("x", FakeOwner())
        print("FAIL: Item class should not be directly instantiated!")
    except TypeError:
        print("SUCCESS: Attempting to create Item() raised a TypeError as expected.")