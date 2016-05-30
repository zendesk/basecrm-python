import unittest
import munch
from decimal import *

import basecrm
from basecrm.test.testutils import BaseTestCase

class DealsWithDecimalsServiceTests(BaseTestCase):
    def test_create(self):
        created_deal = self.create_deal_with_decimal_value()
        self.assertEqual(created_deal.value, Decimal('11.12'))

    def test_update(self):
        created_deal = self.create_deal_with_decimal_value()
        created_deal.value = created_deal.value + Decimal('99.99')
        updated_deal = self.client.deals.update(created_deal.id, created_deal)

        self.assertEqual(updated_deal.value, created_deal.value)
