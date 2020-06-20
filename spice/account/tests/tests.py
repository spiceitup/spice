from common.tests import BaseTestCase, fake


class ModelAccount(BaseTestCase):
    def setUp(self) -> None:
        self.name = fake.name()