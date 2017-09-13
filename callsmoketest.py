__author__ = 'rahul'
 
import unittest
import alibaba
import amazon
import os
import HTMLTestRunner 
 
direct = os.getcwd()
print(direct)

### The file containing the report will be created at path given by direct 
 
class MyTestSuite(unittest.TestCase):
 
    def test_Issue(self):
 
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(alibaba.SearchTests),
            unittest.defaultTestLoader.loadTestsFromTestCase(amazon.SearchTests),
        ])
 
        outfile = open(direct + "\SmokeTest1.html", "w")
 
        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )
 
        runner1.run(smoke_test)
 
 
 
 
 
if __name__ == '__main__':
    unittest.main()