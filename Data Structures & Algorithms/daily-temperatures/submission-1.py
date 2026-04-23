class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        output = [0] * len(temperatures)
        for i in range(n - 1):              # last stays 0
            for j in range(i + 1, n):       # <-- use n, not n-1
                if temperatures[j] > temperatures[i]:
                    output[i] = j - i
                    break   # stop at first warmer day
        return output


        