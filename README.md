# 💬 Chat em Tempo Real via Sockets TCP

Uma aplicação de chat em tempo real com múltiplos usuários, desenvolvida em Python seguindo o modelo cliente-servidor. A comunicação é feita por meio de sockets TCP, garantindo entrega ordenada e confiável dos dados.

## 📹 Vídeo-Manual

https://youtu.be/rk260HLq00w

---

## ⚙️ Arquitetura e Funcionamento

* O sistema é composto por dois módulos independentes: `servidor.py` e `cliente.py`.
* O servidor fica aguardando conexões em uma porta fixa (padrão: `5000`).
* Cada novo cliente que se conecta recebe uma thread dedicada.
* O servidor retransmite cada mensagem recebida para todos os demais participantes da sala (*broadcast*).
* Os dados são transmitidos como strings codificadas em UTF-8, suportando caracteres especiais e acentuação.
* O tamanho máximo de cada pacote é de `1024` bytes.
* A lista de clientes ativos é protegida por um `threading.Lock`, evitando condições de corrida durante leitura e escrita concorrentes.

---

## 🛠️ Pré-requisitos

* Python 3.7 ou superior.
* Nenhuma biblioteca externa é necessária.
* O sistema utiliza apenas módulos da biblioteca padrão do Python:

  * `socket`
  * `threading`

---

## 🚀 Como Executar

### 1. Inicializando o Servidor

Abra um terminal e execute:

```bash
python servidor.py
```

O servidor ficará escutando na porta `5000` em todas as interfaces de rede da máquina.

> Mantenha este terminal aberto durante toda a sessão de chat.

### 2. Conectando os Clientes

Em cada computador (ou terminal) que deseja participar do chat, execute:

```bash
python cliente.py
```

Para conectar a um servidor em outra máquina:

```bash
python cliente.py 192.168.1.100 5000
```

Ao conectar:

1. Informe seu apelido (nickname).
2. Digite suas mensagens.
3. Pressione **Enter** para enviá-las.

### 3. Comandos Disponíveis

| Comando | Descrição                                          |
| ------- | -------------------------------------------------- |
| `/sair` | Encerra a conexão com o servidor e fecha o cliente |

---

## 📂 Estrutura do Projeto

```text
.
├── servidor.py   # Servidor TCP multithread
├── cliente.py    # Cliente TCP com thread de recepção
└── README.md     # Documentação do projeto
```

---

## 👥 Autores

* Nicolas Ferezini
* Christian Ricci
