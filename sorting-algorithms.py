#!/usr/bin/python
# import math
import random
import time
# import sys
# import getopt
import inspect


class DataSet:
    def __init__(self, seedCount = 0):
        self._seedCount = seedCount

    # O(n) time
    def seedValues(self, seedMin = 0, seedMax = 10000):
        self._outputFuncHeader()
        self._startElapsedTimeMs()
        self._values = []
        for i in range(self._seedCount):
            self._values.append(random.randint(seedMin, seedMax))
        self._finishElapsedTimeMs()

    # O(n^2) time
    def bubblesort(self, doUpdate = False):
        self._outputFuncHeader()
        # copy
        values = list(self._values)
        self._startElapsedTimeMs()
        valuesLen = len(values)
        for i in range(valuesLen):
            for j in range(valuesLen):
                if values[i] < values[j]:
                    self._swapValues(values, i, j)
        self._finishElapsedTimeMs()
        if doUpdate:
            self._values = values

    # getters
    def getSeedCount(self):
        return self._seedCount

    # array utility
    def _swapValues(self, arr, i1, i2):
        tmpValue = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = tmpValue

    # time measurement utility
    def _startElapsedTimeMs(self):
        self.startTime = time.time()

    def _finishElapsedTimeMs(self, doOutput = True):
        elapsedTime = time.time() - self.startTime
        if doOutput:
            print('  -elapsedTime:', round(elapsedTime * 1000, 4), 'ms')
        return elapsedTime

    # display utility
    def _outputFuncHeader(self, outputSeedCount = False):
        callerName = inspect.stack()[1][3]
        if outputSeedCount:
            print('DataSet.' + callerName + '(' + str(self._seedCount) + ')')
        else:
            print('DataSet.' + callerName + '()')

    # debug utility
    def debug(self):
        self._outputFuncHeader()
        print('  -seedCount:', self._seedCount)
        print('  -values:', self._values)


dataSets = []
dataSets.append(DataSet(500))
dataSets.append(DataSet(2000))

for dataSet in dataSets:
    print('\n================ Processing DataSet(' + str(dataSet.getSeedCount()) + ') ================')
    dataSet.seedValues()
    dataSet.bubblesort()
    # dataSet.debug()


print('\n')
