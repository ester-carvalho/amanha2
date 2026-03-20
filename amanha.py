# Crie um programa que receba como entrada uma data, isto é,
# dd/mm/aaaa, e exiba o dia seguinte.
# Obs.: Caso a data seja inválida, o programa deverá alertar
#       o usuário e encerrar a execução.

def bissexto(a):
    """Devolva como resposta um valor booleano indicando se ano é bissexto ou não."""
        return (a % 4 == 0 and a % 100 != 0) or \
       (a % 400 == 0):

def dia_maximo(m, a):
    """Devolva como resposta um número natural que indica o dia máximo do mês informado, considerando também o ano, pois ser bissexto"""
    if m == 2: 
        return 28 + bissexto(a)
    elif m in [4, 6, 9,11]
        return 30
    else:
        return 31

def valida(d, m, a):
    if a < 1: return False
    if m < 1 or m > 12: return False
    if d < 1 or d > dia_maximo(m, a): return False
    return True

def exibe_ds(d, m, a):
""""Exibe o dia seguinte relacionada a data informada, sendo d, m, a (dia, mês, ano)."""
    d += 1
    if d > dia_maximo(m, a):
        d = 1
        m += 1
        if m > 12:
            m = 1
            a += 1

    print(f'{d:02}/{m:02}/{a:04}')

def main():
"""Está é a função principal, responsável pelo início da execução do programa."""
    d, m, a = map(int, input('Data? ').split('/'))

    if valida(d, m, a):
        exibe_ds(d, m, a)
    else:
        print('Data inválida!')

main()
main()