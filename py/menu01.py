def mainMenu():
    response = int(input("\n\n----- MENU PRINCIPAL -----\n\n(1) GERENCIAR ESTUDANTES\n(2) GERENCIAR PROFESSORES\n(3) GERENCIAR DISCIPLINAS\n(4) GERENCIAR TURMAS\n(5) GERENCIAR MATRICULAS\n(9)SAIR\n\nINFORME A OPÇÃO DESEJADA:"))
    return response

def operMenu():

    match mainMenu():
        case 1:
            response = int(input("\n\n----- [ESTUDANTES] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIAPL\n\nINFORME A OPÇÃO DESEJADA:"))
        case 2: 
            response = int(input("\n\n----- [PROFESSORES] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIAPL\n\nINFORME A OPÇÃO DESEJADA:"))
        case 3: 
            response = int(input("\n\n----- [DISCIPLINAS] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIAPL\n\nINFORME A OPÇÃO DESEJADA:"))
        case 4: 
            response = int(input("\n\n----- [TURMAS] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIAPL\n\nINFORME A OPÇÃO DESEJADA:"))
        case 5: 
            response = int(input("\n\n----- [MATRÍCULAS] MENU DE OPERAÇÕES -----\n\n(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIAPL\n\nINFORME A OPÇÃO DESEJADA:"))
        case 9: 
            mainMenu()
            
    return response

while True:
    operMenu()


