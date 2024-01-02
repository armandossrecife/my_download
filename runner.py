import unittest
from test_util import TestUtil
from test_download import TestDownload
from HtmlTestRunner import HTMLTestRunner

def suite():
    suite = unittest.TestSuite()

    # Add the test cases from each module
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestUtil))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDownload))

    return suite

if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(output='my_testes')
    runner.run(suite())