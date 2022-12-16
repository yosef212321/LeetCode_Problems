class Solution:
    def isPalindrome(self, x: int) -> bool:
        quetient = x
        remainder =""
        if quetient == 0:
            return True
        else:
            if quetient > 0:
                while(quetient > 0):
                    remainder += str(quetient % 10)
                    quetient = quetient // 10
                if x == int(remainder):
                    return True
                else:
                    return False
            else:
                return False

        
                
            

       
