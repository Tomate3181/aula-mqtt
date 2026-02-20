import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "senai/dev"

client = mqtt.Client()
client.connect(broker, port)

while True:
    mensagem = input("Digite uma mensagem para enviar: ")
    client.publish(topic, mensagem)
    print(f"Mensagem '{mensagem}' publicada no tópico '{topic}'")