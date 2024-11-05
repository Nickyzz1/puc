students = []

def mainMenu():
    try:
        response = int(input("\n----- MENU PRINCIPAL -----\n\n(1) GERENCIAR ESTUDANTES\n(2) GERENCIAR PROFESSORES\n(3) GERENCIAR DISCIPLINAS\n(4) GERENCIAR TURMAS\n(5) GERENCIAR MATRICULAS\n(9) SAIR\n\nINFORME A OPÇÃO DESEJADA: "))
        return response
    except ValueError:
        
        print("\n===========================")
        print("Digite um número válido")
        print("===========================\n")
        
        return None

def operMenu():
    while True:
        try:
            option = mainMenu()
            if option is None:
                continue  
            
            match option:
                case 1:
                    moreOptions("ESTUDANTES")
                case 2: 
                    moreOptions("PROFESSORES")
                case 3: 
                    moreOptions("DISCIPLINAS")
                case 4: 
                    moreOptions("TURMAS")
                case 5: 
                    moreOptions("MATRÍCULAS")
                case 9:
                    print("Até logo")
                    break
                case _:
                    print("\n===========================")
                    print("Digite um número válido")
                    print("===========================\n")
                    continue
        except ValueError:
            print("\n===========================")
            print("Digite um número válido")
            print("===========================\n")

def moreOptions(type):
    while True:
        try:
            
            if(type == "PROFESSORES" or type == "DISCIPLINAS" or type== "TURMAS" or type == "MATRÍCULAS"):
                print("\nEM DESENVOLVIMENTO...")
                operMenu()
            else:
            
                print(f"\n----- [{type}] MENU DE OPERAÇÕES -----")
                response = int(input("(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                
                
                match response:
                    case 1:
                        name = input("\n\n===== INCLUSÃO =====\n\nInforme o nome do estudante:\n-- ")
                        students.append(name)
                        input("Estudante incluído com sucesso! Pressione ENTER para continuar")
                    
                        
                    case 2:
                        print("\n\n===== LISTAGEM =====\n\n")
                        
                        if(len(students) == 0):
                            print("Não há estudantes cadastrados\n")
                        else:
                            for i in range(len(students)):
                                print(" - ", students[i])
                            
                        input("Pressione ENTER para continuar")
                        
                    case 3:
                        print("\n\n===== ATUALIZAÇÃO =====\n")
                        
                        print("\nEM DESENVOLVIMENTO...")
                    
                        input("Pressione ENTER para continuar")
                        
                    case 4:
                        print("\n\n===== EXCLUSÃO =====\n")
                        
                        print("\nEM DESENVOLVIMENTO...")
                
                        input("Pressione ENTER para continuar")
                        
                    case 9:
                        return 
                    case _:
                        print("\n===========================")
                        print("Digite um número válido")
                        print("===========================\n")
                        
        except ValueError:
            print("\n===========================")
            print("Digite um número válido")
            print("===========================\n")

operMenu()
