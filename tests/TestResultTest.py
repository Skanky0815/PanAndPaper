import unittest

from Engine.Test import Result


class TestResultTest(unittest.TestCase):

    def test_is_success(self):
        result: Result = Result(2, 5)

        self.assertTrue(result.is_success())
        self.assertFalse(result.is_critical_success())
        self.assertFalse(result.is_critical_failure())

    def test_is_success_failure(self):
        result: Result = Result(11, 10)

        self.assertFalse(result.is_success())
        self.assertFalse(result.is_critical_success())
        self.assertFalse(result.is_critical_failure())

    def test_is_critical_success(self):
        result: Result = Result(1, 10)

        self.assertTrue(result.is_success())
        self.assertTrue(result.is_critical_success())
        self.assertFalse(result.is_critical_failure())

    def test_is_critical_failure(self):
        result: Result = Result(20, 5)

        self.assertFalse(result.is_success())
        self.assertFalse(result.is_critical_success())
        self.assertTrue(result.is_critical_failure())
