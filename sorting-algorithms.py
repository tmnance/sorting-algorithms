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

    # getters
    def getSeedCount(self):
        return self._seedCount

    # O(n)
    def seedValues(self, seedMin = 0, seedMax = 10000):
        self._outputFuncHeader()
        self._startElapsedTimeMs()
        self._values = []
        for i in range(self._seedCount):
            self._values.append(random.randint(seedMin, seedMax))
        self._finishElapsedTimeMs()

    # average - O(n^2), worst - O(n^2)
    def bubbleSort(self, doUpdate = False):
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

    # average - O(n*log n), worst - O(n^2)
    def quickSort(self, doUpdate = False):
        self._outputFuncHeader()
        # copy
        values = list(self._values)
        self._startElapsedTimeMs()
        # call as separate recursive
        self._quickSort(values, 0, len(values) - 1)
        self._finishElapsedTimeMs()
        if doUpdate:
            self._values = values

    # array utility
    def _swapValues(self, arr, i1, i2):
        # tmpValue = arr[i1]
        # arr[i1] = arr[i2]
        # arr[i2] = tmpValue
        arr[i1], arr[i2] = arr[i2], arr[i1]

    def _quickSort(self, arr, low, high):
        if low < high:
            pivot = self._partition(arr, low, high)
            self._quickSort(arr, low, pivot - 1)
            self._quickSort(arr, pivot + 1, high)

    def _partition(self, arr, low, high):
        pivot = low
        pivotValue = arr[high]
        for i in range(low, high):
            if arr[i] <= pivotValue:
                self._swapValues(arr, i, pivot)
                pivot += 1
        self._swapValues(arr, pivot, high)
        return pivot

    # time measurement utility
    def _startElapsedTimeMs(self):
        self.startTime = time.time()

    def _finishElapsedTimeMs(self, doOutput = True):
        elapsedTime = time.time() - self.startTime
        if doOutput:
            print('  -elapsedTime: ' + str(round(elapsedTime * 1000, 4)) + ' ms')
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
        isSorted = all(self._values[i] <= self._values[i + 1] for i in range(len(self._values) - 1))
        print('  -seedCount: ' + str(self._seedCount))
        print('  -values: ' + str(self._values))
        print('  -isSorted: ' + str(isSorted))


dataSets = []
dataSets.append(DataSet(500))
dataSets.append(DataSet(2000))

for dataSet in dataSets:
    print('\n================ Processing DataSet(' + str(dataSet.getSeedCount()) + ') ================')
    dataSet.seedValues()
    dataSet.bubbleSort()
    dataSet.quickSort()
    # dataSet.debug()


print('\n')
