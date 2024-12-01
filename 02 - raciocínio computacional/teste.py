import json
import os

# json de estudantes
students = []

# função para pegra os dados existentes do json
def loadJson():
    global students
    f_path = "students.json"
    if os.path.exists(f_path):
        with open(f_path, "r", encoding="utf-8") as f:
            students = json.load(f)
            print("Dados carregados do arquivo JSON com sucesso!")
    else:
        print("Arquivo JSON não encontrado.")

# gunção para salvar os dados no JSON
def updateJson():
    f_path = "students.json"
    with open(f_path, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)
    print("Arquivo JSON atualizado com sucesso!")

# função para validar códigos numéricos
def validateCod(cod):
    if cod.isdigit():
        return True
    print("Erro ao validar código! Digite um código válido")
    return False

# verifica se o CPF já está cadastrado
def foundCpf(cpf):
    for i in students:
        if i['cpf'] == cpf:
            print("Não é possível cadastrar o mesmo CPF duas vezes")
            return True
    return False

# Verifica se o código já está cadastrado
def foundCod(cod):
    for i in students:
        if i['codigo'] == cod:
            print("Não é possível cadastrar o mesmo código duas vezes")
            return True
    return False

# Função para criar um estudante
def createStudent(cod, name, cpf):
    if foundCpf(cpf):
        return

    currStudent = {
        'codigo': cod,
        'nome': name,
        'cpf': cpf
    }
    students.append(currStudent)
    updateJson()  # Atualiza o arquivo JSON após adicionar um estudante

# função para listar todos os estudantes
def listingStudents():
    print("\n\n===== LISTAGEM =====\n\n")
    if len(students) == 0:
        print("Não há estudantes cadastrados\n")
    else:
        for i in students:
            print(" - ", i)

# função para editar um estudante
def editStudent(codStudentToEdit, newCod, newName, newCpf):
    studentFound = False
    for i in students:
        if i['codigo'] == codStudentToEdit:
            i['codigo'] = newCod
            i['nome'] = newName
            i['cpf'] = newCpf
            studentFound = True
            updateJson()  # Atualiza o arquivo JSON após a edição
            print('Atualização realizada com sucesso!')
            break
    if not studentFound:
        print("Estudante com o código informado não encontrado.")

# função para excluir um estudante
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
                updateJson()  # Atualiza o arquivo JSON após a exclusão
                print("\nEstudante excluído com sucesso")
                break
        if not studentFound:
            print("Estudante com o código informado não encontrado.")

# função principal para o menu
def mainMenu():
    try:
        response = int(input("\n----- MENU PRINCIPAL -----\n\n(1) GERENCIAR ESTUDANTES\n(9) SAIR\n\nINFORME A OPÇÃO DESEJADA: "))
        return response
    except ValueError:
        print("\n===========================")
        print("Digite um número válido")
        print("===========================\n")
        return None

# menu de operações
def operMenu():
    while True:
        try:
            option = mainMenu()
            if option is None:
                continue

            match option:
                case 1:
                    moreOptions("ESTUDANTES")
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

# menu detalhado para estudantes
def moreOptions(type):
    while True:
        try:
            if type == "ESTUDANTES":
                print(f"\n----- [{type}] MENU DE OPERAÇÕES -----")
                response = int(input("(1) INCLUIR\n(2) LISTAR\n(3) ATUALIZAR\n(4) EXCLUIR\n(9) VOLTAR AO MENU PRINCIPAL\n\nINFORME A OPÇÃO DESEJADA: "))
                match response:
                    case 1:
                        cod = input("\nInforme o código do estudante:\n-- ")
                        if validateCod(cod):
                            cod = int(cod)
                            if not foundCod(cod):
                                name = input("Informe o nome do estudante:\n-- ")
                                cpf = input("Informe o CPF do estudante:\n--")
                                if not foundCpf(cpf):
                                    createStudent(cod, name, cpf)
                                    print("Estudante incluído com sucesso!")
                    case 2:
                        listingStudents()
                    case 3:
                        codStudentToEdit = input("\nDigite o código do estudante que deseja atualizar\n--")
                        if validateCod(codStudentToEdit):
                            codStudentToEdit = int(codStudentToEdit)
                            newCod = input("Digite o novo código:\n--")
                            newName = input("Digite o novo nome:\n--")
                            newCpf = input("Digite o novo CPF para o estudante:\n--")
                            if validateCod(newCod):
                                newCod = int(newCod)
                            if not foundCpf(newCpf):
                                editStudent(codStudentToEdit, newCod, newName, newCpf)
                    case 4:
                        deleteStudent()
                    case 9:
                        return
                    case _:
                        print("\nDigite uma opção válida!")
        except ValueError:
            print("Erro: Digite um número válido.")

loadJson()

operMenu()
