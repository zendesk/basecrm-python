import unittest

import basecrm
from basecrm.test.testutils import BaseTestCase

from decimal import *
from basecrm.coercion import Coercion

class TestCoercion(BaseTestCase):
    def test_to_decimal(self):
        self.assertEqual(Coercion.to_decimal(0), Decimal(0))
        self.assertEqual(Coercion.to_decimal("0"), Decimal(0))
        self.assertEqual(Coercion.to_decimal(1.11), Decimal("1.11"))
        self.assertEqual(Coercion.to_decimal("1.11"), Decimal("1.11"))

    def test_to_string(self):
       self.assertEqual(Coercion.to_string(10), "10")
       self.assertEqual(Coercion.to_string(10.10), "10.1")
       self.assertEqual(Coercion.to_string("10.10"), "10.10")
       self.assertEqual(Coercion.to_string(Decimal("10.10")), "10.10")
