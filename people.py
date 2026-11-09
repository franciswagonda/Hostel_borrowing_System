from datetime import timedelta

class Member:
    _next_id = 1

    def __init__(self, name, room):
        self.member_id = Member._next_id
        Member._next_id += 1
        self.name = name
        self.room = room
        self.late_returns = 0
        self.suspended_until = None
        self.owes = None

    def can_borrow(self, today):
        # 1. Check if they owe a lost item
        if self.owes is not None:
            return False, f"must replace lost item: {self.owes.name}"
        
        # 2. Check if they are suspended
        if self.suspended_until is not None and today <= self.suspended_until:
            return False, f"suspended until {self.suspended_until}"
        
        # 3. If all clear, they can borrow
        return True, ""

    def __str__(self):
        return f"{self.name} (room {self.room})"


# INHERITANCE: Keeper extends Member
class Keeper(Member):
    def approve(self, item, borrower):
        return True


class Loan:
    def __init__(self, item, member, start):
        self.item = item
        self.member = member
        self.start = start
        # POLYMORPHISM: Each item type gives its own number of days for the due date
        self.due = start + timedelta(days=item.loan_days)
        self.returned_on = None
        self.handled_level = None

    def days_late(self, today):
        # Returns the number of days late, or 0 if not late
        return max(0, (today - self.due).days)

    @property
    def active(self):
        return self.returned_on is None

    def __str__(self):
        return f"{self.item.name} - {self.member.name} (due {self.due})"



# TESTING BLOCK (Step 5 from the guide)

if __name__ == "__main__":
    from datetime import date, timedelta

    class FakeItem:
        name = "Phone charger"
        loan_days = 1

    b = Member("Brian", "B07")
    k = Keeper("Amina", "A12")
    
    # Make a loan that started 4 days ago
    loan = Loan(FakeItem(), b, date.today() - timedelta(days=4))
    
    print(b, k, isinstance(k, Member))
    print(loan, loan.days_late(date.today()), loan.active)
    
    # Suspend Brian for 3 days to test can_borrow
    b.suspended_until = date.today() + timedelta(days=3)
    print(b.can_borrow(date.today()))
