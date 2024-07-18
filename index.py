num1 = input('Digite o primeiro número:')
num2 = input('Digite o segundo número:')


num1 = int(num1)
num2 = int(num2)


soma = num1 + num2
subtração = num1 - num2
multiplicação = num1 * num2
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = 'Indefinida (divisão zero)'

print('A soma entre os números é:', soma)
print('A subtração entre os números é:', subtração)
print('A multiplicação entre os números é:', multiplicação)
print('A divisão entre os números é:', divisao)
