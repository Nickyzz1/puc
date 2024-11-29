import json
import os

students = []

def updateJson():

    f_path = "students.json"

    if os.path.exists(f_path):
        print("O arquivo já existe. Atualizando os dados...")

        # Carrega os dados existentes e adiciona novos dados
        with open(f_path, "r") as f:
            existing_data = json.load(f)
        
        # Adiciona os dados de 'students' aos dados existentes
        existing_data.extend(students)
        
        # Salva todos os dados de volta no arquivo
        with open(f_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)
    else:
        print("O arquivo não existe. Criando um novo arquivo...")

        # Cria um novo arquivo e salva os dados de 'students'
        with open(f_path, "w") as f:
            json.dump(students, f, indent=4, ensure_ascii=False)

    print("Arquivo JSON atualizado ou criado com sucesso!")

    # criar um novo arquivo
    with open(f_path, "w") as f:
        json.dump(students, f)

    print("Arquivo JSON atualizado ou criado com sucesso!")

def validateCod(cod):
    if cod.isdigit():
        return True
   
    print("Erro ao validar código! Digite um código válido")
    return False

# função para conferir se o CPF já está cadastrado, assim o mesmo CPF não pode ser cadastrado duas vezes
def foundCpf(cpf):
    for i in students:
        if i['cpf'] == cpf:
            print("Não é possível cadastrar o mesmo CPF duas vezes")
            return True
    return False
    
# função para procurar se o código já está cadastrado, não deixando cadastrar o mesmo código duas vezes
def foundCod(cod):
    for i in students:
        if i['codigo'] == cod:
            print("Não é possível cadastrar o mesmo código duas vezes")
            return True
    return False 
     

# função para criar um estudante
def createStudent(cod, name, cpf):
   
    if foundCpf(cpf):
        return 

    currStudent = {
        'codigo': cod,
        'nome': name,
        'cpf': cpf
    }
    students.append(currStudent)


# função para listar todos os estudantes
def listingStudents():
    
    print("\n\n===== LISTAGEM =====\n\n")
    if(len(students) == 0):
        print("Não há estudantes cadastrados\n")
    else:
        for i in range(len(students)):
            print(" - ", students[i])
   
def editStudent(codStudentToEdit, newCod, newName, newCpf):
    
    # encontrando e atualizando o estudante
    studentFound = False
    for i in students:
        if i['codigo'] == codStudentToEdit:
            i['codigo'] = newCod
            i['nome'] = newName
            i['cpf'] = newCpf
            studentFound = True
            print('Atualização realizada com sucesso!')
            break
    
    if not studentFound:
        print("Estudante com o código informado não encontrado.")            
            
def deleteStudent():
    
    print("\n\n===== EXCLUSÃO =====\n")
    
    codStudentToRemove = input("Digite o código do estudante que deseja excluir\n--")
    if validateCod(codStudentToRemove):
        codStudentToRemove = int(codStudentToRemove)
    
        studentFound = False
        for i in students:
            if i['codigo'] == codStudentToRemove:
                students.remove(i)
                studentFound = True
                print("\nEstudante excluído com sucesso")
                break
        # vebdo se o estudante não foi encontrado
        if not studentFound:
            print("Estudante com o código informado não encontrado.")

# essa função mostra o menu principal
def mainMenu():
    try:
        response = int(input("\n----- MENU PRINCIPAL -----\n\n(1) GERENCIAR ESTUDANTES\n(2) GERENCIAR PROFESSORES\n(3) GERENCIAR DISCIPLINAS\n(4) GERENCIAR TURMAS\n(5) GERENCIAR MATRICULAS\n(9) SAIR\n\nINFORME A OPÇÃO DESEJADA: "))
        return response
    except ValueError:
        print("\n===========================")
        print("Digite um número válido")
        print("===========================\n")
        return None

# esta função mostra o menu de operações
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

# essa função mostra o menu detalhado das opções
def moreOptions(type):
    while True:
        try:
            if(type == "PROFESSORES" or type == "DISCIPLINAS" or type == "TURMAS" or type == "MATRÍCULAS"):
                print("\nEM DESENVOLVIMENTO...")
                operMenu()
            else:
                print(f"\n----- [{type}] MENU DE OPERAÇÕES -----")
                response = int(input("(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                
                match response:
                    
                    # Cadastrar estudante
                    case 1:
                        
                        cod = input("\n\n===== INCLUSÃO =====\n\nInforme o código do estudante:\n-- ")
                        
                        # valido se o código é um número
                        if validateCod(cod):
                            cod = int(cod)
                            
                            if not foundCod(cod):
                                name = input("\nInforme o nome do estudante:\n-- ")
                                cpf = input("\nInforme o CPF do estudante:\n--")
                                
                                # valido se o cpf já está em uso
                                if not foundCpf(cpf):
                                    createStudent(cod, name, cpf)
                                    input("Estudante incluído com sucesso! Pressione ENTER para continuar")
                                
                    # listando todos os estudantes existentes 
                    case 2:
                        
                        listingStudents()
                            
                        input("Pressione ENTER para continuar")
                    
                    # atualizar dados do estudante selecionado
                    case 3:
                        print("\n\n===== ATUALIZAÇÃO =====\n")
                        codStudentToEdit = input("Digite o código do estudante que deseja atualizar\n--")
                        
                        if validateCod(codStudentToEdit):
                            codStudentToEdit = int(codStudentToEdit)
                        
                            newCod = input("Digite o novo código:\n--")
                            newName = input("Digite o novo nome:\n--")
                            newCpf = input("Digite o novo CPF para o estudante:\n--")
                            
                            if validateCod(newCod):
                                newCod = int(newCod)
                                
                            if not foundCpf(newCpf):
                                editStudent(codStudentToEdit, newCod, newName, newCpf)
                        
                        input("Pressione ENTER para continuar")
                        
                    # Excluir estudante
                    case 4:
                       
                        deleteStudent()
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
