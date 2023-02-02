class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        list1 = []
        list2 = []
        for x in ranges:
            for i in range(x[0], x[1] + 1):
                list1.append(i)
        for i in range(left, right + 1):
            list2.append(i)
        for x in list2:
            if x not in list1:
                return False
        return True
