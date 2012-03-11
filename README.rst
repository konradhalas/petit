=====
Petit
=====

Petit is single metaclass which fix broken methods names like "assertEqual" acording to PEP8. Petit stands for "PEP 8 it!".

Usage
-----

Sample usage::

form unittest import TestCase
from petit import Petit

class SthTest(TestCase)

    __metaclass__ = Petit

    def test_sth(self):
        result = (...)
        self.assert_true(result)

