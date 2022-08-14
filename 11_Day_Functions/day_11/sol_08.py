# def sumatoria(numero):
#     if numero == 2:
#         return numero / (numero - 1)
#     else:
#         return (numero / (numero - 1)) + sumatoria(numero - 1)
#
#
# print(sumatoria(5))


def sumatoria(n):
    if n == 1:
        return 1 / (n*(n + 1))
    else:
        return (1 / n*(n + 1)) + (sumatoria(n - 1))


print(sumatoria(5))
