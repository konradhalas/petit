=====
petit
=====

.. image:: https://travis-ci.org/konradhalas/petit.png
    :target: https://travis-ci.org/konradhalas/petit

Petit is a single metaclass which fixes broken methods names in camel case (like "assertEqual") according to PEP8. Petit stands for "PEP 8 it!".

Usage
-----

Sample usage::

    from unittest import TestCase
    from petit import Petit

    class SthTest(TestCase)

        __metaclass__ = Petit

        def test_sth(self):
            result = (...)
            self.assert_true(result)

