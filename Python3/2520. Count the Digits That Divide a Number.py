class Solution:
    def countDigits(self, num: int) -> int:
        contador = 0
        numero_original = num

        while num > 0:
            ultimo_digito = num % 10

            if ultimo_digito != 0:
                if numero_original % ultimo_digito == 0:
                    contador = contador + 1

            num = num // 10

        return contador