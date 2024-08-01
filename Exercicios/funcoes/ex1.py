# Madrugada - 0h às 5h - Boa madruga
# Manhã - 5h às 12h - Bom dia
# Tarde - 12h às 19h - Boa tarde
# Noite - 19h às 24h - Boa noite
# Mensagem automática: Crie uma função que receba um nome como parâmetro
# escreva uma saudação baseada na hora atual.

from datetime import datetime

hora_atual = datetime.now().hour


def solicite_nome():
    nome = input('Qual o seu nome?')
    return nome


def define_saudacao(hora_atual):
    if hora_atual >= 0 and hora_atual <= 5:
        saudacao = "Boa madrugada:"
    elif hora_atual <= 12:
        saudacao = "Bom Dia:"
    elif hora_atual <= 19:
        saudacao = "Boa tarde:"
    else:
        saudacao = "Boa noite:"

    return saudacao


def exibir_mensagem(nome, saudacao):
    print(saudacao + nome)


exibir_mensagem(solicite_nome(), define_saudacao(hora_atual))
