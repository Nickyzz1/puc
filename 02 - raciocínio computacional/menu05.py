import json
import os

# Estruturas de dados globais
students, teachers, disciplines, classes, registrations = [], [], [], [], []

# JSON final
data = {
    'students': students,
    'teachers': teachers,
    'disciplines': disciplines,
    'classes': classes,
    'registrations': registrations
}

# Função para carregar dados do arquivo JSON
def loadJson():
    global students, teachers, disciplines, classes, registrations
    file_path = "data.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)
            students[:] = loaded_data.get('students', [])
            teachers[:] = loaded_data.get('teachers', [])
            disciplines[:] = loaded_data.get('disciplines', [])
            classes[:] = loaded_data.get('classes', [])
            registrations[:] = loaded_data.get('registrations', [])
            print("Dados carregados com sucesso!")
    else:
        print("Arquivo JSON não encontrado. Um novo será criado ao salvar dados.")

# Função para salvar os dados no arquivo JSON
def updateJson():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Dados salvos no arquivo JSON.")

# Função para verificar CPF duplicado
def isFoundCpf(cpf, dataset):
    for item in dataset:
        if item['cpf'] == cpf:
            print("CPF já cadastrado.")
            return True
    return False

# Função para verificar código duplicado
def isFoundCod(cod, dataset):
    for item in dataset:
        if item['codigo'] == cod:
            return True
    return False

# Validação de código
def validateCod(cod, dataset, operation):
    if not cod.isdigit():
        print("Código inválido! Deve ser numérico.")
        return False
    cod = int(cod)
    if operation == 'create' and isFoundCod(cod, dataset):
        print("Código já existente! Operação cancelada.")
        return False
    elif operation in ('edit', 'delete') and not isFoundCod(cod, dataset):
        print("Código não encontrado!")
        return False
    return True

# Função para criar um novo registro
def create(dataset, fields):
    cod = input("Digite o código:\n-- ")
    if validateCod(cod, dataset, 'create'):
        cod = int(cod)
        data_entry = {'codigo': cod}
        for field in fields:
            value = input(f"Digite o {field}:\n-- ")
            if field == 'cpf' and isFoundCpf(value, dataset):
                return
            data_entry[field] = value
        dataset.append(data_entry)
        updateJson()
        print(f"{fields[0].capitalize()} cadastrado(a) com sucesso!")

# Função para listar registros
def listing(dataset, fields):
    if not dataset:
        print("Nenhum registro encontrado.")
        return
    print("\n===== REGISTROS =====")
    for i, item in enumerate(dataset, start=1):
        print(f"{i}.", ", ".join(f"{field.capitalize()}: {item[field]}" for field in fields))

# Função para editar registros
def edit(dataset, fields):
    cod = input("Digite o código do registro a ser editado:\n-- ")
    if not validateCod(cod, dataset, 'edit'):
        return
    cod = int(cod)
    for item in dataset:
        if item['codigo'] == cod:
            for field in fields:
                if field == 'codigo':
                    continue
                value = input(f"Digite o novo {field} (deixe vazio para manter o atual):\n-- ")
                if value:
                    if field == 'cpf' and isFoundCpf(value, dataset):
                        return
                    item[field] = value
            updateJson()
            print("Registro atualizado com sucesso!")
            return
    print("Registro não encontrado!")

# Função para excluir registros
def delete(dataset):
    cod = input("Digite o código do registro a ser excluído:\n-- ")
    if not validateCod(cod, dataset, 'delete'):
        return
    cod = int(cod)
    for item in dataset:
        if item['codigo'] == cod:
            dataset.remove(item)
            updateJson()
            print("Registro excluído com sucesso!")
            return
    print("Registro não encontrado!")

# Menu principal
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
            elif option in range(1, 6):
                subMenu(option)
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# Submenu para cada categoria
def subMenu(option):
    categories = {
        1: ('students', students, ['nome', 'cpf']),
        2: ('teachers', teachers, ['nome', 'cpf']),
        3: ('disciplines', disciplines, ['nome']),
        4: ('classes', classes, ['codigoProfessor', 'codigoMateria']),
        5: ('registrations', registrations, ['codigoEstudante', 'codigoTurma'])
    }
    category, dataset, fields = categories[option]
    while True:
        try:
            print(f"\n===== GERENCIAR {category.upper()} =====")
            print("(1) Incluir")
            print("(2) Listar")
            print("(3) Editar")
            print("(4) Excluir")
            print("(9) Voltar ao menu principal")
            action = int(input("Escolha uma opção:\n-- "))
            if action == 9:
                break
            elif action == 1:
                create(dataset, fields)
            elif action == 2:
                listing(dataset, fields)
            elif action == 3:
                edit(dataset, fields)
            elif action == 4:
                delete(dataset)
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# Execução do programa
if __name__ == "__main__":
    loadJson()
    mainMenu()
