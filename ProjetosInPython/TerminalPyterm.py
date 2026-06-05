import os
from datetime import datetime

def init_sistem():
    print("-"*10, "Seja bem-vindo ao Pyterm", "-"*10)
    print("-"*10, "Pyterm é um terminal de comandos feito totalmente em Python", "-"*10)
    print("-"*10, "Digite 'py -help' para ver os comandos disponíveis", "-"*10)

def version_term():
    print("-"*10, "Pyterm version", "-"*10)
    print("Version: 1.0.0")
    print("@uthor: Jhonata carvalho")
    print("All rights reserved@2026")

def listing_commands():
    print("Comandos disponíveis: ")
    print("  py -help: Exibe esta mensagem")
    print("  exit: Fecha o terminal")
    print("  py -clear: Limpa a tela")
    print("  py -date: Exibe a data e hora atual")
    print("  py -echo: Exibe uma mensagem personalizada")
    print("  py -calc: Realiza operações matemáticas básicas")
    print("  py -version: Exibe a versão do Pyterm")
    print("  py -makedir: Cria um diretório")
    print("  py -list: Lista os arquivos e diretórios do diretório atual")
    print("  py -delete: Exclui um arquivo ou diretório")
    print("  py -open: Abre um diretório ou arquivo")

def execute_term():
    while True:
        entrada = input("user@pyterm $> ").strip()

        if entrada == "exit":
            print("Encerrando o pyterm, obrigado por usar o nosso terminal!")
            break

        partes = entrada.split()

        if not partes:
            continue

        if len(partes) < 2:
            entrada = partes[0]
        else:
            entrada = partes[0] + " " + partes[1]

        match entrada:
            case "py -help":
                listing_commands()
            case "py -clear":
                os.system("cls" if os.name == "nt" else "clear")
            case "py -date":
                agora = datetime.now()
                data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
                print(f"Data e Hora atual: {data_formatada}")
            case "py -echo":
                mensagem = " ".join(partes[2:])
                if mensagem:
                    print(mensagem)
                else:
                    print("Uso: py -echo <sua mensagem aqui>")
            case "py -calc":
                if len(partes) < 4:
                    print("Uso: py -calc <número1> <operador> <número2>")
                    print("Operadores suportados: +, -, *, /")
                    continue
                try:
                    numero1 = float(partes[2])
                    operador = partes[3]
                    numero2 = float(partes[4])

                    match operador:
                        case "+":
                            resultado = numero1 + numero2
                        case "-":
                            resultado = numero1 - numero2
                        case "*":
                            resultado = numero1 * numero2
                        case "/":
                            if numero2 == 0:
                                print("Erro: Divisão por zero não é permitida.")
                                continue
                            resultado = numero1 / numero2
                        case _:
                            print("Operador inválido. Use +, -, *, ou /.")
                            continue
                    print(f"Resultado: {resultado:.1f}")

                except ValueError:
                    print("Erro: Certifique-se de que os números são válidos.") 
            case "py -version":
                version_term()
            case "py -makedir":
                if len(partes) < 3:
                    print("Uso: py -makedir <nome_do_diretório>")
                    continue
                nome_diretorio = " ".join(partes[2:])
                try:
                    os.makedirs(nome_diretorio) # Cria um diretório direto na pasta do computador.
                    print(f"Diretório '{nome_diretorio}' criado com sucesso.")
                except OSError as e:
                    print(f"Erro ao criar diretório: {e}")
            case "py -list":
                arquivos = os.listdir(".")
                print("Arquivos e diretórios no diretório atual:")
                for arquivo in arquivos:
                    print(f"  {arquivo}")
            case "py -delete":
                if len(partes) < 3:
                    print("Uso: py -delete <nome_do_arquivo_ou_diretório>")
                    continue
                nome_arquivo = " ".join(partes[2:])
                try:
                    if os.path.isfile(nome_arquivo):
                        os.remove(nome_arquivo)
                        print(f"Arquivo '{nome_arquivo}' excluído com sucesso.")
                    elif os.path.isdir(nome_arquivo):
                        os.rmdir(nome_arquivo)
                        print(f"Diretório '{nome_arquivo}' excluído com sucesso.")
                    else:
                        print(f"O arquivo ou diretório '{nome_arquivo}' não existe.")
                except OSError as e:
                    print(f"Erro ao excluir arquivo ou diretório: {e}")
            case "py -open":
                if len(partes) < 3:
                    print("Uso: py -open <nome_do_arquivo_ou_diretório>")
                    continue
                nome_arquivo = " ".join(partes[2:])
                try:
                    if os.path.isfile(nome_arquivo):
                        os.startfile(nome_arquivo)
                    elif os.path.isdir(nome_arquivo):
                        os.startfile(nome_arquivo)
                    else:
                        print(f"O arquivo ou diretório '{nome_arquivo}' não existe.")
                except OSError as e:
                    print(f"Erro ao abrir arquivo ou diretório: {e}")
            case _:
                print(f"Comando '{entrada}' não reconhecido. Digite 'py -help' para ver os comandos disponíveis.")

if __name__ == "__main__":
    init_sistem()
    execute_term()
