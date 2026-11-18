class Solution:
    def numberOfSteps(self, num: int) -> int:
        contador = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            contador = contador + 1

        return contador