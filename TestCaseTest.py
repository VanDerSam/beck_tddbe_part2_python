from WasRun import WasRun
from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite

class TestCaseWithBrokenSetupMethod(TestCase):
    def setUp(self):
        raise Exception
    
    def testMethod1(self):
        pass
    
class TestClassWith2TestMethods(TestCase):
    def testMethod1(self):
        a = 1 + 1
    
    def testMethod2(self):
        b = 2 + 2

class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()
    
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
        
    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())
        
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
        
    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())
        
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())
        
    def testFailedButSetupAndTeardown(self):
        # This test for Exercise 1 (rest of the ToDo list)
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("setUp tearDown " == test.log)
        
    def testFailedInSetup(self):
        # This test for Exercise 2 (rest of the ToDo list)
        test = TestCaseWithBrokenSetupMethod("testMethod1")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
        
    def testSuiteFromClass(self):
        # This test for Exercise 3 (rest of the ToDo list)
        objectWithTests = TestClassWith2TestMethods("testMethod1")
        suite = TestSuite().createSuiteFromTestClass(objectWithTests)
        assert(len(suite.tests) == 2)
suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())
# TestSuite for exercises
suite = TestSuite()
suite.add(TestCaseTest("testFailedButSetupAndTeardown"))
suite.add(TestCaseTest("testFailedInSetup"))
suite.add(TestCaseTest("testSuiteFromClass"))
result = TestResult()
suite.run(result)
print("For exercises: " + result.summary())