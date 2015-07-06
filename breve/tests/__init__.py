import unittest


# noinspection PyUnresolvedReferences
def testsuite():
    from breve.tests import tags, macros

    suite = unittest.TestSuite()
    suite.addTest(tags.suite())
    suite.addTest(macros.suite())

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='testsuite')
