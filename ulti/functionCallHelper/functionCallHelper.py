import json


class FunctionCallHandler:
    def __init__(self, functionClassInstance, inputFilePath, outputFilePath):
        f = open(inputFilePath, 'r')
        data = f.read().split('\n')
        f.close()
        self.functionCalls = json.loads(data[0])
        self.functionCallsInput = json.loads(data[1])
        f2 = open(outputFilePath, 'r')
        data = f2.read().split('\n')
        f2.close()
        self.functionCallsResult = json.loads(data[0])
        self.instance = LazyCallable(functionClassInstance)

    def simulated(self):
        out = []
        for i in range(len(self.functionCalls)):
            funcName = self.functionCalls[i]
            funcInput = self.functionCallsInput[i]
            out.append(self.instance.__call__(funcName, funcInput))
        return out

    def simulatedAndCompare(self, verbose=False):
        for i in range(len(self.functionCalls)):
            funcName = self.functionCalls[i]
            funcInput = self.functionCallsInput[i]
            out = self.instance.__call__(funcName, funcInput)
            result = self.functionCallsResult[i]
            if out != result:
                # checkAgain
                self.instance.__call__(funcName, funcInput)
                if verbose:
                    print(
                        f"Step {i} fail, function {funcName} with input {funcInput} return {out} instead of {result}")
                break
        if verbose:
            print("Simulated done")


class LazyCallable(object):
    def __init__(self, m_class):
        self.m_class = m_class
        self.m_object = None

    def __call__(self, name, k):
        if self.m_class.__name__ == name:
            self.m_object = self.m_class(*k)
            return None

        function = getattr(self.m_object, name)
        return function(*k)


if __name__ == "__main__":
    class Solution:
        def __init__(self, name=None):
            self.name = name

        def add(self, x, y):
            return x + y

    fc = FunctionCallHandler(
        Solution, "test.inp", "test.out")
    fc.simulatedAndCompare(verbose=True)
