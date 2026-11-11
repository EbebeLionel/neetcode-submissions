class MinStack:

    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:
        self.array.append(val)

    def pop(self) -> None:
        n = len(self.array)
        if not self.array:
            self.array = self.array
        else:
            self.array = self.array[:n - 1]

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        minVal = float('inf')
        for num in self.array:
            if num < minVal:
                minVal = num

        return minVal
