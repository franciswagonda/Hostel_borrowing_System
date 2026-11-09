"""
Program entry point and command line menu.


Run:  python3 main.py

"""
from datetime import timedelta

from club import Club, MAX_ACTIVE_LOANS
from items import DailyItem, HouseholdItem, StudyItem, SpecialItem
from people import Member, Keeper
from notifiers import ConsoleNotifier, WhatsAppNotifier, SmsNotifier


def ask(prompt):
    try:
        return input(prompt).strip()
    except EOFError:
        print()
        raise SystemExit


def pick(options, label):
    if not options:
        print(f"No {label} to choose from.")
        return None
    for n, o in enumerate(options, 1):
        print(f"  {n}. {o}")
    c = ask(f"Choose {label} number (Enter to cancel): ")
    if c.isdigit() and 1 <= int(c) <= len(options):
        return options[int(c) - 1]
    print("Cancelled.")
    return None


def show_items(club):
    items = club.available_items()
    print("\nAVAILABLE ITEMS")
    if not items:
        print("  Nothing is available right now.")
    for i in items:
        flag = "  (needs keeper approval)" if i.requires_approval else ""
        print(f"  {i}{flag}")


def borrow_flow(club):
    member = pick(club.members, "member")
    if not member:
        return
    ok, why = club.check_member(member)
    if not ok:
        print(f"Cannot borrow: {why}.")
        return
    print(f"{member.name} is using {club.active_count(member)} of {MAX_ACTIVE_LOANS} borrow slots.")
    items = [i for i in club.available_items() if i.owner is not member]
    item = pick(items, "item to borrow")
    if not item:
        return
    approved = True
    if item.requires_approval:
        approved = ask(f"Keeper, approve '{item.name}' for {member.name}? (y/n): ").lower() == "y"
    ok, msg = club.borrow(member, item, approved)
    print(msg)
    if ok:
        print(f"{member.name} now has {club.active_count(member)} of {MAX_ACTIVE_LOANS} borrow slots used.")


def return_flow(club):
    if not club.active_loans():
        print("Nothing is out right now. Borrow something first (option 2).")
        return
    loan = pick(club.active_loans(), "loan to return")
    if loan:
        print(club.give_back(loan))


def show_loans(club):
    print(f"\nTODAY: {club.today}")
    loans = club.active_loans()
    if not loans:
        print("  No items are out right now.")
    for l in loans:
        late = l.days_late(club.today)
        status = f"OVERDUE by {late} day(s)" if late else "on time"
        print(f"  {l.item.name} -> {l.member.name}, due {l.due} ({status})")


def resolve_flow(club):
    if not club.overdue_loans():
        print("No overdue loans. Use option 8 to move the calendar forward and make one late.")
        return
    loan = pick(club.overdue_loans(), "overdue loan to resolve")
    if not loan:
        return
    print("\nHow was it resolved?")
    print("  1. Borrower returned it now")
    print("  2. Owner agrees to an extension")
    print("  3. Item is lost / broken (borrower must replace)")
    c = ask("Choose: ")
    if c == "1":
        print(club.give_back(loan))
    elif c == "2":
        days = ask("Extra days (1-3): ")
        if days.isdigit() and 1 <= int(days) <= 3:
            club.extend(loan, int(days))
            print(f"Extended. New due date: {loan.due}.")
        else:
            print("Extension must be 1 to 3 days.")
    elif c == "3":
        club.mark_lost(loan)
        print(f"'{loan.item.name}' marked lost. {loan.member.name} cannot borrow until it is replaced.")
    else:
        print("Cancelled.")


def replacement_flow(club):
    owing = [m for m in club.members if m.owes]
    if not owing:
        print("Nobody owes a replacement. Mark an item as lost first (option 6, then 3).")
        return
    m = pick(owing, "member who is replacing an item")
    if m:
        print(club.confirm_replacement(m))


def advance_flow(club):
    n = ask("Move the calendar forward by how many days? ")
    if n.isdigit() and int(n) > 0:
        club.today += timedelta(days=int(n))
        print(f"Today is now {club.today}.")
        if club.overdue_loans():
            print("Some items are overdue. Use option 5 to run the conflict check.")
    else:
        print("Enter a positive number.")


def register_flow(club):
    name, room = ask("Name: "), ask("Room: ")
    if name and room:
        club.members.append(Member(name, room))
        print(f"Welcome, {name}!")
    else:
        print("Name and room are required.")


def add_item_flow(club):
    owner = pick(club.members, "owner")
    if not owner:
        return
    kinds = [DailyItem, HouseholdItem, StudyItem, SpecialItem]
    kind = pick([f"{k.category} ({k.loan_days} day)" for k in kinds], "item type")
    if not kind:
        return
    name = ask("Item name: ")
    if name:
        cls = kinds[[f"{k.category} ({k.loan_days} day)" for k in kinds].index(kind)]
        club.items.append(cls(name, owner))
        print(f"Added '{name}'.")


def members_list(club):
    print("\nMEMBERS")
    for m in club.members:
        notes = []
        if isinstance(m, Keeper):
            notes.append("KEEPER")
        if m.suspended_until and club.today <= m.suspended_until:
            notes.append(f"suspended until {m.suspended_until}")
        if m.owes:
            notes.append(f"owes: {m.owes.name}")
        print(f"  {m}  late returns: {m.late_returns}  {' | '.join(notes)}")


def seed(club):
    amina = Keeper("Amina", "A12")
    brian, cathy, dan = Member("Brian", "B07"), Member("Cathy", "C03"), Member("Dan", "A15")
    club.members += [amina, brian, cathy, dan]
    club.items += [
        DailyItem("Phone charger", amina), DailyItem("Calculator", brian),
        HouseholdItem("Iron box", cathy), HouseholdItem("Kettle", dan),
        StudyItem("Law textbook", brian), SpecialItem("Formal shoes", cathy),
    ]
    # Demo situation so every menu option has something to work on from the start
    def lend(member, item_name, days_ago):
        item = next(i for i in club.items if i.name == item_name)
        club.borrow(member, item)
        loan = club.loans[-1]
        loan.start = club.today - timedelta(days=days_ago)
        loan.due = loan.start + timedelta(days=item.loan_days)
        return loan

    lend(brian, "Phone charger", 5)    # due 4 days ago -> overdue (warning level)
    lend(cathy, "Kettle", 1)           # on time
    lend(dan, "Calculator", 9)         # overdue (suspension level)
    lost = lend(cathy, "Law textbook", 4)
    club.mark_lost(lost)               # Cathy lost it and must replace it
    cathy.late_returns = 1


MENU = """
===== HOSTEL BORROWING CLUB =====
 1. Show available items
 2. Borrow an item
 3. Return an item
 4. Show items currently out
 5. Run conflict check (overdue items)
 6. Resolve an overdue loan
 7. Confirm a replacement of a lost item
 8. Move calendar forward (to test late returns)
 9. Show members
10. Register new member
11. Add an item to the shelf
12. Change how members are notified
 0. Exit"""


def choose_notifier():
    """DUCK TYPING: the three notifiers are different classes with no shared parent."""
    options = {"1": ConsoleNotifier, "2": WhatsAppNotifier, "3": SmsNotifier}
    while True:
        print("\nHow should members be notified?  1 = notice board  2 = WhatsApp  3 = SMS")
        c = ask("Choose 1, 2 or 3: ")
        if c in options:
            notifier = options[c]()
            print(f"Notifications will now be sent by: {notifier.name}")
            return notifier
        print("Please type 1, 2 or 3.")


def change_notifier(club):
    club.notifier = choose_notifier()


def main():
    # DUCK TYPING: swap in any notifier, the Club does not mind.
    club = Club(choose_notifier())
    seed(club)
    actions = {
        "1": show_items, "2": borrow_flow, "3": return_flow, "4": show_loans,
        "5": lambda c: c.run_conflict_check(), "6": resolve_flow, "7": replacement_flow,
        "8": advance_flow, "9": members_list, "10": register_flow, "11": add_item_flow,
        "12": change_notifier,
    }
    while True:
        print(MENU)
        print(f"(Notifications: {club.notifier.name})")
        c = ask("Choose: ")
        if c == "0":
            print("Goodbye!")
            break
        action = actions.get(c)
        action(club) if action else print("Please choose a number from the menu.")


if __name__ == "__main__":
    main()