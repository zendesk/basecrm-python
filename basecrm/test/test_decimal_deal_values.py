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

        client = self.client
        original_request_func = client.http_client.request
        client.http_client.request = lambda *args, **kwargs: (200, {}, munch.Munch(created_deal))

        updated_deal = self.client.deals.update(created_deal.id, created_deal)

        self.assertEqual(updated_deal.value, created_deal.value)

        client.http_client.request = original_request_func
