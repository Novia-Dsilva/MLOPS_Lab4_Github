def calculate_subtotal(prices):
    """
    Calculate the subtotal of all items in the cart.
    
    Args:
        prices (list): List of item prices.
    
    Returns:
        float: Sum of all prices.
    
    Raises:
        ValueError: If prices is not a list or contains non-numeric values.
        ValueError: If any price is negative.
    """
    if not isinstance(prices, list):
        raise ValueError("Prices must be a list.")
    
    if not prices:
        return 0.0
    
    for price in prices:
        if not isinstance(price, (int, float)):
            raise ValueError("All prices must be numbers.")
        if price < 0:
            raise ValueError("Prices cannot be negative.")
    
    return sum(prices)


def apply_discount(subtotal, discount_percent):
    """
    Apply a percentage discount to the subtotal.
    
    Args:
        subtotal (float): Original subtotal amount.
        discount_percent (float): Discount percentage (0-100).
    
    Returns:
        float: Discounted amount.
    
    Raises:
        ValueError: If inputs are not numbers.
        ValueError: If discount is not between 0 and 100.
        ValueError: If subtotal is negative.
    """
    if not isinstance(subtotal, (int, float)) or not isinstance(discount_percent, (int, float)):
        raise ValueError("Subtotal and discount must be numbers.")
    
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100.")
    
    discount_amount = subtotal * (discount_percent / 100)
    return subtotal - discount_amount


def calculate_tax(amount, tax_rate):
    """
    Calculate tax on a given amount.
    
    Args:
        amount (float): Amount to calculate tax on.
        tax_rate (float): Tax rate as a percentage (e.g., 8.5 for 8.5%).
    
    Returns:
        float: Tax amount.
    
    Raises:
        ValueError: If inputs are not numbers.
        ValueError: If amount or tax_rate is negative.
    """
    if not isinstance(amount, (int, float)) or not isinstance(tax_rate, (int, float)):
        raise ValueError("Amount and tax rate must be numbers.")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")
    
    return amount * (tax_rate / 100)


def calculate_total(subtotal, discount_percent, tax_rate):
    """
    Calculate final total after discount and tax.
    
    Args:
        subtotal (float): Original subtotal.
        discount_percent (float): Discount percentage (0-100).
        tax_rate (float): Tax rate percentage.
    
    Returns:
        float: Final total amount.
    
    Raises:
        ValueError: If any input validation fails.
    """
    # Apply discount first
    discounted_amount = apply_discount(subtotal, discount_percent)
    
    # Calculate tax on discounted amount
    tax_amount = calculate_tax(discounted_amount, tax_rate)
    
    # Return final total
    return round(discounted_amount + tax_amount, 2)


def apply_coupon(subtotal, coupon_value, is_percentage=True):
    """
    Apply a coupon code (fixed amount or percentage).
    
    Args:
        subtotal (float): Original subtotal.
        coupon_value (float): Coupon value (amount or percentage).
        is_percentage (bool): True if percentage, False if fixed amount.
    
    Returns:
        float: Amount after coupon applied.
    
    Raises:
        ValueError: If inputs are invalid.
    """
    if not isinstance(subtotal, (int, float)) or not isinstance(coupon_value, (int, float)):
        raise ValueError("Subtotal and coupon value must be numbers.")
    
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    
    if coupon_value < 0:
        raise ValueError("Coupon value cannot be negative.")
    
    if is_percentage:
        if coupon_value > 100:
            raise ValueError("Percentage coupon cannot exceed 100%.")
        return subtotal - (subtotal * (coupon_value / 100))
    else:
        # Fixed amount coupon
        if coupon_value > subtotal:
            return 0.0  # Can't go below zero
        return subtotal - coupon_value


def calculate_shipping(subtotal, shipping_rate, free_shipping_threshold=100):
    """
    Calculate shipping cost. Free shipping if subtotal exceeds threshold.
    
    Args:
        subtotal (float): Cart subtotal.
        shipping_rate (float): Standard shipping cost.
        free_shipping_threshold (float): Minimum amount for free shipping.
    
    Returns:
        float: Shipping cost (0 if free shipping applies).
    
    Raises:
        ValueError: If inputs are not numbers or are negative.
    """
    if not all(isinstance(x, (int, float)) for x in [subtotal, shipping_rate, free_shipping_threshold]):
        raise ValueError("All inputs must be numbers.")
    
    if subtotal < 0 or shipping_rate < 0 or free_shipping_threshold < 0:
        raise ValueError("Values cannot be negative.")
    
    if subtotal >= free_shipping_threshold:
        return 0.0
    
    return shipping_rate


def count_items(quantities):
    """
    Count total number of items in cart.
    
    Args:
        quantities (list): List of item quantities.
    
    Returns:
        int: Total number of items.
    
    Raises:
        ValueError: If quantities is not a list or contains invalid values.
    """
    if not isinstance(quantities, list):
        raise ValueError("Quantities must be a list.")
    
    if not quantities:
        return 0
    
    for qty in quantities:
        if not isinstance(qty, int):
            raise ValueError("All quantities must be integers.")
        if qty < 0:
            raise ValueError("Quantities cannot be negative.")
    
    return sum(quantities)


def calculate_average_price(prices):
    """
    Calculate average price of items in cart.
    
    Args:
        prices (list): List of item prices.
    
    Returns:
        float: Average price.
    
    Raises:
        ValueError: If prices is empty or invalid.
    """
    if not isinstance(prices, list):
        raise ValueError("Prices must be a list.")
    
    if not prices:
        raise ValueError("Cannot calculate average of empty cart.")
    
    for price in prices:
        if not isinstance(price, (int, float)):
            raise ValueError("All prices must be numbers.")
        if price < 0:
            raise ValueError("Prices cannot be negative.")
    
    return sum(prices) / len(prices)