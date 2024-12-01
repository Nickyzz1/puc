import json
import os

# listas que serão manipuladas no código
students = [] 
teachers = []
disciplines = []
classes = []
registrations = []

# model JSON final
data = {
    'students': students,
    'teachers': teachers,
    'disciplines': disciplines,
    'classes': classes,
    'registrations': registrations
}

# função para pegar dados do arquivo JSON
def loadJson():
    
    # para que as modificações atinjam as listas globalmente
    global students, teachers, disciplines, classes, registrations
    
    file_path = "data.json"
    if os.path.exists(file_path):
        
        with open(file_path, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)
            students[:] = loaded_data.get('students', []) # pega os dasdos da chave que eu quero(ex: students) e coloca na lista
            teachers[:] = loaded_data.get('teachers', [])
            disciplines[:] = loaded_data.get('disciplines', [])
            classes[:] = loaded_data.get('classes', [])
            registrations[:] = loaded_data.get('registrations', [])
            print("Dados carregados com sucesso!")
    else:
        print("Arquivo JSON não encontrado. Um novo será criado para salvar dados...")

# salva os dados no JSON
def updateJson():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False) # escreve no formato de json
    print("Dados salvos no arquivo JSON.")

# gunção para conferir se o CPF já está cadastrado, assim o mesmo CPF não pode ser cadastrado duas vezes
def isFoundCpf(cpf, dataset):
    for item in dataset:
        if item['cpf'] == cpf:
            print("CPF já cadastrado.")
            return True
    return False

# função para procurar se o código já está cadastrado, não deixando cadastrar o mesmo código duas vezes
def isFoundCod(cod, dataset):
    for item in dataset:
        if item['codigo'] == cod:
            return True
    return False

# funfão para validar o código
def validateCod(cod, dataset, operation):
    
    # aqui o meu raciocício foi que se for uma criação o código não pode ser pre-existente, mas se for uma edição ele precisa necessa´riamente ser
    
    # verificando se o código é um número
    if not cod.isdigit():
        print("Código inválido! Deve ser numérico.")
        return False
    
    cod = int(cod)
    
    if operation == 'create' and isFoundCod(cod, dataset):
        print("Não é possível cadastrar o mesmo código duas vezes!")
        return False
    
    elif operation in ('edit', 'delete') and not isFoundCod(cod, dataset):
        print("Código não encontrado!")
        return False
    
    return True

# função para criar dados
def create(dataset, fields):
    
    cod = input("Digite o código:\n-- ")
    
    if validateCod(cod, dataset, 'create'):
        cod = int(cod)
        dataEntry = {'codigo': cod}
        
        for field in fields:
            value = input(f"Digite o {field}:\n-- ")
            if field == 'cpf' and isFoundCpf(value, dataset):
                return
            dataEntry[field] = value # cria um novo campo para os valores inputados pelo user
        dataset.append(dataEntry) # adiciona a lista, por sua vez, a lista adicona ao "data" que atualiza o json
        updateJson()
        print(f"{fields[0].capitalize()} cadastrado(a) com sucesso!")

# função para listar registros do dataset
def listing(dataset, fields):
    
    if len(dataset) == 0:
        print("Nenhum registro encontrado.")
        return
    
    print("\n===== REGISTROS =====")
    for i, item in enumerate(dataset, start=1):
        print(f"Item {i} : ", ", ".join(f"{field.capitalize()}: {item[field]}" for field in fields))

# função para editar os registros
def edit(dataset, fields):
    
    cod = input("Digite o código do registro a ser editado:\n-- ")
    
    if not validateCod(cod, dataset, 'edit'):
        return
    
    cod = int(cod)
    
    for item in dataset:
        if item['codigo'] == cod: # acha o item pelo código
            for field in fields: # itera sobre todos os campos
                if field == 'codigo': # não permite alterar o id 
                    continue
                value = input(f"Digite o novo {field} (deixe vazio para manter o atual):\n-- ") # no for faz um input para cada item de fieds, EX: nome, cpf
                if value:
                    if field == 'cpf' and isFoundCpf(value, dataset):
                        return
                    item[field] = value #  atualiza o item no campo atual
            updateJson() # atualizo o JSON aqui
            print("Registro atualizado com sucesso!")
            return
    print("Registro não encontrado!")

# função para excluir registros
def delete(dataset):
    cod = input("Digite o código do registro a ser excluído:\n-- ")
    
    if not validateCod(cod, dataset, 'delete'):
        return
    
    cod = int(cod)
    # procura em todos os items o código inputado pelo user e remove quando acha
    for item in dataset:
        if item['codigo'] == cod:
            dataset.remove(item)
            updateJson()
            print("Registro excluído com sucesso!")
            return
    print("Registro não encontrado!")

# menu principal
def mainMenu():
    while True:
        try:
            print("\n===== MENU PRINCIPAL =====")
            print("(1) Gerenciar Estudantes")
            print("(2) Gerenciar Professores")
            print("(3) Gerenciar Disciplinas")
            print("(4) Gerenciar Turmas")
            print("(5) Gerenciar Matrículas")
            print("(9) Sair")
            option = int(input("Escolha uma opção:\n-- "))
            if option == 9:
                print("Saindo...")
                break
            elif option in range(1, 6): # verific mais rapidamente o parametro
                operMenu(option)
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# menu de operacoes para cada categoria
def operMenu(option):
    
    # aqui eu decici montar uma categoria, então esse dicionário tem uma chave e a tupla dentro dela significa respectivamente: o nome de cada categoria, a lista de cada categoria e o conjunto de perguntas de cada categoria
    categories = {
        1: ('students', students, ['nome', 'cpf']),
        2: ('teachers', teachers, ['nome', 'cpf']),
        3: ('disciplines', disciplines, ['nome']),
        4: ('classes', classes, ['codigoProfessor', 'codigoMateria']),
        5: ('registrations', registrations, ['codigoEstudante', 'codigoTurma'])
    }
    
    # pego cada item pela opção inputada pelo usário, Ex: se o user mandar 1 como option, então no dicionário ele vai pegar os dados dentro da chave 1, nesse caso ('students', students...etc)
    
    category = categories[option].__getitem__(0)
    dataset = categories[option].__getitem__(1)
    fields = categories[option].__getitem__(2)
    
    while True:
        try:
            print(f"\n===== GERENCIAR {category.upper()} =====")
            print("(1) Incluir")
            print("(2) Listar")
            print("(3) Editar")
            print("(4) Excluir")
            print("(9) Voltar ao menu principal")
            action = int(input("Escolha uma opção:\n-- "))
            
            match action:
            
                case 9:
                    break
                case 1:
                    create(dataset, fields)
                case 2:
                    listing(dataset, fields)
                case 3:
                    edit(dataset, fields)
                case 4:
                    delete(dataset)
                case _:
                    print("Opção inválida! Tente novamente.")
                    
        except ValueError:
            print("Entrada inválida! Insira um número válido.")

loadJson()

mainMenu()
