from django.test import TestCase
from faker import Faker

fake = Faker()


class BaseTestCase(TestCase):
    """
    Spice Base Test case, need to be implement in every test case
    """

    def setUp(self) -> None:
        """
        Run before test
        """
        pass

    def tearDown(self) -> None:
        """
        Run after test
        """
        pass
