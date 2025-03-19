import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all test modules
from tests.test_inventory_item import TestInventoryItem
from tests.test_inventory_manager import TestInventoryManager
from tests.test_search_sort import TestSearchSort


def run_tests():
    """Run all test suites"""
    # Create test suite
    test_suite = unittest.TestSuite()

    # Add test cases
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestInventoryItem))
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestInventoryManager)
    )
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSearchSort))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)


if __name__ == "__main__":
    run_tests()
