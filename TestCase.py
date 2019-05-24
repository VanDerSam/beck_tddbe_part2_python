from TestResult import TestResult

class TestCase:
    def __init__(self, name):
        self.name = name
        
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()