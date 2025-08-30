#1
def calculadora():
    """
    Calculadora que realiza as quatro operações básicas com tratamento de erros
    """
    print("=== CALCULADORA PYTHON ===")
    print("Operações disponíveis: +, -, *, /")
    print("Digite 'sair' a qualquer momento para encerrar\n")
    
    while True:
        try:
            # Solicitar primeiro número
            num1_input = input("Digite o primeiro número: ").strip().lower()
            if num1_input == 'sair':
                print("Encerrando calculadora...")
                break
            num1 = float(num1_input)
            
            # Solicitar segundo número
            num2_input = input("Digite o segundo número: ").strip().lower()
            if num2_input == 'sair':
                print("Encerrando calculadora...")
                break
            num2 = float(num2_input)
            
            # Solicitar operação
            operacao = input("Digite a operação (+, -, *, /): ").strip().lower()
            if operacao == 'sair':
                print("Encerrando calculadora...")
                break
            
            # Realizar cálculo baseado na operação
            if operacao == '+':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}\n")
                
            elif operacao == '-':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}\n")
                
            elif operacao == '*':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}\n")
                
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero não é permitida!")
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}\n")
                
            else:
                raise ValueError("Erro: Operação inválida! Use apenas +, -, *, /")
            
        except ValueError as e:
            # Tratar erros de entrada não numérica
            if "could not convert string to float" in str(e):
                print("Erro: Por favor, digite apenas números válidos!\n")
            else:
                print(f"{e}\n")
                
        except ZeroDivisionError as e:
            # Tratar divisão por zero
            print(f"{e}\n")
            
        except KeyboardInterrupt:
            # Permitir saída com Ctrl+C
            print("\n\nEncerrando calculadora...")
            break
            
        except Exception as e:
            # Tratar outros erros inesperados
            print(f"Erro inesperado: {e}\n")

# Versão alternativa mais compacta
def calculadora_simples():
    """
    Versão mais compacta da calculadora
    """
    print("=== CALCULADORA SIMPLES ===")
    
    while True:
        try:
            # Obter entradas
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            operacao = input("Operação (+, -, *, /): ").strip()
            
            # Validar e executar operação
            if operacao not in ['+', '-', '*', '/']:
                print("Operação inválida! Use apenas +, -, *, /\n")
                continue
                
            if operacao == '/' and num2 == 0:
                print("Erro: Divisão por zero não é permitida!\n")
                continue
            
            # Calcular resultado
            if operacao == '+': resultado = num1 + num2
            elif operacao == '-': resultado = num1 - num2
            elif operacao == '*': resultado = num1 * num2
            else: resultado = num1 / num2
            
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}\n")
            
        except ValueError:
            print("Erro: Digite apenas números válidos!\n")
        except KeyboardInterrupt:
            print("\nCalculadora encerrada.")
            break

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
    # Para usar a versão simples, descomente a linha abaixo:

    # calculadora_simples()
