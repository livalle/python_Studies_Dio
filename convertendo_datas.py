# Convertendo e formatando datas com strftime e strptime
from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-09-03 21:02"

# Máscaras corrigidas
mascara_ptbr = "%d/%m/%Y %a"  # Dia/Mês/Ano com o dia da semana abreviado
mascara_en = "%Y-%m-%d %H:%M"  # Ano-Mês-Dia Hora:Minuto

# Formatando a data e hora atual com a máscara em PT-BR
print(data_hora_atual.strftime(mascara_ptbr))

# Convertendo a string para um objeto datetime usando a máscara correta
data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(data_convertida)  # Exibindo o objeto datetime
print(type(data_convertida))  # Exibindo o tipo do objeto
