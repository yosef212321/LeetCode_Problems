class Solution:
    def compress(self, chars: List[str]) -> int:
        leftpt, rightpt = 0, 0
        ans = ""
        while rightpt < len(chars):
            count = 0
            while rightpt < len(chars) and chars[leftpt] == chars[rightpt]:
                count += 1
                rightpt += 1
            if count == 1:
                ans += chars[leftpt]
            elif count < 10:
                ans += chars[leftpt]
                ans += str(count)
            else:
                ans += chars[leftpt]
                count = str(count)
                for i in count:
                    ans += str(i)
            leftpt = rightpt
        chars[:] = ans
        return len(chars)



            
            
                

               


