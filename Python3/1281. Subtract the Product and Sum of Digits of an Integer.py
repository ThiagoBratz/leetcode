class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        soma = 0
        produto = 1

        while n > 0:
            ultimo_digito = n % 10
            soma = soma + ultimo_digito
            produto = produto * ultimo_digito
            n = n // 10

        diferenca = produto - soma
        return diferenca