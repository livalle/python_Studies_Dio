  #Outro exemplo de cód. (mais especificamente o uso de timedelta)
      from datetime import datetime, timedelta

# Data e hora atuais
agora = datetime.now()

# Adiciona 5 dias à data e hora atuais
futuro = agora + timedelta(days=5)

# Subtrai 2 horas da data e hora atuais
passado = agora - timedelta(hours=2)

print(f"Agora: {agora}")
print(f"Daqui a 5 dias: {futuro}")
print(f"Há 2 horas atrás: {passado}")
