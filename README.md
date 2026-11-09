# Hostel_borrowing_System
# Hostel Borrowing System

A Python application where students borrow items from a shared shelf.

## How it works
* Students can borrow items, but there is a limit of 2 active borrows at a time.
* If an item is not returned on time, the system sends warnings and eventually suspends the borrower.
* If an item is lost, the borrower must replace it before borrowing again.

## Project Structure
This project is built using Object-Oriented Programming (OOP) and is split into five files:
* `items.py` - Defines the items that can be borrowed.
* `people.py` - Defines the members, keepers, and loan records.
* `notifiers.py` - Handles the messages and rules for late items.
* `club.py` - The "brain" of the app that holds the rules and connects everything.
* `main.py` - The interactive menu that the user sees.

## Team Contributions
* **Diana Atugonza (`club.py`):** Built the central `Club` class. Implemented the borrowing logic (2-item limit), conflict checking, returning items, and rules for handling lost/broken items.
* **Alvin Mugisha Allan (`items.py`):
* **Iyamumpaye Brenda (`people.py`):
* **Nshemiire Shawn (`notifiers.py`):
* **Francis Wagonda (`main.py`):

## How to Run
Make sure all five files are in the same folder, then run:
`python main.py`