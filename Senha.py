#3
def verificar_senha_forte():
    """
    Programa que verifica se uma senha é forte
    Senha forte: pelo menos 8 caracteres e contém pelo menos um número
    """
    print("Verificador de Senha Forte")
    print("A senha deve ter pelo menos 8 caracteres e conter pelo menos um número")
    print("Digite 'sair' para encerrar\n")
    
    while True:
        senha = input("Digite uma senha: ").strip()
        
        if senha.lower() == 'sair':
            print("Encerrando programa...")
            break
        
        # Verificar comprimento mínimo
        if len(senha) < 8:
            print("❌ Senha fraca! Deve ter pelo menos 8 caracteres.\n")
            continue
        
        # Verificar se contém pelo menos um número
        contem_numero = any(char.isdigit() for char in senha)
        if not contem_numero:
            print("❌ Senha fraca! Deve conter pelo menos um número.\n")
            continue
        
        # Se passou em todas as verificações
        print("✅ Senha forte! Atende aos requisitos de segurança.")
        break

# Executar o programa
verificar_senha_forte()