from abc import ABC, abstractmethod
from datetime import timedelta


# ---------------------------------------------------------------
# NOTIFIERS - DUCK TYPING
# These three classes share NO parent class. Each one simply has a
# class variable `name` and a method send(member, text). Any object
# with those two things can be used as a notifier ("if it quacks
# like a duck, it is a duck").
# NSHEMIIRE SHAWN S5B13/023---------------------------------------------------------------

class ConsoleNotifier:
    """DUCK TYPING: no parent class, only name + send()."""
    name = "Notice board"

    def send(self, member, text):
        print(f"[notice board] {member.name}: {text}")


class WhatsAppNotifier:
    """DUCK TYPING: no parent class, only name + send()."""
    name = "WhatsApp"

    def send(self, member, text):
        print(f"[WhatsApp -> room {member.room}] Hi {member.name}, {text}")


class SmsNotifier:
    """DUCK TYPING: no parent class, only name + send()."""
    name = "SMS"

    def send(self, member, text):
        print(f"[SMS] {member.name}: {text[:80]}")


# ---------------------------------------------------------------
# CONFLICT POLICIES - ABSTRACTION + POLYMORPHISM
# ---------------------------------------------------------------

class ConflictPolicy(ABC):
    """ABSTRACTION: cannot be created directly. Every policy MUST
    say when it applies and what it does."""

    @abstractmethod
    def applies(self, days_late):
        ...

    @abstractmethod
    def handle(self, loan, club, notifier):
        ...


class ReminderPolicy(ConflictPolicy):
    """POLYMORPHISM: Level 1 - a friendly reminder (1 to 2 days late)."""
    label = "Level 1 - friendly reminder"

    def applies(self, days_late):
        return 1 <= days_late <= 2

    def handle(self, loan, club, notifier):
        notifier.send(
            loan.member,
            f"please return '{loan.item.name}'. It was due {loan.due}."
        )


class WarningPolicy(ConflictPolicy):
    """POLYMORPHISM: Level 2 - a formal warning (3 to 5 days late)."""
    label = "Level 2 - formal warning"

    def applies(self, days_late):
        return 3 <= days_late <= 5

    def handle(self, loan, club, notifier):
        # Count the late return only once for this loan
        if loan.handled_level != 2:
            loan.member.late_returns += 1
        notifier.send(
            loan.member,
            f"this is a formal warning. '{loan.item.name}' is overdue "
            f"(due {loan.due}). Late returns so far: "
            f"{loan.member.late_returns}."
        )
        notifier.send(
            loan.item.owner,
            f"your item '{loan.item.name}' is late. "
            f"{loan.member.name} has not returned it (due {loan.due})."
        )


class SuspensionPolicy(ConflictPolicy):
    """POLYMORPHISM: Level 3 - suspension and replacement talk
    (6 or more days late)."""
    label = "Level 3 - suspension and replacement talk"

    def applies(self, days_late):
        return days_late >= 6

    def handle(self, loan, club, notifier):
        until = club.today + timedelta(days=7)
        loan.member.suspended_until = until
        notifier.send(
            loan.member,
            f"you are suspended until {until} because '{loan.item.name}' "
            f"is badly overdue. Please return it or arrange a replacement."
        )
        notifier.send(
            loan.item.owner,
            f"your item '{loan.item.name}' is 6+ days late. "
            f"{loan.member.name} has been suspended."
        )


# ---------------------------------------------------------------
# TEST - runs only when this file is run directly
# ---------------------------------------------------------------

if __name__ == "__main__":
    from datetime import date

    class P:  # fake person
        def __init__(self, name, room):
            self.name, self.room = name, room
            self.late_returns, self.suspended_until = 0, None

    class FakeItem:
        name = "Phone charger"
        owner = P("Amina", "A12")

    class FakeLoan:
        item = FakeItem()
        member = P("Brian", "B07")
        due = date.today()
        handled_level = None

    class FakeClub:
        today = date.today()

    for n in (ConsoleNotifier(), WhatsAppNotifier(), SmsNotifier()):
        print(f"--- {n.name} ---")
        for days, policy in ((2, ReminderPolicy()),
                             (4, WarningPolicy()),
                             (8, SuspensionPolicy())):
            assert policy.applies(days)
            print(policy.label)
            policy.handle(FakeLoan(), FakeClub(), n)

    # ConflictPolicy is abstract, so this must fail
    try:
        ConflictPolicy()
    except TypeError as e:
        print("OK, TypeError as expected:", e)
