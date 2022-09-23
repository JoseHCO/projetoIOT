import random
import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definition import client_id, user, password, server, port

# Retorna mensagem no console do aquecedor On e Off
def retornoMsg(client, userData, msg):
    # Retorno da Estufa 1
    if msg.topic == f'v1/{user}/things/{client_id}/cmd/2':
        vetor = msg.payload.decode().split(',')
        aquecedor('on' if vetor[1] == '1' else 'off')
        client.publish(
            f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
        a = "True"
        return a

# Conexao com o sistema MQTT
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

# Monitora e Recebe dados da chamada do Aquecedor pela Web
client.on_message = retornoMsg
client.subscribe(f'v1/{user}/things/{client_id}/cmd/#')
client.loop_start()

# Comportamento do sistema
i = 0
bol = True

while bol:
    # Dados Estufa 1
    client.publish(f'v1/{user}/things/{client_id}/data/0', temperatura())
    client.publish(f'v1/{user}/things/{client_id}/data/1', umidade())
    # Timer de Repetição para limitação de dados no sistema
    time.sleep(10)
    i = i+1
    if i == 100:
        bol = False

# Finalização da Sessão
client.disconnect()
