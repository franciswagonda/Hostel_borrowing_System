"""
notifiers.py  -  OWNER: Nshemiire Shawn
=========================================
Your job: the messages the club sends, and the rules for what happens when
an item is late.
OOP ideas to show: DUCK TYPING, ABSTRACTION, POLYMORPHISM.

Build it one step at a time. Run the file after every step:
    python3 notifiers.py
Do NOT rename anything in this file. Other files use these exact names.
"""

# STEP 1: imports
# TODO: from abc import ABC, abstractmethod
# TODO: from datetime import timedelta


# STEP 2: three notifiers  (DUCK TYPING)
# They must NOT share a parent class. Each one only needs:
#   - a class variable  name
#   - a method          send(self, member, text)
# The member's name is member.name and the room is member.room.
#
#   Class             name           send(...) prints
#   ConsoleNotifier   "Notice board" "   [notice board] Brian: <text>"
#   WhatsAppNotifier  "WhatsApp"     "   [WhatsApp -> room B07] Hi Brian, <text>"
#   SmsNotifier       "SMS"          "   [SMS] Brian: <first 80 characters of text>"
#
# TODO: write the three classes below.
class ConsoleNotifier:
    pass


class WhatsAppNotifier:
    pass


class SmsNotifier:
    pass


# STEP 3: the abstract class ConflictPolicy  (ABSTRACTION)
# TODO: make it inherit from ABC and add two ABSTRACT methods:
#         applies(self, days_late)             -> True or False
#         handle(self, loan, club, notifier)   -> does the action
class ConflictPolicy:
    pass


# STEP 4: three policies  (INHERITANCE + POLYMORPHISM)
# Each extends ConflictPolicy and has a class variable  label.
# Always send messages with  notifier.send(person, text).
#
# ReminderPolicy   label "Level 1 - friendly reminder"
#   applies: 1 to 2 days late
#   handle:  send loan.member: "please return '<item name>'. It was due <due date>."
#
# WarningPolicy    label "Level 2 - formal warning"
#   applies: 3 to 5 days late
#   handle:  if loan.handled_level != 2, add 1 to loan.member.late_returns
#            send loan.member a warning that includes their late_returns count
#            send loan.item.owner a message that the item is late
#
# SuspensionPolicy label "Level 3 - suspension and replacement talk"
#   applies: 6 or more days late
#   handle:  set loan.member.suspended_until to club.today + timedelta(days=7)
#            tell the borrower they are suspended until that date
#            tell loan.item.owner the item is 6+ days late
#
# TODO: write the three classes below.
class ReminderPolicy(ConflictPolicy):
    pass


class WarningPolicy(ConflictPolicy):
    pass


class SuspensionPolicy(ConflictPolicy):
    pass


# STEP 5: test your work
# TODO: under the line below, make fake classes for a person (name, room,
#       late_returns, suspended_until), an item (name, owner), a loan
#       (item, member, due, handled_level) and a club (today).
#       Then loop over the three notifiers and the three policies (with 2, 4
#       and 8 days late) and call policy.handle(...) each time.
#       Also check that ConflictPolicy() raises a TypeError.
if __name__ == "__main__":
    pass

# DONE WHEN: you see nine messages in three styles with no errors, and you can
# explain why the notifiers need no parent class but the policies do.
# HAND OVER: send this file to Diana and Francis.
