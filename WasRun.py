from TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.wasRun = None
        
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "
        
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "
        
    def tearDown(self):
        self.log = self.log + "tearDown "