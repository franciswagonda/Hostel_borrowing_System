# Hostel Borrowing Club

A command-line app that helps students in a hostel share items such as chargers, iron boxes, kettles and textbooks. Members lend what they do not need this week and borrow what they need today. The app tracks who has what and handles members who do not return items.

**Tagline:** Borrow it. Use it. Pass it on.

## The story

Brian's charger dies the night before an exam. He does not want to buy a new one, so he checks the club shelf and borrows Amina's phone charger. He also borrows Cathy's iron box for an interview.

Brian then forgets to return the charger. The club does not shout at him. It follows clear steps:

1. **1-2 days late:** a friendly reminder.
2. **3-5 days late:** a formal warning, and the owner is told.
3. **6 or more days late:** Brian is suspended for a week.

Amina, the keeper, meets Brian. He admits he lost the charger. She marks it as lost, and Brian cannot borrow again until he replaces it. When he brings a new charger, the item goes back on the shelf and his suspension ends.

Sharing works because the rules are fair, late returns are handled in steps, and every item comes back.

## Features

- Show all available items
- Borrow an item by choosing a member and then an item from the available list
- Return an item
- See which items are out and which are overdue
- Run a conflict check for overdue items
- Resolve an overdue loan: returned, extended, or lost (the borrower must replace it)
- Confirm a replacement of a lost item
- Register new members and add items to the shelf
- Move the calendar forward to test late returns without waiting
- Change how members are notified (notice board, WhatsApp or SMS) at any time

## Club rules built into the app

- Maximum 2 items per person at a time
- You cannot borrow your own item
- Loan time depends on the item type (see below)
- Special items need the keeper's approval
- Suspended members, and members who owe a replacement, cannot borrow

| Item type | Examples | Loan time |
| --- | --- | --- |
| Daily use | Chargers, calculators | 1 day |
| Household | Iron box, kettle | 3 days |
| Study | Textbooks | 7 days |
| Special | Formal shoes, projector | 1 day, keeper approval |

## How to run

You need Python 3. No other installs are needed.

```bash
python3 main.py
```

At the start you choose how members are notified: notice board, WhatsApp, or SMS. You can change it later with menu option 12.

The app starts with a demo situation so every menu option works straight away: Brian and Dan have overdue items, Cathy lost a textbook and must replace it, and Cathy has one item out on time.

## Try the story

The app starts with Brian's charger already 4 days late, so you can follow the story straight away.

| Step | Menu option |
| --- | --- |
| See the available items | 1 |
| See who has what, with overdue items marked | 4 |
| Run the conflict check (warning for Brian, suspension for Dan) | 5 |
| Mark Brian's overdue charger as lost: choose the loan, then option 3 | 6 |
| Check that Brian is blocked from borrowing | 2 |
| Confirm Brian replaced the charger | 7 |
| See the charger available again | 1 |
| Borrow two items as one member, then try a third (it is blocked) | 2 (three times) |

## Object-oriented ideas used

| Idea | Where it is used |
| --- | --- |
| Abstraction | `Item` and `ConflictPolicy` are abstract classes and cannot be created directly |
| Inheritance | `DailyItem`, `HouseholdItem`, `StudyItem` and `SpecialItem` extend `Item`; `Keeper` extends `Member` |
| Polymorphism | Each item type has its own loan period, and each conflict policy (`ReminderPolicy`, `WarningPolicy`, `SuspensionPolicy`) handles lateness in its own way through the same `handle()` method |
| Duck typing | `ConsoleNotifier`, `WhatsAppNotifier` and `SmsNotifier` share no parent class; the club only needs each one to have a `send()` method |

## Project structure

```
main.py        # menu, starting data and program entry point
club.py        # club rules: borrow, return, 2-item limit, conflict check, lost items
items.py       # Item (abstract) and its four types
people.py      # Member, Keeper and Loan
notifiers.py   # three notifiers (duck typing) and three conflict policies
README.md
```

## Team

| Member | File | What they own |
| --- | --- | --- |
| Alvin Mugisha Allan | `items.py` | `Item` and its types: abstraction, inheritance, polymorphism |
| Iyamumpaye Brenda | `people.py` | `Member`, `Keeper`, `Loan`: inheritance and overdue logic |
| Nshemiire Shawn | `notifiers.py` | Notifiers (duck typing) and conflict policies (polymorphism) |
| Diana Atugonza | `club.py` | Club rules and how the classes work together |
| Francis Wagonda | `main.py` | Menu, starting data and program start |

## Built by

A group project by five members, each building one file from scratch. See the team table above.

## Limits and next steps

- Data is kept in memory only, so it resets every time the app closes.
- Next steps: save records to a file, add a login for keepers, and add a simple web sign-up form.
