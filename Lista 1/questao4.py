def is_prime(num):  # Função que verifica se o número é primo
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print(is_prime(24))
