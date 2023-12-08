import unittest

from unittest.loader import makeSuite

from test_cases.framework import Test

from test_cases.login_to_the_system import TestLoginPage
from test_cases.log_out import TestLogOut
from test_cases.login_invalid import TestLoginPage
from test_cases.add_a_player import TestAddaPlayer

def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestLogOut))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestAddaPlayer))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())