def decimal_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numeral_romano = ''
    i = 0
    while numero > 0:
        if numero >= valores[i]:
            numeral_romano += simbolos[i]
            numero -= valores[i]
        else:
            i += 1
    return numeral_romano

