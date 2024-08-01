import datetime
#alimentar a variavel com o tempo "agora"
tempo = datetime.datetime.now()
semana = datetime.datetime.now().isoweekday()

mes = tempo.month
ano = tempo.year
dia = tempo.day
hora = tempo.hour
minuto = tempo.minute
segundo = tempo.second
resposta = ''
ms = ""

if hora < 12:
    complemento = "bom dia"
elif hora < 12 and hora < 18:
    complemento = "boa tarde"
else:
    complemento = "boa noite"

    if semana == 1:
        resposta = "domingo"
    elif semana == 2:
        resposta = "Segunda_feira"
    elif semana == 3:
        resposta = "terca_feira"
    elif semana == 4:
        resposta = "quarta_feira"
    elif semana == 5:
        resposta = "quinta_feira"
    elif semana == 6:
        resposta = "sexta_feira"
    elif semana == 7:
        resposta = "sabado"

    if mes == 1:
        ms = "janeiro"
    elif mes == 2:
        ms = "fevereiro"
    elif mes == 3:
        ms = "março"
    elif mes == 4:
        ms = "abril"
    elif mes == 5:
        ms = "maio"
    elif mes == 6:
        ms = "junho"
    elif mes == 7:
        ms = "julho"
    elif mes == 8:
        ms = "agosto"
    elif mes == 9:
        ms = "setembro"
    elif mes == 10:
        ms = "outubro"
    elif mes == 11:
        ms = "novembro"
    elif mes == 12:
        ms = "dezembro"

    print(f"{complemento}\nhoje é  {dia} do mes {mes} de {ms}, do ano {ano}, agora sao  {hora}:{minuto}:{segundo}")
