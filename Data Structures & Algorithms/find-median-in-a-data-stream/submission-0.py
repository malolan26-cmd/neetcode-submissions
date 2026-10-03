class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = len(self.nums)

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.length += 1
        self.nums.sort()

    def findMedian(self) -> float:
        median = 0
        if self.length == 1:
            median = self.nums[0]
            return median

        if self.length % 2 == 1:
            median = self.nums[(self.length)// 2]
            return median

        else:
            median = (self.nums[(self.length // 2) - 1] + self.nums[(self.length // 2)]) / 2
            return median
        
        
        