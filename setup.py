#!/usr/bin/env python

from setuptools import setup

setup(name='bitfinex-api-module',
      version='0.2.2',
      description='Bitfinex API client.',
      url='https://github.com/QuoineFinancial/bitfinex-api-module',
      packages=['bfxapi', 'bfxapi.models', 'bfxapi.websockets',
                'bfxapi.rest',  'bfxapi.utils', ]
      )
