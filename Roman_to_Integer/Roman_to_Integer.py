class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        roman_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i = 0
        while(i < len(s)):
            if s[i] == "I":
                if i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                    sum +=(roman_to_int[s[i+1]] - roman_to_int[s[i]])
                    i +=2
                else:
                    sum +=roman_to_int[s[i]]
                    i +=1
            elif s[i] == "V":
                sum +=roman_to_int[s[i]]
                i +=1
            elif s[i] == "X":
                if i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                    sum +=(roman_to_int[s[i+1]] - roman_to_int[s[i]])
                    i +=2
                else:
                    sum +=roman_to_int[s[i]]
                    i +=1
            elif s[i] == "L":
                sum +=roman_to_int[s[i]]
                i +=1
            elif s[i] == "C":
                if i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                    sum +=(roman_to_int[s[i+1]] - roman_to_int[s[i]])
                    i +=2
                else:
                    sum +=roman_to_int[s[i]]
                    i +=1
            elif s[i] == "D":
                sum +=roman_to_int[s[i]]
                i +=1
            elif s[i] == "M":
                sum +=roman_to_int[s[i]]
                i +=1
            else:
                pass
        return sum   
