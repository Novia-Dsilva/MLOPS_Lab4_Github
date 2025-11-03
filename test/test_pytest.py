# ################### pytest for calculator #######################

# import pytest
# from src import calculator

# def test_fun1():
#     assert calculator.fun1(2, 3) == 5
#     assert calculator.fun1(5,0) == 5
#     assert calculator.fun1 (-1, 1) == 0
#     assert calculator.fun1 (-1, -1) == -2


# def test_fun2():
#     assert calculator.fun2(2, 3) == -1
#     assert calculator.fun2(5,0) == 5
#     assert calculator.fun2 (-1, 1) == -2
#     assert calculator.fun2 (-1, -1) == 0

# def test_fun3():
#     assert calculator.fun3(2, 3) == 6
#     assert calculator.fun3(5,0) == 0
#     assert calculator.fun3 (-1, 1) == -1
    
#     assert calculator.fun3 (-1, -1) == 1

# def test_fun4():
#     assert calculator.fun4(2, 3, 5) == 10
#     assert calculator.fun4(5,0, -1) == 4
#     assert calculator.fun4 (-1, -1, -1) == -3
    
#     assert calculator.fun4 (-1, -1, 100) == 98
    
############################################################

#pytest for shoppy cart

############################################################

import pytest
from src import shopping_cart


# Basic tests for calculate_subtotal
def test_calculate_subtotal():
    assert shopping_cart.calculate_subtotal([10, 20, 30]) == 60
    assert shopping_cart.calculate_subtotal([5.99, 3.50, 2.01]) == 11.50
    assert shopping_cart.calculate_subtotal([100]) == 100
    assert shopping_cart.calculate_subtotal([]) == 0.0


# Parametrized tests for calculate_subtotal
@pytest.mark.parametrize("prices, expected", [
    ([10, 20, 30], 60),
    ([5.99, 3.50, 2.01], 11.50),
    ([100], 100),
    ([0, 0, 0], 0),
    ([15.75, 24.25], 40.0),
])
def test_calculate_subtotal_parametrized(prices, expected):
    """Parametrized test for subtotal calculation"""
    assert shopping_cart.calculate_subtotal(prices) == expected


# Basic tests for apply_discount
def test_apply_discount():
    assert shopping_cart.apply_discount(100, 10) == 90.0
    assert shopping_cart.apply_discount(50, 20) == 40.0
    assert shopping_cart.apply_discount(200, 0) == 200.0
    assert shopping_cart.apply_discount(100, 100) == 0.0


# Parametrized tests for apply_discount
@pytest.mark.parametrize("subtotal, discount, expected", [
    (100, 10, 90.0),
    (50, 20, 40.0),
    (200, 0, 200.0),
    (100, 50, 50.0),
    (75.50, 25, 56.625),
])
def test_apply_discount_parametrized(subtotal, discount, expected):
    """Parametrized test for discount application"""
    assert shopping_cart.apply_discount(subtotal, discount) == expected


# Basic tests for calculate_tax
def test_calculate_tax():
    assert shopping_cart.calculate_tax(100, 10) == 10.0
    assert shopping_cart.calculate_tax(50, 8.5) == 4.25
    assert shopping_cart.calculate_tax(200, 0) == 0.0


# Parametrized tests for calculate_tax
@pytest.mark.parametrize("amount, tax_rate, expected", [
    (100, 10, 10.0),
    (50, 8.5, 4.25),
    (200, 0, 0.0),
    (75, 6, 4.5),
    (1000, 7.5, 75.0),
])
def test_calculate_tax_parametrized(amount, tax_rate, expected):
    """Parametrized test for tax calculation"""
    assert shopping_cart.calculate_tax(amount, tax_rate) == expected


# Basic tests for calculate_total
def test_calculate_total():
    # Subtotal 100, 10% discount = 90, 10% tax = 9, total = 99
    assert shopping_cart.calculate_total(100, 10, 10) == 99.0
    # Subtotal 200, 20% discount = 160, 8% tax = 12.8, total = 172.8
    assert shopping_cart.calculate_total(200, 20, 8) == 172.8
    # No discount, no tax
    assert shopping_cart.calculate_total(100, 0, 0) == 100.0


# Parametrized tests for calculate_total
@pytest.mark.parametrize("subtotal, discount, tax_rate, expected", [
    (100, 10, 10, 99.0),
    (200, 20, 8, 172.8),
    (100, 0, 0, 100.0),
    (50, 10, 5, 47.25),
])
def test_calculate_total_parametrized(subtotal, discount, tax_rate, expected):
    """Parametrized test for total calculation"""
    assert shopping_cart.calculate_total(subtotal, discount, tax_rate) == expected


# Basic tests for apply_coupon
def test_apply_coupon():
    # Percentage coupon
    assert shopping_cart.apply_coupon(100, 15, is_percentage=True) == 85.0
    # Fixed amount coupon
    assert shopping_cart.apply_coupon(100, 25, is_percentage=False) == 75.0
    # Coupon exceeds subtotal
    assert shopping_cart.apply_coupon(50, 60, is_percentage=False) == 0.0


# Parametrized tests for apply_coupon
@pytest.mark.parametrize("subtotal, coupon_value, is_percentage, expected", [
    (100, 15, True, 85.0),
    (100, 25, False, 75.0),
    (50, 60, False, 0.0),
    (200, 10, True, 180.0),
    (80, 20, False, 60.0),
])
def test_apply_coupon_parametrized(subtotal, coupon_value, is_percentage, expected):
    """Parametrized test for coupon application"""
    assert shopping_cart.apply_coupon(subtotal, coupon_value, is_percentage) == expected


# Basic tests for calculate_shipping
def test_calculate_shipping():
    # Below threshold
    assert shopping_cart.calculate_shipping(50, 10, 100) == 10.0
    # Above threshold - free shipping
    assert shopping_cart.calculate_shipping(150, 10, 100) == 0.0
    # Exactly at threshold
    assert shopping_cart.calculate_shipping(100, 10, 100) == 0.0


# Parametrized tests for calculate_shipping
@pytest.mark.parametrize("subtotal, shipping_rate, threshold, expected", [
    (50, 10, 100, 10.0),
    (150, 10, 100, 0.0),
    (100, 10, 100, 0.0),
    (99.99, 15, 100, 15.0),
    (200, 5, 75, 0.0),
])
def test_calculate_shipping_parametrized(subtotal, shipping_rate, threshold, expected):
    """Parametrized test for shipping calculation"""
    assert shopping_cart.calculate_shipping(subtotal, shipping_rate, threshold) == expected


# Basic tests for count_items
def test_count_items():
    assert shopping_cart.count_items([1, 2, 3]) == 6
    assert shopping_cart.count_items([5, 5, 5]) == 15
    assert shopping_cart.count_items([]) == 0
    assert shopping_cart.count_items([10]) == 10


# Parametrized tests for count_items
@pytest.mark.parametrize("quantities, expected", [
    ([1, 2, 3], 6),
    ([5, 5, 5], 15),
    ([10], 10),
    ([0, 0, 0], 0),
    ([2, 4, 6, 8], 20),
])
def test_count_items_parametrized(quantities, expected):
    """Parametrized test for item counting"""
    assert shopping_cart.count_items(quantities) == expected


# Basic tests for calculate_average_price
def test_calculate_average_price():
    assert shopping_cart.calculate_average_price([10, 20, 30]) == 20.0
    assert shopping_cart.calculate_average_price([5, 5, 5]) == 5.0
    assert shopping_cart.calculate_average_price([100]) == 100.0


# Parametrized tests for calculate_average_price
@pytest.mark.parametrize("prices, expected", [
    ([10, 20, 30], 20.0),
    ([5, 5, 5], 5.0),
    ([100], 100.0),
    ([15, 25], 20.0),
    ([10, 20, 30, 40], 25.0),
])
def test_calculate_average_price_parametrized(prices, expected):
    """Parametrized test for average price calculation"""
    assert shopping_cart.calculate_average_price(prices) == expected


# ERROR HANDLING TESTS

def test_calculate_subtotal_errors():
    """Test error handling for calculate_subtotal"""
    with pytest.raises(ValueError, match="Prices must be a list"):
        shopping_cart.calculate_subtotal("not a list")
    
    with pytest.raises(ValueError, match="All prices must be numbers"):
        shopping_cart.calculate_subtotal([10, "twenty", 30])
    
    with pytest.raises(ValueError, match="Prices cannot be negative"):
        shopping_cart.calculate_subtotal([10, -5, 30])


def test_apply_discount_errors():
    """Test error handling for apply_discount"""
    with pytest.raises(ValueError, match="Subtotal and discount must be numbers"):
        shopping_cart.apply_discount("100", 10)
    
    with pytest.raises(ValueError, match="Subtotal cannot be negative"):
        shopping_cart.apply_discount(-50, 10)
    
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        shopping_cart.apply_discount(100, 150)


def test_calculate_tax_errors():
    """Test error handling for calculate_tax"""
    with pytest.raises(ValueError, match="Amount and tax rate must be numbers"):
        shopping_cart.calculate_tax("100", 10)
    
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        shopping_cart.calculate_tax(-100, 10)
    
    with pytest.raises(ValueError, match="Tax rate cannot be negative"):
        shopping_cart.calculate_tax(100, -5)


def test_apply_coupon_errors():
    """Test error handling for apply_coupon"""
    with pytest.raises(ValueError, match="Subtotal and coupon value must be numbers"):
        shopping_cart.apply_coupon("100", 10)
    
    with pytest.raises(ValueError, match="Subtotal cannot be negative"):
        shopping_cart.apply_coupon(-50, 10)
    
    with pytest.raises(ValueError, match="Percentage coupon cannot exceed 100%"):
        shopping_cart.apply_coupon(100, 150, is_percentage=True)


def test_calculate_shipping_errors():
    """Test error handling for calculate_shipping"""
    with pytest.raises(ValueError, match="All inputs must be numbers"):
        shopping_cart.calculate_shipping("100", 10, 50)
    
    with pytest.raises(ValueError, match="Values cannot be negative"):
        shopping_cart.calculate_shipping(-50, 10, 100)


def test_count_items_errors():
    """Test error handling for count_items"""
    with pytest.raises(ValueError, match="Quantities must be a list"):
        shopping_cart.count_items("not a list")
    
    with pytest.raises(ValueError, match="All quantities must be integers"):
        shopping_cart.count_items([1, 2.5, 3])
    
    with pytest.raises(ValueError, match="Quantities cannot be negative"):
        shopping_cart.count_items([1, -2, 3])


def test_calculate_average_price_errors():
    """Test error handling for calculate_average_price"""
    with pytest.raises(ValueError, match="Prices must be a list"):
        shopping_cart.calculate_average_price("not a list")
    
    with pytest.raises(ValueError, match="Cannot calculate average of empty cart"):
        shopping_cart.calculate_average_price([])
    
    with pytest.raises(ValueError, match="All prices must be numbers"):
        shopping_cart.calculate_average_price([10, "twenty"])
