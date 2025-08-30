#4
def verificar_par_impar():
    """
    Programa que verifica se números são pares ou ímpares
    e conta a quantidade de cada tipo
    """
    print("Verificador de Números Pares e Ímpares")
    print("Digite números inteiros ou 'fim' para encerrar\n")
    
    pares = 0
    impares = 0
    
    while True:
        entrada = input("Digite um número: ").strip()
        
        if entrada.lower() == 'fim':
            break
        
        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                print(f"✅ {numero} é PAR")
                pares += 1
            else:
                print(f"✅ {numero} é ÍMPAR")
                impares += 1
                
        except ValueError:
            print("❌ Erro: Digite apenas números inteiros ou 'fim'")
    
    # Exibir resultados finais
    print(f"\n=== RESULTADOS ===")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")
    print(f"Total de números: {pares + impares}")

# Executar o programa
verificar_par_impar()