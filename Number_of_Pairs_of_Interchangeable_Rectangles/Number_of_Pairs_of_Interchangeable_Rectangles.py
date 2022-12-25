class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dict = {}
        result = 0
        for width,heigth in rectangles:
            if width/heigth in dict:
                dict[width/heigth] +=1
            else:
                dict[width/heigth] = 1
        for val in dict.values():
            if val > 1:
                result += (val*(val - 1))//2
        return result

