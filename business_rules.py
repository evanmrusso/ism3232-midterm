NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.07
EDUCATION_DISCOUNT = 0.16
STANDARD_DISCOUNT_MIN_SEATS = 10
EDUCATION_DISCOUNT_MIN_SEATS = 50
ONBOARDING_FEE = 60.0
ONBOARDING_FEE_MAX_DISCOUNTED_COST = 400.0
CONTRACT_REVIEW_LICENSE_TOTAL_THRESHOLD = 5000.0
DEDICATED_TRAINER_MIN_SEATS = 25
DEDICATED_TRAINER_LICENSE_TOTAL_THRESHOLD = 3000.0


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Returns the license cost before any discount (rule 1)."""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Returns the discount rate as a decimal, so 7% is 0.07 (rules 2 and 3)."""
    if seats >= EDUCATION_DISCOUNT_MIN_SEATS and education:
        return EDUCATION_DISCOUNT
    elif seats >= STANDARD_DISCOUNT_MIN_SEATS:
        return STANDARD_DISCOUNT
    else:
        return NO_DISCOUNT


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """Returns the license total for one order: the discounted cost, plus the onboarding fee when it applies (rule 4). It must call your first two functions."""
    license_cost = calculate_license_cost(seat_price, seats)
    discount_rate = get_seat_discount(seats, education)
    discount_amount = license_cost * discount_rate
    discounted_cost = license_cost - discount_amount

    if discounted_cost <= ONBOARDING_FEE_MAX_DISCOUNTED_COST:
        return discounted_cost + ONBOARDING_FEE
    else:
        return discounted_cost


def needs_contract_review(total: float) -> bool:
    """Returns True when the license total needs a contract review (rule 5), otherwise False."""
    return total > CONTRACT_REVIEW_LICENSE_TOTAL_THRESHOLD


def gets_trainer(seats: int, total: float) -> bool:
    """Returns True when the order gets a dedicated trainer (rule 6), otherwise False."""
    return (
        seats >= DEDICATED_TRAINER_MIN_SEATS
        or total > DEDICATED_TRAINER_LICENSE_TOTAL_THRESHOLD
    )


def total_licensed(orders: list) -> float:
    """Returns the sum of the license totals for every order in the list. It must use a for loop that calls calculate_license_total."""
    total = 0.0
    for order in orders:
        seat_price = order["seat_price"]
        seats = order["seats"]
        education = order["education"]
        total = total + calculate_license_total(seat_price, seats, education)
    return total


def largest_license(orders: list) -> str:
    """Returns the company of the order with the largest license total. If two are tied for largest, it returns the one that comes first in the list. An empty list returns an empty string, "". It must use a for loop that calls calculate_license_total."""
    if not orders:
        return ""
    largest_total = 0.0
    largest_company = ""
    for order in orders:
        seat_price = order["seat_price"]
        seats = order["seats"]
        education = order["education"]
        license_total = calculate_license_total(seat_price, seats, education)
        if license_total > largest_total:
            largest_total = license_total
            largest_company = order["company"]
    return largest_company


def format_license_line(
    company: str, total: float, contract_review: bool, trainer: bool
) -> str:
    """Returns one line of the report, such as Pine Books: $260.00 | contract review: no | trainer: no. Each True/False value is shown as yes or no, and the amount always has two decimal places."""
    if contract_review:
        contract_review_str = "yes"
    else:
        contract_review_str = "no"
    if trainer:
        trainer_str = "yes"
    else:
        trainer_str = "no"
    return f"{company}: ${total:.2f} | contract review: {contract_review_str} | trainer: {trainer_str}"
