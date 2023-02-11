class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))[::-1]
        
        res = 1
        slowest = cars[0]
        
        for car in cars[1:]:
            cPos, cSpeed = car
            sPos, sSpeed = slowest
            if ((target - sPos)/ sSpeed) < ((target - cPos)/ cSpeed):
                slowest = car
                res += 1
        
        return res
