from datetime import date, timedelta
from people import Loan
from notifiers import ReminderPolicy, WarningPolicy, SuspensionPolicy

MAX_ACTIVE_LOANS = 2

class Club:
    def __init__(self, notifier):
        self.today = date.today()
        self.items = []
        self.members = []
        self.loans = []
        self.notifier = notifier
        self.policies = [ReminderPolicy(), WarningPolicy(), SuspensionPolicy()]

    #  Step 3: Question Methods 
    def available_items(self):
        return [i for i in self.items if i.status == "available"]

    def active_loans(self):
        return [l for l in self.loans if l.active]

    def overdue_loans(self):
        return [l for l in self.active_loans() if l.days_late(self.today) > 0]

    def active_count(self, member):
        return len([l for l in self.active_loans() if l.member == member])

    # Step 4: Check Member 
    def check_member(self, member):
        # 1. Ask the member if they can borrow
        can_borrow, reason = member.can_borrow(self.today)
        if not can_borrow:
            return False, reason

        # 2. Check if they reached the active limit
        if self.active_count(member) >= MAX_ACTIVE_LOANS:
            return False, f"limit reached: {MAX_ACTIVE_LOANS} active borrows at a time. Return an item first."

        return True, ""

    #  Step 5: Borrowing 
    def borrow(self, member, item, approved=True):
        # Check 1: Is the member allowed to borrow?
        can_borrow, reason = self.check_member(member)
        if not can_borrow:
            return False, reason

        # Check 2: Is the item available?
        if item.status != "available":
            return False, "item is not available"

        # Check 3: Do they already own this item?
        if item.owner == member:
            return False, "this is your own item"

        # Check 4: Does it need approval and they don't have it?
        if item.requires_approval and not approved:
            return False, "keeper did not approve this special item"

        # If all checks pass, create the loan
        new_loan = Loan(item, member, self.today)
        item.status = "on loan"
        self.loans.append(new_loan)

        due_date = new_loan.due.strftime("%Y-%m-%d")
        return True, f"{member.name} borrowed '{item.name}'. Due back {due_date}"

    #  Step 6: Returning 
    def give_back(self, loan):
        loan.returned_on = self.today
        loan.item.status = "available"

        days_late = loan.days_late(self.today)

        # If it was late and hasn't been handled yet
        if days_late > 0 and loan.handled_level is None:
            loan.member.late_returns += 1

        if days_late > 0:
            return f"'{loan.item.name}' returned by {loan.member.name} ({days_late} day(s) late)."
        else:
            return f"'{loan.item.name}' returned by {loan.member.name} on time."

    #  Step 7: Conflict Check 
    def run_conflict_check(self):
        overdue = self.overdue_loans()

        if not overdue:
            print("No conflicts today. Everything borrowed is on time.")
            return

        for loan in overdue:
            days = loan.days_late(self.today)

            # POLYMORPHISM: We just call handle() and each policy does its own thing
            for i, policy in enumerate(self.policies):
                if policy.applies(days):
                    print(f"{loan.member.name} - {loan.item.name} - {days} days late - {policy.label}")
                    policy.handle(loan, self, self.notifier)
                    # Set the handled level to the policy's position in the list (1, 2, or 3)
                    loan.handled_level = i + 1
                    break # Stop checking policies once one applies

    # Step 8: Lost Items 
    def mark_lost(self, loan):
        loan.returned_on = self.today
        loan.item.status = "lost"
        loan.member.owes = loan.item
        loan.member.late_returns += 1

    def confirm_replacement(self, member):
        member.owes.status = "available"
        member.owes = None
        member.suspended_until = None
        return "Item was replaced. Member is cleared."

    def extend(self, loan, days):
        loan.due = loan.due + timedelta(days=days)
        loan.handled_level = None


# This check keeps the file safe if you run it alone, but does nothing when Francis runs the app.
if __name__ == "__main__":
    print("club.py is complete and ready to go! No testing code is running.")
