import paho.mqtt.client as mqtt

# ==============================
# Configurações
# ==============================
broker = "broker.hivemq.com"
port = 1883
topic = "senai/dev"

# ==============================
# Callback de recebimento
# ==============================
def on_message(client, userdata, msg):
    print(f"\n Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

# ==============================
# Cliente MQTT
# ==============================
client = mqtt.Client()

client.on_message = on_message
client.connect(broker, port)

# Inscreve no tópico
client.subscribe(topic)

# Inicia loop em background
client.loop_start()

print(f"Conectado ao broker e inscrito no tópico '{topic}'")

# ==============================
# Publicação
# ==============================
while True:
    mensagem = input("Digite uma mensagem para enviar: ")
    client.publish(topic, mensagem)