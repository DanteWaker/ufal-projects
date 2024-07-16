# Time:
## Jose Denner Lira do Nascimento
## Rodrigo dos Santos Baptista


## Projeto de Relógios Vetoriais com gRPC em Python
### Este projeto implementa um sistema de relógios vetoriais em um ambiente distribuído utilizando gRPC para comunicação entre processos em Python. Cada processo mantém seu próprio relógio vetorial e comunica-se com outros processos para sincronizar estados, demonstrando a ordenação causal em sistemas distribuídos.

### Pré-Requisitos
Antes de iniciar, certifique-se de ter instalado em sua máquina:

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

Passos:
==============================
git clone [URL do Repositório]
cd [Nome do Diretório do Projeto]
==============================
- Crie e Ative um Ambiente Virtual (opcional, mas recomendado)

No Linux/macOS:
python3 -m venv venv
source venv/bin/activate


No Windows:
python -m venv venv
.\venv\Scripts\activate
Instale as Dependências

Para todos:
pip install grpcio grpcio-tools
Gerando Código a partir de Definições Proto
Antes de executar o servidor e o cliente, você precisa gerar os códigos de stub do gRPC a partir das suas definições .proto.

Gere os Códigos Stub do gRPC

Na raiz do seu projeto, execute:

python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/vector_clock.proto
Certifique-se de que seu arquivo .proto esteja no diretório ./protos e ajuste o comando conforme necessário para corresponder à sua estrutura de diretórios.

Executando o Projeto
Inicie os Servidores

Execute o script Python que inicia os servidores (processos). Cada servidor será iniciado em sua própria thread, escutando em uma porta pré-definida.

python vector_clock_app.py
O script iniciará automaticamente vários servidores em portas diferentes e iniciará a troca de mensagens entre eles.