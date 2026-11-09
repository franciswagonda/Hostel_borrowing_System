"""
main.py  -  OWNER: Francis Wagonda
====================================
Your job: the screen the user sees. You write the menu and connect each menu
number to the right action. You also join the four other files, so you finish
last. Run the app with:
    python3 main.py

You can build and test STEPS 2, 3 and 5 before the other files are ready.
Do NOT rename anything the other files provide.
"""

# STEP 1: imports  (uncomment each line when that file is ready)
# from datetime import timedelta
# from club import Club, MAX_ACTIVE_LOANS
# from items import DailyItem, HouseholdItem, StudyItem, SpecialItem
# from people import Member, Keeper
# from notifiers import ConsoleNotifier, WhatsAppNotifier, SmsNotifier


# STEP 2: two helper functions (test these first)
# TODO: ask(prompt)
#         shows the prompt and returns what the user typed with spaces removed.
#         If the input ends unexpectedly (EOFError), print a blank line and exit.
# TODO: pick(options, label)
#         empty list -> print "No <label> to choose from." and return None
#         otherwise print the options numbered from 1, ask
#         "Choose <label> number (Enter to cancel): " and return the chosen one.
#         Invalid answer -> print "Cancelled." and return None.


# STEP 3: the menu text
# TODO: MENU = a multi-line text showing:
#   1. Show available items
#   2. Borrow an item
#   3. Return an item
#   4. Show items currently out
#   5. Run conflict check (overdue items)
#   6. Resolve an overdue loan
#   7. Confirm a replacement of a lost item
#   8. Move calendar forward (to test late returns)
#   9. Show members
#  10. Register new member
#  11. Add an item to the shelf
#  12. Change how members are notified
#   0. Exit


# STEP 4: one function per menu number. Each takes club.
# TODO: show_items(club)      1  print club.available_items(); add
#                                "(needs keeper approval)" where requires_approval
# TODO: borrow_flow(club)     2  pick a member; ask club.check_member(member), if no
#                                print the reason and stop; show how many of the 2
#                                slots are used; pick an item the member does not own;
#                                if it needs approval ask the keeper y/n; call
#                                club.borrow(...) and print the message
# TODO: return_flow(club)     3  nothing out -> hint to borrow first; otherwise pick
#                                from club.active_loans() and call club.give_back
# TODO: show_loans(club)      4  print today, then each active loan with its due date
#                                and "OVERDUE by N day(s)" or "on time"
# (5 needs no function: call club.run_conflict_check())
# TODO: resolve_flow(club)    6  nothing overdue -> hint to use option 8; otherwise
#                                pick an overdue loan and offer: 1 returned now,
#                                2 extension of 1-3 days, 3 lost or broken
# TODO: replacement_flow(club) 7 pick from members whose owes is set; call
#                                club.confirm_replacement(member)
# TODO: advance_flow(club)    8  ask how many days (positive whole number only);
#                                club.today += timedelta(days=n)
# TODO: members_list(club)    9  print each member with late returns, KEEPER for
#                                keepers (use isinstance), suspension date, what they owe
# TODO: register_flow(club)   10 ask name and room, add a Member to club.members
# TODO: add_item_flow(club)   11 pick an owner and an item type, ask the name,
#                                add the item to club.items
# TODO: change_notifier(club) 12 ask which notifier and set club.notifier


# STEP 5: choose_notifier()
# TODO: print the three choices (1 notice board, 2 WhatsApp, 3 SMS), ask until the
#       user types 1, 2 or 3, print "Notifications will now be sent by: <name>"
#       and return the new notifier object.


# STEP 6: seed(club)  -  demo data so every option works from the start
# TODO: members: Amina (a Keeper, room A12), Brian (B07), Cathy (C03), Dan (A15)
# TODO: six items: Phone charger (Daily, Amina), Calculator (Daily, Brian),
#       Iron box (Household, Cathy), Kettle (Household, Dan),
#       Law textbook (Study, Brian), Formal shoes (Special, Cathy)
# TODO: three borrowings with club.borrow, then moved into the past by changing
#       loan.start and loan.due:
#         Brian's charger 5 days ago (overdue)
#         Dan's calculator 9 days ago (very overdue)
#         Cathy's kettle 1 day ago (on time)


# STEP 7: main()
# TODO: create Club(choose_notifier()), call seed(club), then loop forever:
#         print MENU, ask "Choose: ", call the matching function from a dictionary
#         {"1": show_items, ...}. "0" prints "Goodbye!" and stops. Anything else
#         prints "Please choose a number from the menu."
def main():
    pass


if __name__ == "__main__":
    main()

# STEP 8: test. Run python3 main.py and use every option from 1 to 12 once.
# Try typing letters and empty answers too. The app must never crash.
# DONE WHEN: all 12 options work from a fresh start and you can run the demo story.
