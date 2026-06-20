# [cite_start]Chat em Tempo Real via Sockets TCP [cite: 3]

[cite_start]Uma aplicação de chat em tempo real com múltiplos usuários, desenvolvida em Python seguindo o modelo cliente-servidor[cite: 5]. [cite_start]A comunicação é feita por meio de sockets TCP, garantindo entrega ordenada e confiável dos dados[cite: 7].

## 📹 Vídeo-Manual
[cite_start][https://youtu.be/rk260HLq00w] [cite: 134]

---

## ⚙️ Arquitetura e Funcionamento

* [cite_start]O sistema é composto por dois módulos independentes: `servidor.py` e `cliente.py`[cite: 12].
* [cite_start]O servidor fica aguardando conexões em uma porta fixa (padrão: 5000)[cite: 13].
* [cite_start]Cada novo cliente que se conecta recebe uma thread dedicada[cite: 14].
* [cite_start]O servidor retransmite cada mensagem recebida para todos os demais participantes da sala (broadcast)[cite: 6].
* [cite_start]Os dados são transmitidos como strings codificadas em UTF-8, suportando caracteres especiais e acentuação[cite: 22].
* [cite_start]O tamanho máximo de cada pacote é de 1024 bytes[cite: 23].
* [cite_start]A lista de clientes ativos é protegida por um `threading.Lock`, evitando condições de corrida durante leitura e escrita concorrentes[cite: 122].

---

## 🛠️ Pré-requisitos

* [cite_start]É necessário ter Python 3.7 ou superior instalado[cite: 98].
* [cite_start]Nenhuma biblioteca externa é requerida[cite: 98].
* [cite_start]O sistema utiliza apenas módulos da biblioteca padrão do Python (`socket` e `threading`)[cite: 99].

---

## 🚀 Como Executar

### 1. Inicializando o Servidor
* [cite_start]Abra um terminal e execute: `python servidor.py`[cite: 101, 102].
* [cite_start]O servidor ficará escutando na porta 5000 de todas as interfaces de rede da máquina[cite: 103].
* [cite_start]Mantenha este terminal aberto durante toda a sessão de chat[cite: 104].

### 2. Conectando os Clientes
* [cite_start]Em cada computador (ou terminal) que deseja participar do chat, execute: `python cliente.py`[cite: 106].
* [cite_start]Para conectar a um servidor em outra máquina, informe o IP e a porta: `python cliente.py 192.168.1.100 5000`[cite: 107].
* [cite_start]Ao conectar, o sistema pedirá que o usuário informe seu apelido[cite: 108].
* [cite_start]Após isso, basta digitar as mensagens e pressionar Enter para enviá-las[cite: 109].

### 3. Comandos do Usuário
* [cite_start]O comando `/sair` encerra a conexão com o servidor e fecha o cliente[cite: 111, 112].

---

## 📂 Estrutura de Arquivos do Projeto

* [cite_start]`servidor.py`: Servidor TCP multithread[cite: 134].
* [cite_start]`cliente.py`: Cliente TCP com thread de recepção[cite: 134].
* [cite_start]`README.md`: Link para o vídeo-manual (YouTube)[cite: 134].

---

## 👥 Autores

* [cite_start]Nicolas Ferezini [cite: 1]
* [cite_start]Christian Ricci [cite: 2]