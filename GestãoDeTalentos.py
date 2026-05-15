import json
def salvar_dados(lista):
    try:
        with open("candidatos.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar {e}")
        
def carregar_dados():
    try:
        with open("candidatos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado. Carregando lista padrão...")
        return obter_lista_padrao()
    except json.JSONDecodeError:
        print("ERRO! O arquivo JSON está corrompido ou vazio. Carregando lista padrão...")
        return obter_lista_padrao()

def obter_lista_padrao():
    return [
        {"nome":"João Ricardo", "tecnologia":"Python","experiência":3},
        {"nome":"Alex Pereira","tecnologia":"Java","experiência":2},
        {"nome":"Lucas Alexandre","tecnologia":"Javascript","experiência":5},
        {"nome":"Rafael Gomes","tecnologia":"Assembly","experiência":1},
        {"nome":"Paulo Roger","tecnologia":"Python","experiência":6},
        {"nome":"Mercio Rodrigues","tecnologia":"C","experiência":6}     
    ]
def search_senioriti(senioridade):
    nivel = input("Qual nível de senioridade você quer buscar? ").title()
    for info in senioridade:
        if verify_candidats(info['experiência']) == nivel:
            print(f"nome: {info['nome']} | experiência: {info['experiência']}")

def add_new_cv(curriculo):
    print("Para adicionar um novo currículo ao sistema, preencha os dados abaixo: ")
    nome = input("Informe o nome do novo currículo: ")
    tec = input("informe a nova tecnologia(linguagem) do novo currículo: ")
    try:
        exp = int(input("Informe a experiência do novo currículo: "))

        new_cv = {
            "nome": nome,
            "tecnologia": tec,
            "experiência": exp
        }

        curriculo.append(new_cv)
        
        print(f"Um novo currículo com o nome de {nome}, foi adicionado com sucesso.")

        for item in curriculo:
            print(f"nome: {item['nome']} | tecnologia: {item['tecnologia']} | experiência: {item['experiência']}")
    except ValueError:
        print("ERRO! Informe apenas números nesse campo.")      

def search_candidats(tec):
    busca = input("por qual tecnologia você quer buscar? ").lower()
    for tecnologi in tec:
        if tecnologi['tecnologia'].lower() == busca:
            print(f"nome: {tecnologi['nome']} | tecnologia: {tecnologi['tecnologia']}")

def listing_all_candidats(candidats):
    for item in candidats:
        print(f"nome: {item['nome']} | tecnologia: {item['tecnologia']} | experiência: {item['experiência']}")

def verify_candidats(anos):
    if anos < 2:
        return "Júnior"
    elif 2 <= anos <= 5:
        return "Pleno"
    else:
        return "Sênior"

candidatos = [
    {"nome":"João Ricardo", "tecnologia":"Python","experiência":3},
    {"nome":"Alex Pereira","tecnologia":"Java","experiência":2},
    {"nome":"Lucas Alexandre","tecnologia":"Javascript","experiência":5},
    {"nome":"Rafael Gomes","tecnologia":"Assembly","experiência":1},
    {"nome":"Paulo Roger","tecnologia":"Python","experiência":6},
    {"nome":"Mercio Rodrigues","tecnologia":"C","experiência":6}
]

# Verificar a lista candidatos, exibindo o nível de senioridade de cada um.
# Criei um for para fazer uma varredura na lista candidatos e chamar a função para verificar o atributo experiência de cada candidato na lista.
candidatos = carregar_dados()
print("Relação de Senioridade dos candidatos: ")
for candidat in candidatos:
    result = verify_candidats(candidat['experiência'])
    print(f"nome: {candidat['nome']} | tecnologia: {candidat['tecnologia']} -> {result}")
while True:
    try:
        escolha = int(input("Escolha uma opção: (1. Listar todos os candidatos | 2. Buscar por candidatos pela tecnologia | 3. Adicionar um novo currículo ao sistema | 4. Buscar candidatos pela senioridade ou digite 0 para sair)"))

        match escolha:
            case 0:
                print("Terminando programa.")
                break
            case 1:
                print("Listando todos os candidatos: ")
                listing_all_candidats(candidatos)
            case 2:
                search_candidats(candidatos)
            case 3:
                add_new_cv(candidatos)
                salvar_dados(candidatos)
            case 4:
                search_senioriti(candidatos)
    except ValueError:
        print("\nERROR! Porfavor, digitar apenas números nas opções.\n")