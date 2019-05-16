"""
Module to test rest methods
"""

import os
import asyncio
import unittest
from datetime import datetime
from dateutil.tz import tzutc
from bfxapi.rest.BfxRest import BfxRest


class TestBfxRest(unittest.TestCase):
    """
    Tests for BfxRest module
    """

    API_KEY = os.getenv('BALANCE_TRACER_BITFINEX_KEY')
    API_SECRET = os.getenv('BALANCE_TRACER_BITFINEX_SECRET')


    def test_get_currency_movements(self):
        """
        Test get_currency movements
        """
        loop = asyncio.new_event_loop()
        bfx = BfxRest(self.API_KEY, self.API_SECRET, loop=loop, logLevel='DEBUG')

        movements = asyncio.run(bfx.get_currency_movements('BTC',
                                                           datetime(2015, 9, 1, tzinfo=tzutc()),
                                                           datetime(2019, 5, 1, tzinfo=tzutc())
                                                           )
                                )
        self.assertIsNotNone(movements)

        loop.close()


if __name__ == '__main__':
    unittest.main()
