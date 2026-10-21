## 1. Building the project

```bash
cd
pwd
mkdir ism3232_midterm
cd ~/ism3232_midterm
pwd
code .
python3 -m venv .venv
source .venv/bin/activate
which python3
pip install pytest
pip install ruff
pip freeze > requirements.txt
echo '.venv' > .gitgnore
echo '__pycache__/' >> .gitignore
echo '*.pyc' >> .gitignore
touch business_rules.py main.py commands.md README.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
git init
git commit -m 'Midterm setup'
git branch -M main
git remote add origin https://github.com/evanmrusso/ism3232-midterm.git
git push -u origin main
git add .
git commit -m 'Midterm setup'
git push -u origin main
git push -u origin main
git check-ignore .venv/ __pycache__/
git add .
git commit -m "Fix gitignore and remove misspelled file"
git push
printf ".venv/\n__pycache__/\n*.pyc\n" > .gitignore
rm -i .gitgnore
git check-ignore .venv/ __pycache__/
git add .
git commit -m "Fix gitignore and remove misspelled file"
git push
git status
```

## 2. The virtual environment

```bash
which python3
```

```text
/home/evanm/ism3232_midterm/.venv/bin/python3
```

The `.venv/bin/python3` portion of the output shows that Python is running from my project’s virtual environment.

## 3. The project structure

```bash
tree -L 2
```

```text
.
├── README.md
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_business_rules.py

2 directories, 7 files
```

The `.venv` folder exists on my computer but is not in my GitHub repository because `.gitignore` excludes it from Git tracking.

## 4. Every function and test

```bash
rg 'def '
```

```
business_rules.py
13:def calculate_license_cost(seat_price: float, seats: int) -> float:
18:def get_seat_discount(seats: int, education: bool = False) -> float:
28:def calculate_license_total(
43:def needs_contract_review(total: float) -> bool:
48:def gets_trainer(seats: int, total: float) -> bool:
56:def total_licensed(orders: list) -> float:
67:def largest_license(orders: list) -> str:
84:def format_license_line(

tests/test_business_rules.py
13:def test_license_cost_is_seat_price_times_seats():
16:def test_get_seat_discount_returns_0_for_9_seats_not_education():
19:def test_get_seat_discount_returns_7_percent_for_10_seats_not_education():  
22:def test_get_seat_discount_returns_7_percent_for_49_seats_education():
25:def test_get_seat_discount_returns_7_percent_for_50_seats_not_education():
28:def test_get_seat_discount_returns_16_percent_for_50_seats_education():  
34:def test_calculate_license_total_returns_cost_plus_onboarding_fee_when_discounted_cost_is_exactly_400():
37:def test_calculate_license_total_returns_cost_no_onboarding_fee_when_discounted_cost_is_just_over_400():
40:def test_needs_contract_review_returns_false_when_total_is_exactly_5000():
43:def test_needs_contract_review_returns_true_when_total_is_over_5000():
46:def test_gets_trainer_returns_false_when_seats_is_24_with_total_2999():
49:def test_gets_trainer_returns_true_when_seats_is_25_with_total_2999():
52:def test_gets_trainer_returns_false_when_seats_is_24_with_total_is_exactly_3000():
55:def test_gets_trainer_returns_true_when_seats_is_24_with_total_is_over_3000():                              
58:def test_total_licensed_returns_sum_for_two_orders():
65:def test_largest_license_returns_company_with_largest_total():
72:def test_largest_license_returns_first_company_on_a_tie(): 
79:def test_largest_license_returns_an_empty_string_for_an_empty_list():
83:def test_format_license_line_returns_no_when_both_are_false():
86:def test_format_license_line_returns_yes_when_both_are_true():

`business_rules.py` defines 8 functions, and `tests/test_business_rules.py` defines 20 tests.

## 5. Which files print

```bash
rg -l 'print'
```

```
commands.md
main.py
```

`main.py` is the only Python file that prints, because it builds the report; `business_rules.py` is not listed because its functions return values instead of printing them, which lets the tests in `tests/test_business_rules.py` check each result with `assert`.

## 6. The commit history

```bash
git log --oneline
```

```
aedad04 (HEAD -> main, origin/main) Completed test_business_rules.py
9ddc0f1 Main.py completed
769dac2 Finished Business_rules.py
9e0aec2 Fix gitignore and remove misspelled file
64215f4 Midterm setup
```

At that point, the repository had 5 commits.