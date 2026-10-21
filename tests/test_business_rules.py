from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)


def test_license_cost_is_seat_price_times_seats():
    assert round(calculate_license_cost(40.00, 5), 2) == 200.00
    
def test_get_seat_discount_returns_0_for_9_seats_not_education():
    assert get_seat_discount(9, False) == 0.0

def test_get_seat_discount_returns_7_percent_for_10_seats_not_education():  
    assert get_seat_discount(10, False) == 0.07      
           
def test_get_seat_discount_returns_7_percent_for_49_seats_education():
    assert get_seat_discount(49, True) == 0.07
    
def test_get_seat_discount_returns_7_percent_for_50_seats_not_education():
    assert get_seat_discount(50, False) == 0.07
    
def test_get_seat_discount_returns_16_percent_for_50_seats_education():  
    assert get_seat_discount(50, True) == 0.16 
    
seats = 8
price = 50.00
education = False
def test_calculate_license_total_returns_cost_plus_onboarding_fee_when_discounted_cost_is_exactly_400():
    assert round(calculate_license_total(50.00, 8, False), 2) == 460.00
    
def test_calculate_license_total_returns_cost_no_onboarding_fee_when_discounted_cost_is_just_over_400():
    assert round(calculate_license_total(400.01, 1, False), 2) == 400.01
    
def test_needs_contract_review_returns_false_when_total_is_exactly_5000():
    assert needs_contract_review(5000) is False
    
def test_needs_contract_review_returns_true_when_total_is_over_5000():
    assert needs_contract_review(5000.01) is True
    
def test_gets_trainer_returns_false_when_seats_is_24_with_total_2999():
    assert gets_trainer(24, 2999) is False
    
def test_gets_trainer_returns_true_when_seats_is_25_with_total_2999():
    assert gets_trainer(25, 2999) is True 
    
def test_gets_trainer_returns_false_when_seats_is_24_with_total_is_exactly_3000():
    assert gets_trainer(24, 3000) is False   
    
def test_gets_trainer_returns_true_when_seats_is_24_with_total_is_over_3000():                              
    assert gets_trainer(24, 3000.01) is True    
    
def test_total_licensed_returns_sum_for_two_orders():
    orders = [
        {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},
        {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True}, 
    ] 
    assert round(total_licensed(orders), 2) == 2036.70
    
def test_largest_license_returns_company_with_largest_total():
    orders = [                                                                            
        {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},
        {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},  
    ]   
    assert largest_license(orders) == "Upland Farms"
    
def test_largest_license_returns_first_company_on_a_tie(): 
    orders = [                                                                              
        {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},                                                                                                                                                      
        {"company": "Upland Farms", "seat_price": 30.00, "seats": 25, "education": True},                                                                                                      
    ]                                                                                                                                     
    assert largest_license(orders) == "Vega Dental"
    
def test_largest_license_returns_an_empty_string_for_an_empty_list():
    orders = []
    assert largest_license(orders) == ""
    
def test_format_license_line_returns_no_when_both_are_false():
    assert format_license_line("Pine Books", 260.00, False, False) == "Pine Books: $260.00 | contract review: no | trainer: no"

def test_format_license_line_returns_yes_when_both_are_true():
    assert format_license_line("Summit College", 6300.00, True, True) == "Summit College: $6300.00 | contract review: yes | trainer: yes"