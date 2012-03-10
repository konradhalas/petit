from unittest import TestCase
from petit import Petit

class PetitTest(TestCase):

    __metaclass__ = Petit

    def test_apply_petit(self):
        class BadClass(object):
            __metaclass__ = Petit

        self.assertEqual(type(BadClass), Petit)

    def test_fix_bad_method_name_in_class(self):
        class BadClass(object):
            __metaclass__ = Petit

            def badMethodName(self):
                pass

        obj = BadClass()

        self.assertTrue(hasattr(obj, 'bad_method_name'))

    def test_fix_bad_method_name_in_base_class(self):

        class BadClass(object):

            def badMethodName(self):
                pass

        class GoodClass(BadClass):
            __metaclass__ = Petit

        obj = GoodClass()

        self.assertTrue(hasattr(obj, 'bad_method_name'))

    def test_is_bad_function_name(self):
        self.assertTrue(Petit.is_bad_function_name('badName'))

    def test_is_good_function_name(self):
        self.assertFalse(Petit.is_bad_function_name('good_name'))

    def test_create_good_function_name_from_camelcase(self):
        self.assertEqual(Petit.create_good_function_name('reallyBadName'), 'really_bad_name')

    def test_create_good_function_name_with_first_upper_charachter(self):
        self.assertEqual(Petit.create_good_function_name('BadName'), 'bad_name')

    def test_it_works(self):
        self.assert_true(True)

