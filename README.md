# 🚀 SaldoUp API

O **SaldoUp API** é o ecossistema de backend de uma aplicação voltada para o controle de finanças pessoais e gestão de saldos. O projeto foi desenvolvido com foco em alta performance, tipagem forte e uma arquitetura limpa, modular e escalável.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework web de alta performance e documentação automática.
- **Alembic**: Gerenciamento avançado de migrações de banco de dados.
- **Pydantic**: Validação de dados e estruturação de schemas.

---

## 📐 Estrutura e Arquitetura do Projeto

Para garantir as boas práticas de mercado e o isolamento de responsabilidades, o projeto utiliza uma arquitetura modular dividida dentro do diretório `/app`:

- `api/`: Pontos de entrada (endpoints) e controle de rotas de comunicação.
- `core/`: Configurações globais do sistema, segurança e variáveis de ambiente.
- `models/`: Definições das tabelas e relacionamentos do banco de dados.
- `repositories/`: Camada de persistência (comunicação direta com o banco de dados).
- `schemas/`: Validação e serialização de dados com Pydantic.
- `services/`: Camada isolada onde residem as regras de negócio da aplicação.

---

## 🔒 Recursos Já Implementados

- [x] Inicialização e configuração base da API com FastAPI.
- [x] Arquitetura base com rotas modulares utilizando `APIRouter`.
- [x] Sistema estruturado de Autenticação (`/api/auth`).
- [x] Controle e histórico de migrações de banco de dados integrado com Alembic.
- [ ] Implementação das regras de negócio de receitas e despesas *(Em desenvolvimento)*.
- [ ] Integração com banco de dados em produção *(Em desenvolvimento)*.

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de ter o **Python 3.10 ou superior** instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd saldoup-app/backend
   ```

2. **Ative o ambiente virtual (venv):**
   ```bash
   # No Windows:
   .\venvcripts\activate
   # No Linux ou Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências necessárias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode as migrações do banco de dados:**
   ```bash
   alembic upgrade head
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   uvicorn app.main:app --reload
   ```

Acesse a documentação interativa da API gerada automaticamente pelo FastAPI em: `http://127.0.0`
