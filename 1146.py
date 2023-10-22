from math import log, trunc
from ulti.functionCallHelper.functionCallHelper import FunctionCallHandler


class SnapshotArray_DataBase:
    def __init__(self, length: int):
        self.array = [0]*length
        self.fullSnapshot = []
        self.archiveRedoLogs = []
        self.redoLogs = []
        self.snapLogs = []
        self.snap_id = -1
        self.currentFullSnapshotID = -1
        self.currentArchiveRedoLogsID = 0

    def set(self, index: int, val: int) -> None:
        self.redoLogs.append((index, val))
        self.array[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.snapLogs.append(
            (self.currentFullSnapshotID, self.currentArchiveRedoLogsID, len(self.redoLogs)))
        if len(self.redoLogs) % 50000 == 0:
            self.fullSnapshot.append(self.array.copy())
            self.archiveRedoLogs.append(self.redoLogs)
            self.currentArchiveRedoLogsID += 1
            self.currentFullSnapshotID += 1
            self.redoLogs = []
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        fullSnapShotID, archiveRedoLogsID, redoLogsLength = self.snapLogs[snap_id]
        array, redoLogs = [], []
        if fullSnapShotID >= 0:
            array = self.fullSnapshot[fullSnapShotID].copy()
        else:
            array = [0]*len(self.array)
        if archiveRedoLogsID < len(self.archiveRedoLogs):
            redoLogs = self.archiveRedoLogs[archiveRedoLogsID]
        else:
            redoLogs = self.redoLogs
        for _index, _val in redoLogs[:redoLogsLength]:
            array[_index] = _val

        return array[index]


class SnapshotArray:
    def __init__(self, length: int):
        self.elementHistory = [{} for _ in range(length)]
        self.currentSnapshot = 0
        for index in range(length):
            self.elementHistory[index][self.currentSnapshot] = 0

    def set(self, index: int, val: int) -> None:
        self.elementHistory[index][self.currentSnapshot] = val

    def snap(self) -> int:
        self.currentSnapshot += 1
        return self.currentSnapshot - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.elementHistory[index]
        keys = list(history.keys())
        left = -1
        right = len(keys)

        for _ in range(trunc(log(right - left, 2))+1):
            mid = (left + right) // 2
            if left == mid:
                break
            if keys[mid] <= snap_id:
                left = mid
            else:
                right = mid

        return history[keys[left]]


def test():
    fc = FunctionCallHandler(
        SnapshotArray, "test/1146/limit.inp", "test/1146/limit.out")
    fc.simulatedAndCompare()
    # out = fc.simulated()
    # print(out == result)


test()
