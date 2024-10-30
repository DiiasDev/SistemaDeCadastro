import json

def edita():
 
    nome_arquivo = input("Entre com o nome do arquivo (ola.json): ")

    with open(nome_arquivo, "r+") as arquivo:
        usuarios = json.load(arquivo)

    while True:
        opcao = input(
            "1- Cadastrar\n2- Consultar CPF\n3- Alterar dados de um cliente\n4- Apagar cliente\n5- Mostrar clientes\n6- Sair\n"
        )

        if opcao == "1":
            nome = input("Entre com o nome de usuário: ")
            cpf = input("Entre com o CPF de usuário: ")
            email = input("Entre com o email de usuário: ")
            endereco = input("Entre com o endereço de usuário: ")

            usuario = {"nome": nome, "cpf": cpf, "email": email, "endereco": endereco}
            usuarios.append(usuario)

            # Atualiza o arquivo com os novos dados
            with open(nome_arquivo, "w") as arquivo:
                json.dump(usuarios, arquivo)

            print("Dados armazenados com sucesso...")

            with open(nome_arquivo, "r") as arquivo:
                usuarios = json.load(arquivo)

        elif opcao == "2":
            cpf_consulta = input("Digite o CPF que deseja consultar: ")
            usuario_encontrado = None

            for usuario in usuarios:
                if cpf_consulta == usuario["cpf"]:
                    usuario_encontrado = usuario
                    break  # Encerra o loop ao encontrar o usuário

            if usuario_encontrado:
                print(f"Cliente encontrado: {usuario_encontrado['nome']}")
            else:
                print("Usuário não cadastrado!")
        elif opcao == "3":
                cpf_consulta = input("Digite o CPF do usuário que deseja alterar: ")
                usuario_encontrado = None

                for usuario in usuarios:
                    if cpf_consulta == usuario["cpf"]:
                        usuario_encontrado = usuario
                        break  # Encerra o loop ao encontrar o usuário

                if usuario_encontrado:
                    print(f"Cliente encontrado: {usuario_encontrado['nome']}")
                    print(f"Digite qual dado você deseja alterar")
                    dados = input("1- Nome\n2- CPF\n3- Email\n4- Endereço\n")
                
                    
                    if dados == "1":
                        novo_valor = input(f"Digite o novo valor para Nome : ")
                        usuario["nome"] = novo_valor
                        print(usuario)
                        
                        with open(nome_arquivo, "w") as arquivo:
                            json.dump(usuarios, arquivo)
                    elif dados == '2':
                        novo_valor = input(f"Digite o novo valor para CPF : ")
                        usuario["cpf"] = novo_valor
                        print(usuario)
                        
                        with open(nome_arquivo, "w") as arquivo:
                            json.dump(usuarios, arquivo)
                    elif dados == '3':
                        novo_valor = input(f"Digite o novo valor para Email : ")
                        usuario["email"] = novo_valor
                        print(usuario)
                        
                        with open(nome_arquivo, "w") as arquivo:
                            json.dump(usuarios, arquivo)
                    elif dados == '4':
                        novo_valor = input(f"Digite o novo valor para Endereço : ")
                        usuario["endereco"] = novo_valor
                        print(usuario)
                        
                        with open(nome_arquivo, "w") as arquivo:
                            json.dump(usuarios, arquivo)
                    else: 
                        print("Valor inválido!")
                    
                else:
                    print("Usuário não cadastrado!")
                    
        #Apagar cliente            
        elif opcao == "4":
            cpf_consulta = input("Digite o CPF do usuário que deseja Apagar: ")
            usuario_encontrado = None

            for usuario in usuarios:
                if cpf_consulta == usuario["cpf"]:
                    usuario_encontrado = usuario
                    break  # Encerra o loop ao encontrar o usuário

            if usuario_encontrado:
                print(f"Cliente encontrado: {usuario_encontrado['nome']}")
                apagar = input("Deseja realmente apagar?\n1- Sim\n2- Não\n")

                if apagar == '1':
                    usuarios.remove(usuario_encontrado)
                    print("Usuário deletado com sucesso!")
                    
                    with open(nome_arquivo, "w") as arquivo:
                        json.dump(usuarios, arquivo)
                        
                elif apagar == '2':
                    print("Operação cancelada.")
            else:
                print("Usuário não encontrado.")
                
        elif opcao == "5":
            print(usuarios)
            
        elif opcao == "6":
            print("Saindo...")
            exit()
            
if __name__ == "__main__":
    edita()