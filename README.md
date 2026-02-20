# 📡 Estudo de Protocolo MQTT com Python

Este projeto é um exemplo prático e simples de implementação do protocolo **MQTT (Message Queuing Telemetry Transport)** utilizando a linguagem Python. O objetivo foi estudar os conceitos de **Publish/Subscribe** conectando-se a um broker público.

## 📝 Sobre o Projeto

O script cria um cliente MQTT que atua simultaneamente como:
1.  **Subscriber (Assinante):** Inscreve-se no tópico `senai/dev` para escutar mensagens.
2.  **Publisher (Publicador):** Permite ao usuário digitar mensagens no terminal e enviá-las para o mesmo tópico.

Como o cliente assina e publica no mesmo tópico, você verá o retorno da sua própria mensagem (echo), confirmando que a comunicação com o broker (servidor) foi bem-sucedida.

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Biblioteca:** [Eclipse Paho MQTT Python Client](https://pypi.org/project/paho-mqtt/)
*   **Broker Público:** `broker.hivemq.com` (Porta 1883)

## ⚙️ Pré-requisitos e Instalação

Certifique-se de ter o Python instalado em sua máquina. Em seguida, instale a biblioteca `paho-mqtt` executando o seguinte comando no terminal:

```bash
pip install paho-mqtt
```

## 🚀 Como Executar

1.  Salve o código do projeto em um arquivo, por exemplo: `mqtt_exemplo.py`.
2.  Abra o terminal na pasta do arquivo.
3.  Execute o script:

```bash
python mqtt_exemplo.py
```

4.  O programa irá conectar ao broker e aguardar entrada do usuário.
5.  Digite uma mensagem e pressione **Enter**. Você verá a confirmação de recebimento logo em seguida.

## 🔍 Entendendo o Código

*   **Configurações:** Define o endereço do broker (`broker.hivemq.com`), a porta (`1883`) e o tópico (`senai/dev`).
*   **Callback `on_message`:** Esta função é acionada automaticamente sempre que uma nova mensagem chega no tópico inscrito.
*   **`client.loop_start()`:** Inicia uma thread em segundo plano (background) para gerenciar a conexão e o recebimento de mensagens sem travar o programa principal.
*   **Loop `while True`:** Mantém o programa rodando no terminal para capturar o que o usuário digita e publicar (`client.publish`).

## ⚠️ Aviso Importante

Este exemplo utiliza um **Broker Público** (`broker.hivemq.com`).
*   **Não envie dados sensíveis ou senhas.**
*   Qualquer pessoa no mundo conectada a este broker e inscrita no tópico `senai/dev` poderá ler suas mensagens.

## 🤝 Contribuição

Este código foi desenvolvido para fins educacionais durante estudos sobre IoT e conectividade M2M. Sinta-se à vontade para modificar, mudar o tópico e testar com outros brokers!
