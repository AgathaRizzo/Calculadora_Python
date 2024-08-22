print("Selecione a operação desejada:")
print("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
resposta = int(input("\nDigite sua opção (1,2,3,4): "))
soma = 0
subtracao = 0
multiplicacao = 0
divisão = 0

def calcularSoma():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: ")) 
    soma = n1 + n2
    print(n1, "+", n2, "=", soma)

def calcularSubtracao():
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("\nDigite o segundo número: "))
    subtracao = n1 - n2
    print(n1, "-", n2, "=", subtracao)
def calcularMultiplicacao():
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("\nDigite o segundo número: "))
    multiplicacao = n1 * n2
    print(n1, "*", n2, "=", multiplicacao)
def calcularDivisao():
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("\nDigite o segundo número: "))
    divisao = n1/n2
    print(n1, "/", n2, "=", divisao)
  
if resposta == 1:
    calcularSoma()
elif resposta == 2:
    calcularSubtracao()
elif resposta == 3:
    calcularMultiplicacao()
elif resposta == 4:
    calcularDivisao()
else:
    print("Escolha uma operação válida!")
