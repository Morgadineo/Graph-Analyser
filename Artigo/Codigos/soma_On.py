
def soma(n: int) -> int:
    """
    Calcula a soma dos n primeiros números naturais, incluindo o 0. Implementado com estruturas de repetição.

    Return:
        Número inteiro referente a soma dos números do intervalo.
    """
    total = 0
    
    for num in range(n):
        total += num

    return total

print(soma(6))


