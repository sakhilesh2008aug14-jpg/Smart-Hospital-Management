# Smart Hospital Management System

A beginner-friendly, menu-driven Python mini-project demonstrating Object-Oriented Programming (OOP) concepts.

## Features

- Register and view patients
- View registered doctors
- Book appointments for registered patients
- Generate consultation and follow-up bills
- Basic input validation
- Two sample doctors are included so the program can be tested immediately

## OOP concepts demonstrated

| Concept | Where it is used |
|---|---|
| Classes and objects | `Person`, `Patient`, `Doctor`, `Hospital`, and bill classes |
| Encapsulation | `Patient.__illness` is private and accessed through `get_illness()` |
| Inheritance | `Patient` and `Doctor` inherit from `Person`; bill types inherit from `Bill` |
| Abstraction | `Person` and `Bill` are abstract base classes |
| Polymorphism | `ConsultationBill` and `FollowUpBill` implement `calculate_bill()` differently |
| Constructors | `__init__()` initializes each object's data |
| Methods | Registration, appointment, display, and billing methods |

## Requirements

- Python 3.8 or later
- No external packages required

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python hospital.py
```

On some systems, use `python3 hospital.py`.

## Sample doctor IDs

- `D101` - Dr. Ananya, Cardiology, consultation fee Rs. 700
- `D102` - Dr. Rahul, Dermatology, consultation fee Rs. 500

Register a patient first before booking an appointment.

## Note

This is an educational console-based project. It uses sample data and does not store records permanently after the program closes. Do not enter real patient or personal information.
