from TestResult import TestResult

class TestSuite:
    def __init__(self):
        self.tests = []
        
    def add(self, test):
        self.tests.append(test)
        
    def run(self, result):
        for test in self.tests:
            test.run(result)
            
    def createSuiteFromTestClass(self, objectWithTests):
        testMethodList = [func for func in dir(objectWithTests) if callable(getattr(objectWithTests, func)) and func.startswith("test")]
        suite = TestSuite()
        for testMethod in testMethodList:
            suite.add(testMethod)
        return suite