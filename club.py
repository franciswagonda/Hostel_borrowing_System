"""
club.py  -  OWNER: Diana Atugonza
===================================
Your job: the brain of the app. It holds the club's rules and decides who can
borrow what. Everything else sends requests to your Club class.

You need people.py (Brenda) and notifiers.py (Shawn) to TEST this file.
Write your code first, test it when their files arrive.
Do NOT rename anything in this file. Other files use these exact names.
"""

# STEP 1: imports and the loan limit
# TODO: from datetime import date, timedelta
# TODO: from people import Loan
# TODO: from notifiers import ReminderPolicy, WarningPolicy, SuspensionPolicy
# TODO: MAX_ACTIVE_LOANS = 2


class Club:
    # STEP 2: __init__(self, notifier)
    # TODO: set these:
    #         self.today     -> date.today()
    #         self.items, self.members, self.loans -> three empty lists
    #         self.notifier  -> the notifier you were given
    #         self.policies  -> [ReminderPolicy(), WarningPolicy(), SuspensionPolicy()]
    def __init__(self, notifier):
        pass

    # STEP 3: the question methods
    # TODO: available_items()   -> items whose status is "available"
    # TODO: active_loans()      -> loans whose active is true
    # TODO: overdue_loans()     -> active loans where days_late(self.today) > 0
    # TODO: active_count(member)-> how many active loans that member has

    # STEP 4: check_member(self, member)  -> returns (True, "") or (False, reason)
    # TODO: ask member.can_borrow(self.today); if it says no, return its answer
    # TODO: if active_count(member) >= MAX_ACTIVE_LOANS, return
    #       (False, "limit reached: 2 active borrows at a time. Return an item first")
    # TODO: otherwise return (True, "")

    # STEP 5: borrow(self, member, item, approved=True)
    #         -> returns (True, message) or (False, reason)
    # Check in this order and stop at the first problem:
    #   1. check_member(member) says no
    #   2. item.status is not "available"      -> "item is not available"
    #   3. item.owner is member                -> "this is your own item"
    #   4. item.requires_approval and not approved
    #                                          -> "keeper did not approve this special item"
    # If all pass:
    # TODO: create Loan(item, member, self.today)
    # TODO: set item.status = "on loan"
    # TODO: add the loan to self.loans
    # TODO: return (True, "Brian borrowed 'Phone charger'. Due back 2026-11-07.")

    # STEP 6: give_back(self, loan)  -> returns a message
    # TODO: set loan.returned_on to today and loan.item.status to "available"
    # TODO: if the loan was late and loan.handled_level is None,
    #       add 1 to loan.member.late_returns
    # TODO: return "'Phone charger' returned by Brian (2 day(s) late)." or "... on time."

    # STEP 7: run_conflict_check(self)   (POLYMORPHISM)
    # TODO: for each overdue loan, work out days_late, then loop through
    #       self.policies. For the policy where applies(days_late) is True:
    #         - print the borrower, item, days late and policy.label
    #         - call policy.handle(loan, self, self.notifier)
    #         - set loan.handled_level to (position in the list) + 1
    # TODO: if nothing is overdue, print
    #       "No conflicts today. Everything borrowed is on time."
    # Notice: you never write if level == 1 ... elif level == 2.
    # You just call handle(), and each policy does its own thing.

    # STEP 8: lost items and extensions
    # TODO: mark_lost(self, loan)
    #         returned_on = today, item.status = "lost",
    #         loan.member.owes = the item, add 1 to loan.member.late_returns
    # TODO: confirm_replacement(self, member)  -> returns a message
    #         item.status = "available", member.owes = None,
    #         member.suspended_until = None
    # TODO: extend(self, loan, days)
    #         add that many days to loan.due, set loan.handled_level = None


# STEP 9: test your work (when people.py and notifiers.py are ready)
# TODO: under the line below, make a Club(ConsoleNotifier()), two Members and a
#       DailyItem. Borrow, return and borrow again. Then try three borrows by
#       one member and check the third fails. Move club.today forward 5 days and
#       run the conflict check. Mark an item lost and check the borrower is blocked.
if __name__ == "__main__":
    pass

# DONE WHEN: a third borrow is blocked, an overdue loan triggers the right
# message, and a lost item blocks the borrower until confirm_replacement runs.
# HAND OVER: send this file to Francis.
