class TestResult:
    def __init__(self):
        self.runCount = 0
        
    def testStarted(self):
        self.runCount = self.runCount + 1 
    
    def summary(self):
        return "%d run, 0 failed" % self.runCount