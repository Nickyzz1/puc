def mainMenu():
    try:
        response = int(input("\n\n----- MENU PRINCIPAL -----\n\n(1) GERENCIAR ESTUDANTES\n(2) GERENCIAR PROFESSORES\n(3) GERENCIAR DISCIPLINAS\n(4) GERENCIAR TURMAS\n(5) GERENCIAR MATRICULAS\n(9) SAIR\n\nINFORME A OPÇÃO DESEJADA: "))
        return response
    except ValueError:
        print("\nDigite um número válido\n")
        return None

def operMenu():
    while True:
        try:
            option = mainMenu()
            if option is None:
                continue  
            
            match option:
                case 1:
                    response = int(input("\n\n----- [ESTUDANTES] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                case 2: 
                    response = int(input("\n\n----- [PROFESSORES] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                case 3: 
                    response = int(input("\n\n----- [DISCIPLINAS] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                case 4: 
                    response = int(input("\n\n----- [TURMAS] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                case 5: 
                    response = int(input("\n\n----- [MATRÍCULAS] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                case 9:
                    print("Até logo")
                    break
                case _:
                    print("Digite um número válido")
                    continue

            moreOptions(response)
        except ValueError:
            print("\nDigite um número válido\n")

def moreOptions(response):
    match response:
        case 1:
            print("\n\n===== INCLUIR =====\n\nFinalizando a aplicação...\n")
        case 2:
            print("\n\n===== LISTAR =====\n\nFinalizando a aplicação...\n")
        case 3:
            print("\n\n===== ATUALIZAÇÃO =====\n\nFinalizando a aplicação...\n")
        case 4:
            print("\n\n===== EXCLUIR =====\n\nFinalizando a aplicação...\n")
        case 9:
            operMenu()
        case _:
            print("\nDigite um número válido\n")

operMenu()
