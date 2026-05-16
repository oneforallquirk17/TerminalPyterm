import json

def save_product(saving):
    try:
        with open("my_list.json", "w", encoding="utf-8") as save:
            json.dump(saving, save, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f"Erro ao salvar {error}")
def carregar_dados():
    try:
        with open("my_list.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("ERRO! Arquivo não encontrado. Carregando a lista padrão.")
        return list_defult()
    except json.JSONDecodeError:
        print("ERRO! O arquivo json está corrompido ou vazo. Carregando a lista padrão...")
        return list_defult()

def list_defult():
    return [
        {"nome":"feijão","quantidade":120,"preço":8.50},
        {"nome":"arroz","quantidade":200,"preço":4.00},
        {"nome":"macarrão","quantidade":150,"preço":2.50},
        {"nome":"carne","quantidade":240,"preço":50.00},
        {"nome":"sucos","quantidade":780,"preço":5.00},
        {"nome":"guloseimas","quantidade":900,"preço":1.00},
        {"nome":"pão","quantidade":1500,"preço":1.50}
        ]

def register_sale(vendas):
    print("Sistema de vendas, porfavor informe os dados do produto que deseja comprar abaixo.")
    nome = input("Insira o nome do item: ").lower()
    localizado = False
    print("Localizando produto...")
    for item in vendas:
        if item['nome'].lower() == nome:
            print("Produto localizado!")
            localizado = True
            print(f"nome: {item['nome']} | quantidade: {item['quantidade']} | preço: {item['preço']}")

            try:
                qtd = int(input("Informe a quantidade desejada: "))

                if qtd <= item['quantidade']:
                    item['quantidade'] -= qtd
                    total_venda = qtd * item['preço']
                    print(f"Venda localizada com sucesso! Total a pagar: R$ {total_venda:.2f}")

                    save_product(vendas)
                else:
                    print(f"ERRO! Estoque insificiente. Temos apenas {item['quantidade']} unidades.")
            except ValueError:
                print("ERRO! Porfavor, deigitar apenas números inteiros para a quantidade.")
            break

    if not localizado:
        print(f"Produto '{nome}' não localizado no estoque.")
    
def display_products(mercadorias):
    print("-"*10, " Exbindo todo o estoque de produtos ", "-"*10)
    for item in mercadorias:
        print(f"nome: {item['nome']} | quantidade: {item['quantidade']} | preço: {item['preço']}")

def cad_new_product(add):
    print("Para adicionar um novo produto ao sistema de estoque, preencha os dados abaixo: ")
    nome = input("Informe o nome do novo produto: ")
    try:
        qtd = int(input("Informa a quantidade do novo produto: "))
        preco = float(input("Informe o preço do novo produto: "))

        new_product = {
            "nome": nome,
            "quantidade": qtd,
            "preço": preco
        }

        add.append(new_product)

        print(f"Um novo produto {nome} foi adicionado com sucesso ao sistema de estoque.")
        for item in add:
            print(f"nome: {item['nome']} | quantidade: {item['quantidade']} | preço: {item['preço']}")
    except ValueError:
        print("ERRO! identificamos uma informação inválida em um dos campos. Porfavor, digitar apenas números.")

produtos = [
    {"nome":"feijão","quantidade":120,"preço":8.50},
    {"nome":"arroz","quantidade":200,"preço":4.00},
    {"nome":"macarrão","quantidade":150,"preço":2.50},
    {"nome":"carne","quantidade":240,"preço":50.00},
    {"nome":"sucos","quantidade":780,"preço":5.00},
    {"nome":"guloseimas","quantidade":900,"preço":1.00},
    {"nome":"pão","quantidade":1500,"preço":1.50}
]

produtos = carregar_dados()

print("-"*10, " Gestão de Controle de Estoque e Vendas ", "-"*10)
while True:
    try:
        escolha = int(input("Escolha a sua opção: (1.Cadastrar novo produto | 2.Visualizar estoque | 3.Registrar uma venda ou digite 0 para sair)."))
        match escolha:
            case 0:
                print("Encerrando programa...")
                break
            case 1:
                cad_new_product(produtos)
                save_product(produtos)
            case 2:
                display_products(produtos)
            case 3:
                register_sale(produtos)
    except ValueError:
        print("ERRO! Digite apenas números para as opções.")