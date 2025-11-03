# # ################### unittest for calculator #######################


# import sys
# import os
# import unittest

# # Get the path to the project's root directory
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(project_root)

# from src import calculator


# class TestCalculator(unittest.TestCase):

#     def test_fun1(self):
#         self.assertEqual(calculator.fun1(2, 3), 5)
#         self.assertEqual(calculator.fun1(5, 0), 5)
        
#         self.assertEqual(calculator.fun1(-1, 1), 0)
#         self.assertEqual(calculator.fun1(-1, -1), -2)

#     def test_fun2(self):
#         self.assertEqual(calculator.fun2(2, 3), -1)
#         self.assertEqual(calculator.fun2(5, 0), 5)
#         self.assertEqual(calculator.fun2(-1, 1), -2)
#         self.assertEqual(calculator.fun2(-1, -1), 0)

#     def test_fun3(self):
#         self.assertEqual(calculator.fun3(2, 3), 6)
#         self.assertEqual(calculator.fun3(5, 0), 0)
#         self.assertEqual(calculator.fun3(-1, 1), -1)
#         self.assertEqual(calculator.fun3(-1, -1), 1)

#     def test_fun4(self):
#         self.assertEqual(calculator.fun4(2, 3, 5), 10)
#         self.assertEqual(calculator.fun4(5, 0, -1), 4)
#         self.assertEqual(calculator.fun4(-1, -1, -1), -3)
#         self.assertEqual(calculator.fun4(-1, -1, 100), 98)



# if __name__ == '__main__':
#     unittest.main()

############################################################

#unittest for shoppy cart

############################################################

import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import shopping_cart


class TestShoppingCart(unittest.TestCase):
    """Test cases for shopping cart functions"""

    def test_calculate_subtotal(self):
        """Test subtotal calculation"""
        self.assertEqual(shopping_cart.calculate_subtotal([10, 20, 30]), 60)
        self.assertEqual(shopping_cart.calculate_subtotal([5.99, 3.50, 2.01]), 11.50)
        self.assertEqual(shopping_cart.calculate_subtotal([100]), 100)
        self.assertEqual(shopping_cart.calculate_subtotal([]), 0.0)

    def test_apply_discount(self):
        """Test discount application"""
        self.assertEqual(shopping_cart.apply_discount(100, 10), 90.0)
        self.assertEqual(shopping_cart.apply_discount(50, 20), 40.0)
        self.assertEqual(shopping_cart.apply_discount(200, 0), 200.0)
        self.assertEqual(shopping_cart.apply_discount(100, 100), 0.0)

    def test_calculate_tax(self):
        """Test tax calculation"""
        self.assertEqual(shopping_cart.calculate_tax(100, 10), 10.0)
        self.assertEqual(shopping_cart.calculate_tax(50, 8.5), 4.25)
        self.assertEqual(shopping_cart.calculate_tax(200, 0), 0.0)
        self.assertEqual(shopping_cart.calculate_tax(75, 6), 4.5)

    def test_calculate_total(self):
        """Test total calculation with discount and tax"""
        self.assertEqual(shopping_cart.calculate_total(100, 10, 10), 99.0)
        self.assertEqual(shopping_cart.calculate_total(200, 20, 8), 172.8)
        self.assertEqual(shopping_cart.calculate_total(100, 0, 0), 100.0)
        self.assertEqual(shopping_cart.calculate_total(50, 10, 5), 47.25)

    def test_apply_coupon(self):
        """Test coupon application"""
        # Percentage coupon
        self.assertEqual(shopping_cart.apply_coupon(100, 15, is_percentage=True), 85.0)
        self.assertEqual(shopping_cart.apply_coupon(200, 10, is_percentage=True), 180.0)
        
        # Fixed amount coupon
        self.assertEqual(shopping_cart.apply_coupon(100, 25, is_percentage=False), 75.0)
        self.assertEqual(shopping_cart.apply_coupon(80, 20, is_percentage=False), 60.0)
        
        # Coupon exceeds subtotal
        self.assertEqual(shopping_cart.apply_coupon(50, 60, is_percentage=False), 0.0)

    def test_calculate_shipping(self):
        """Test shipping calculation"""
        # Below threshold
        self.assertEqual(shopping_cart.calculate_shipping(50, 10, 100), 10.0)
        self.assertEqual(shopping_cart.calculate_shipping(99.99, 15, 100), 15.0)
        
        # Above threshold - free shipping
        self.assertEqual(shopping_cart.calculate_shipping(150, 10, 100), 0.0)
        self.assertEqual(shopping_cart.calculate_shipping(200, 5, 75), 0.0)
        
        # Exactly at threshold
        self.assertEqual(shopping_cart.calculate_shipping(100, 10, 100), 0.0)

    def test_count_items(self):
        """Test item counting"""
        self.assertEqual(shopping_cart.count_items([1, 2, 3]), 6)
        self.assertEqual(shopping_cart.count_items([5, 5, 5]), 15)
        self.assertEqual(shopping_cart.count_items([]), 0)
        self.assertEqual(shopping_cart.count_items([10]), 10)
        self.assertEqual(shopping_cart.count_items([2, 4, 6, 8]), 20)

    def test_calculate_average_price(self):
        """Test average price calculation"""
        self.assertEqual(shopping_cart.calculate_average_price([10, 20, 30]), 20.0)
        self.assertEqual(shopping_cart.calculate_average_price([5, 5, 5]), 5.0)
        self.assertEqual(shopping_cart.calculate_average_price([100]), 100.0)
        self.assertEqual(shopping_cart.calculate_average_price([15, 25]), 20.0)

    # ERROR HANDLING TESTS

    def test_calculate_subtotal_errors(self):
        """Test error handling for calculate_subtotal"""
        with self.assertRaises(ValueError):
            shopping_cart.calculate_subtotal("not a list")
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_subtotal([10, "twenty", 30])
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_subtotal([10, -5, 30])

    def test_apply_discount_errors(self):
        """Test error handling for apply_discount"""
        with self.assertRaises(ValueError):
            shopping_cart.apply_discount("100", 10)
        
        with self.assertRaises(ValueError):
            shopping_cart.apply_discount(-50, 10)
        
        with self.assertRaises(ValueError):
            shopping_cart.apply_discount(100, 150)
        
        with self.assertRaises(ValueError):
            shopping_cart.apply_discount(100, -10)

    def test_calculate_tax_errors(self):
        """Test error handling for calculate_tax"""
        with self.assertRaises(ValueError):
            shopping_cart.calculate_tax("100", 10)
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_tax(-100, 10)
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_tax(100, -5)

    def test_apply_coupon_errors(self):
        """Test error handling for apply_coupon"""
        with self.assertRaises(ValueError):
            shopping_cart.apply_coupon("100", 10)
        
        with self.assertRaises(ValueError):
            shopping_cart.apply_coupon(-50, 10)
        
        with self.assertRaises(ValueError):
            shopping_cart.apply_coupon(100, 150, is_percentage=True)
        
        with self.assertRaises(ValueError):
            shopping_cart.apply_coupon(100, -10)

    def test_calculate_shipping_errors(self):
        """Test error handling for calculate_shipping"""
        with self.assertRaises(ValueError):
            shopping_cart.calculate_shipping("100", 10, 50)
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_shipping(-50, 10, 100)
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_shipping(100, -10, 50)

    def test_count_items_errors(self):
        """Test error handling for count_items"""
        with self.assertRaises(ValueError):
            shopping_cart.count_items("not a list")
        
        with self.assertRaises(ValueError):
            shopping_cart.count_items([1, 2.5, 3])
        
        with self.assertRaises(ValueError):
            shopping_cart.count_items([1, -2, 3])

    def test_calculate_average_price_errors(self):
        """Test error handling for calculate_average_price"""
        with self.assertRaises(ValueError):
            shopping_cart.calculate_average_price("not a list")
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_average_price([])
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_average_price([10, "twenty"])
        
        with self.assertRaises(ValueError):
            shopping_cart.calculate_average_price([10, -5])


if __name__ == '__main__':
    unittest.main()