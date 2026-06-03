import os
from datetime import datetime

def init_sistem():
    print("-"*10, "Seja bem-vindo ao Pyterm", "-"*10)
    print("-"*10, "Pyterm é um terminal de comandos feito totalmente em Python", "-"*10)
    print("-"*10, "Digite 'help' para ver os comandos disponíveis", "-"*10)

def listing_commands():
    print("Comandos disponíveis: ")
    print("  py -help: Exibe esta mensagem")
    print("  exit: Fecha o terminal")
    print("  py -clear: Limpa a tela")
    print("  py -date: Exibe a data e hora atual")
    print("  py -echo: Exibe uma mensagem personalizada")
    print("  py -calc: Realiza operações matemáticas básicas")

def execute_term():
    while True:
        entrada = input("user@pyterm $ ").strip()

        if entrada == "exit":
            print("Encerrando o pyterm, obrigado por usar o nosso terminal!")
            break

        partes = entrada.split()
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
            case _:
                print(f"Comando '{entrada}' não reconhecido. Digite 'py -help' para ver os comandos disponíveis.")

if __name__ == "__main__":
    init_sistem()
    execute_term()
