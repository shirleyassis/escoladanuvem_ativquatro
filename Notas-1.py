#2
def registrar_notas():
    """
    Programa para registrar notas de uma turma e calcular a média
    """
    print("=== REGISTRO DE NOTAS DA TURMA ===")
    print("Digite as notas (0 a 10) ou 'fim' para encerrar\n")
    
    notas = []  # Lista para armazenar as notas válidas
    
    while True:
        try:
            # Solicitar nota
            entrada = input("Digite uma nota (0-10) ou 'fim': ").strip().lower()
            
            # Verificar se o usuário quer encerrar
            if entrada == 'fim':
                break
            
            # Converter para float e validar
            nota = float(entrada)
            
            # Verificar se a nota está no intervalo válido
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} registrada com sucesso!")
            else:
                print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
                
        except ValueError:
            print("Erro: Digite apenas números ou 'fim'. Tente novamente.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}. Tente novamente.")
    
    # Calcular e exibir resultados
    if notas:
        media = sum(notas) / len(notas)
        print(f"\n=== RESULTADOS ===")
        print(f"Total de notas registradas: {len(notas)}")
        print(f"Notas: {notas}")
        print(f"Média da turma: {media:.2f}")
        
        # Estatísticas adicionais
        print(f"Maior nota: {max(notas):.2f}")
        print(f"Menor nota: {min(notas):.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")


