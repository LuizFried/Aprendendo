import math
from time import sleep

entrada1 = str(input('Primeira entrada:')).strip().replace(',', '.')
entrada2 = str(input('Segunda entrada:')).strip().replace(',', '.')

try:
    if entrada1.isnumeric():
        entrada1 = int(entrada1)
    else:
        try:
            entrada1 = float(entrada1)
        except ValueError:
            entrada1 = 0

    if entrada2.isnumeric():
        entrada2 = int(entrada2)
    else:
        try:
            entrada2 = float(entrada2)
        except ValueError:
            entrada2 = 0
except:
    print('ERRO')




saida_desejada = 0
peso_entrada = 0.5
peso_entrada2 = 3
aprendizado = 0.01
erro = math.inf
contador = 0

if entrada1 < 0:
    entrada1 = entrada1 * -1
if entrada2 < 0:
    entrada2 = entrada2 * -1


def ativação(soma):
    if soma >= 0:
        return 1
    else:
        return 0


while not erro ==0:
    sleep(0.5)
    contador += 1
    soma = (entrada1 * peso_entrada) + (entrada2 *peso_entrada2)

    print(f'entrada 1: {entrada1}, entrada 2: {entrada2}, Desejado: {saida_desejada},'
          f' peso {peso_entrada:.5f} , {soma}')

    saida = ativação(soma)

    print(f'saida {saida}')

    erro = saida_desejada - saida
    print(f'erro {erro}')

    if not erro == 0:
        peso_entrada = peso_entrada + (aprendizado * entrada1 * entrada2 * erro)
        peso_entrada2 = peso_entrada2 + (aprendizado * entrada1 * entrada2 *erro)

if saida == saida_desejada:
    print(f'Parabéns a Rede_Neural aprendeu com {contador} tentativas')