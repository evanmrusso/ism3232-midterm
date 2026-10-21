# ISM3232 Midterm: Cloudstep Software

- **Name:** Evan Russo
- **Version:** 1.0
- **Date:** October 21, 2026

## What This Program Does

This program calculates license totals for Cloudstep Software, which sells its scheduling app by the seat. For each order, it applies the seat discount and the onboarding fee, and flags whether the order needs a contract review or gets a dedicated trainer. It then prints a report with one line per order, followed by a summary of the total, average and largest license, plus how many reviews and trainers are needed.

## Business Rules

1. The license cost is the seat price multiplied by the number of seats.
2. Orders with fewer than 10 seats get no discount; orders with 10 or more seats get 7% off.
3. Education customers with 50 or more seats get 16% off instead of 7%; everyone else with 50 or more seats stays at 7%.
4. A $60 onboarding fee is added when the cost after the discount is $400 or less.
5. A contract review is needed when the license total is more than $5,000.
6. An order gets a dedicated trainer when it has 25 or more seats, or when its license total is more than $3,000.

## How to Run

```bash
git clone https://github.com/evanmrusso/ism3232-midterm.git
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```bash
ruff check .
pytest -v
```

There are 20 tests in `tests/test_business_rules.py`. They cover all eight functions and both sides of every limit in the business rules.

## Files in This Repository

- `.gitignore`: the files and folders Git should not track, such as the virtual environment and caches
- `README.md`: this file, with instructions for running and testing the project
- `business_rules.py`: the constants and eight functions that apply the business rules
- `commands.md`: the terminal record of how the project was built and checked
- `main.py`: the order list, and the code that prints the report
- `requirements.txt`: the packages needed to run and test the project
- `tests/__init__.py`: an empty file that marks `tests` as a package so pytest can import `business_rules`
- `tests/test_business_rules.py`: the 20 pytest tests for the business rules

## AI Use Statement
- I did not use AI on the ism3232 Midterm Exam