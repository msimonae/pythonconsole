# Caculadora Python

print('############################## Python Calculator ################################ \n')

print('Selecione o número da operação desejada : \n')

print('1 - Soma')

print('2 - Subtração')

print('3 - Multiplicação')

print('4 - Divisão \n')

opcao = int(input('Digite a sua opção desejada(1/2/3/4) : '))

if opcao == 1:

	num1 = int(input('\nDigite o primeiro número: '))

	num2 = int(input('\nDigite o segundo número: '))

	soma = lambda num1,num2 : num1 + num2

	print('\n\n{} + {} = {}'.format(num1,num2,soma(num1,num2)))

elif opcao == 2:
	
	num1 = int(input('\nDigite o primeiro número: '))

	num2 = int(input('\nDigite o segundo número: '))

	subtracao = lambda num1,num2 : num1 - num2

	print('\n\n{} - {} = {}'.format(num1,num2,subtracao(num1,num2)))

elif opcao == 3:
	
	num1 = int(input('\nDigite o primeiro número: '))

	num2 = int(input('\nDigite o segundo número: '))

	multiplicacao = lambda num1,num2 : num1 * num2

	print('\n\n{} x {} = {}'.format(num1,num2,multiplicacao(num1,num2)))

elif opcao == 4:
	
	num1 = int(input('\nDigite o primeiro número: '))

	num2 = int(input('\nDigite o segundo número: '))

	divisao = lambda num1,num2 : num1 / num2

	print('\n\n{} / {} = {}'.format(num1,num2,divisao(num1,num2)))

else:
	print('Opção Inválida !')
	



